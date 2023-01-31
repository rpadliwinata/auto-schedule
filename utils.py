from collections import defaultdict
import re
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd
from tempfile import NamedTemporaryFile

def clean_df(raw_df):
    df = raw_df.copy()
    df['Nama Sesuai SSO'] = df['Nama Sesuai SSO'].str.strip()
    df['Nama Sesuai SSO'] = df['Nama Sesuai SSO'].str.title()
    df.columns = list(map(lambda x: x.replace('.', ':'), df.columns))
    df.columns = list(map(lambda x: x.replace('SELESA', 'SELASA'), df.columns))
    df = df.drop_duplicates(subset='Nama Sesuai SSO', keep='last')
    return df

def df_to_schedule(raw_df):
    df = clean_df(raw_df)
    list_nama = df['Nama Sesuai SSO']
    dict_jadwal = {}
    temp_matkul = []
    temp_jadwal = defaultdict(lambda: defaultdict(lambda: {}))
    counter = 0
    for nama in list_nama:
        for key, value in df[df['Nama Sesuai SSO'] == nama].squeeze().items():
            try:
                if value == 'BISA':
                    matkul, hari, jam = re.findall('JAGA\s+(\S+)\s+\[(\S+)\s+(\d{2}[:.]\d{2}\s+-\s+\d{2}[:.]\d{2})', key)[0]
                    temp_jadwal['jadwal'][hari][jam] = None
                    temp_jadwal['appearance'] = 0
                    temp_matkul.append(matkul)
                    counter += 1
            except Exception as e:
                print(str(e))
        temp_jadwal['matkul'] = list(set(temp_matkul))
        temp_jadwal['ketersediaan'] = counter
        dict_jadwal[nama.strip()] = dict(temp_jadwal)
        temp_jadwal = defaultdict(lambda: defaultdict(lambda: {}))
        temp_matkul = []
        counter = 0
    return dict_jadwal

def df_to_excel_schedule(df, judul):
    raw_schedule = df_to_schedule(df)
    asprak_excel = []
    matkul_excel = []
    hari_excel = []
    jam_excel = []
    isi_excel = []
    starts = []
    stops = []
    starts_d = []
    stops_d = []
    temp_start = 2
    temp_stop = 1
    temp_start_d = 2
    temp_stop_d = 1
    for asprak, value in raw_schedule.items():
        matkul_excel.extend(value['matkul'])
        for hari, jadwal in value['jadwal'].items():
            for isi in jadwal.keys():
                asprak_excel.append(asprak)
                matkul_excel.append('')
                hari_excel.append(hari)
                jam_excel.append(isi)
                isi_excel.append('')
                temp_stop += 1
                temp_stop_d += 1
            starts_d.append(temp_start_d)
            stops_d.append(temp_stop_d)
            temp_start_d = temp_stop_d + 1
            temp_stop_d = temp_start_d - 1
        matkul_excel = matkul_excel[:-len(value['matkul'])]
        starts.append(temp_start)
        stops.append(temp_stop)
        temp_start = temp_stop + 1
        temp_stop = temp_start -1
    ready_excel = pd.DataFrame({
        'asprak': asprak_excel,
        'matkul': matkul_excel,
        'hari': hari_excel,
        'jam': jam_excel,
        'isi': isi_excel
    })
    wb = Workbook()
    ws = wb.active
    for r in dataframe_to_rows(ready_excel, index=False, header=True):
        ws.append(r)
    for i in range(len(starts)):
        ws.merge_cells(start_row=starts[i], start_column=1, end_row=stops[i], end_column=1)
    
    for i in range(len(starts_d)):
        ws.merge_cells(start_row=starts_d[i], start_column=3, end_row=stops_d[i], end_column=3)
    
    # with NamedTemporaryFile() as tmp:
    #     wb.save(tmp.name)
    #     tmp.seek(0)
    #     stream = tmp.read()
    
    # return stream
    wb.save(f'{judul}.xlsx')