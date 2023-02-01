from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from utils import df_to_excel_schedule, to_api, assign
from io import StringIO
import pandas as pd
import aiofiles
from deta import Deta

deta = Deta("c09hsnq1_tDcQgDiYGUxUNqFJpMtriV33FU1o1uE5")
drive = deta.Drive('asprak')


app = FastAPI()

@app.post('/upload')
async def upload_csv(in_file: UploadFile = File(...)):
    # df = pd.read_csv(StringIO(str(file.file.read(), 'utf-16')), encoding='utf-16')
    # file = await raw_file.read()
    drive.put('data.csv', StringIO(str(in_file.file.read(), 'utf-8')))
    # async with aiofiles.open('data.csv', 'wb') as out_file:
    #     content = await in_file.read()
    #     await out_file.write(content)
    file = drive.get('data.csv')
    df = pd.read_csv(StringIO(str(file.read(), 'utf-8')), encoding='utf-8')
    
    
    df_to_excel_schedule(df, 'hasil')
    return {'success': True}

@app.get('/file')
async def get_excel():
    return FileResponse('hasil.xlsx')


@app.get('/dummy')
async def get_dummy():
    df = pd.read_csv('data.csv')
    empty_jadwal = assign(df)
    return {
        'status': 200,
        'success': True,
        'message': 'Success',
        'data': to_api(empty_jadwal)
    }
