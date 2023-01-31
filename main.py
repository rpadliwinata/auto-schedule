from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from utils import df_to_excel_schedule
from io import StringIO
import pandas as pd


app = FastAPI()

@app.post('/upload')
async def upload_csv(raw_file: UploadFile = File(...)):
    # df = pd.read_csv(StringIO(str(file.file.read(), 'utf-16')), encoding='utf-16')
    # file = await raw_file.read()
    df = pd.read_csv(StringIO(raw_file.file.read().decode('utf-8')), encoding='utf-8')
    df_to_excel_schedule(df, 'hasil')
    return {'success': True}

@app.get('/file')
async def get_excel():
    return FileResponse('hasil.xlsx')


@app.get('/new')
async def new_dummy():
    return {
        'status': 200,
        'success': True,
        'message': 'Success',
        'data': {
            "RABU": {
                "09:30 - 12:30": [
                    {
                        "ruang": None,
                        "matkul": "ALPRO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Andi Muh. Syahrul Ulum",
                            "Rama Padliwinata",
                            "Mohammad Mirza Qusyairi",
                            "David Dharmawan Saputra",
                            "I Putu Sri Randha Yoga",
                            "Khalilullah Al Faath"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Satrio Nurcahya",
                            "Zadosaadi Brahmantio Purwanto",
                            "Muhammad Qalbun Saliim Bakhri",
                            "Fakhri Maulana Falah",
                            "Ihsani Hawa Arsytania",
                            "Andhika Putra"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Azriel Farasfauzan Sepvira",
                            "Ananda Ardian Pratama Putra",
                            "Reva Doni Aprilio",
                            "Sabrinaadindasari",
                            "Wana Ardilah Iwan",
                            "Muhammad Abdul Aziz"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Chara Maria Emmanuel Yuliarta",
                            "Naufal Rafi Adiansyah",
                            "Muhammad Farras Aditya",
                            "Alfransis Perugia Bennybeng Holle",
                            "Muhammad Noer Ibnu Sina",
                            "Ryan Rizky Rizwandy"
                        ]
                    }
                ],
                "06:30 - 09:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Satrio Nurcahya",
                            "Andi Muh. Syahrul Ulum",
                            "Muhammad Qalbun Saliim Bakhri",
                            "Rama Padliwinata",
                            "Muhammad Daffa Ferdiansyah",
                            "Mrizkyfirdaus@Student.Telkomuniversity.Ac.Id"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Azriel Farasfauzan Sepvira",
                            "Ananda Ardian Pratama Putra",
                            "Reva Doni Aprilio",
                            "Sabrinaadindasari",
                            "Wana Ardilah Iwan"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Chara Maria Emmanuel Yuliarta",
                            "Naufal Rafi Adiansyah",
                            "Alfransis Perugia Bennybeng Holle",
                            "Alifya Fatimah Ariyanto",
                            "Rafly Athalla",
                            "Muhammad Azmi Faizuddin Permana"
                        ]
                    }
                ],
                "12:30 - 15:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Satrio Nurcahya",
                            "Zadosaadi Brahmantio Purwanto",
                            "Andi Muh. Syahrul Ulum",
                            "Nada Fajri Mufidah",
                            "Olaza Aurora Syafira",
                            "Alfransis Perugia Bennybeng Holle"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Aulia Maharani",
                            "Azriel Farasfauzan Sepvira",
                            "Ananda Ardian Pratama Putra",
                            "Sabrinaadindasari",
                            "Wana Ardilah Iwan",
                            "Windy Ramadhanti"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Andhika Bayu Yudhistira Arda Putra",
                            "Naufal Rafi Adiansyah",
                            "Moh Adi Ikfini M",
                            "Muhammad Noer Ibnu Sina",
                            "Ryan Rizky Rizwandy",
                            "Alifya Fatimah Ariyanto"
                        ]
                    }
                ],
                "15:30 - 18:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Satrio Nurcahya",
                            "Talitha Nabila",
                            "Zadosaadi Brahmantio Purwanto",
                            "Andi Muh. Syahrul Ulum",
                            "Orvala Azzurri Madhyastha",
                            "Nada Fajri Mufidah"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Aulia Maharani",
                            "Azriel Farasfauzan Sepvira",
                            "Ananda Ardian Pratama Putra",
                            "Nia Madu Marliana",
                            "Sabrinaadindasari",
                            "Wana Ardilah Iwan"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Andhika Bayu Yudhistira Arda Putra",
                            "Naufal Rafi Adiansyah",
                            "Alfransis Perugia Bennybeng Holle",
                            "Rafly Athalla",
                            "Muhammad Azmi Faizuddin Permana"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISOP",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Muhamad Agil Fachrian",
                            "Zalfaa Putri Ayudhia",
                            "Muhammad Aga Ananda Said Muharam",
                            "Mohammad Mirza Qusyairi",
                            "Ahmad Fakih",
                            "Sabila Amanda Putri Riyadi"
                        ]
                    }
                ]
            },
            "KAMIS": {
                "15:30 - 18:30": [
                    {
                        "ruang": None,
                        "matkul": "ALPRO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Zharfan Dawud Harwiraputera",
                            "Talitha Nabila",
                            "Andi Muh. Syahrul Ulum",
                            "Nada Fajri Mufidah",
                            "Mohammad Mirza Qusyairi",
                            "Aidil Arifin Nizar"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Satrio Nurcahya",
                            "Salsa Arifah Zakkiya",
                            "Zadosaadi Brahmantio Purwanto",
                            "Rayhan Risq Arya Brinanta",
                            "Andhika Putra",
                            "Muhamad Rafli Susanto"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Muhammad Haykal Kamil",
                            "Nia Madu Marliana",
                            "Sabrinaadindasari",
                            "Wana Ardilah Iwan",
                            "Ahmad Fathan Hanif"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Chara Maria Emmanuel Yuliarta",
                            "Naufal Rafi Adiansyah",
                            "Alfransis Perugia Bennybeng Holle",
                            "Muhammad Fachri Habibi",
                            "Muhammad Azmi Faizuddin Permana"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "WEBPRO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Deni Panji Dirgantara",
                            "Fauzan Reza Arnanda",
                            "Leonardho R Sitanggang",
                            "Rizky Naufal Alghifari",
                            "Maulana Akbar Ramadhan",
                            "Haqila Nur Nouvadila"
                        ]
                    }
                ],
                "18:30 - 21:30": [
                    {
                        "ruang": None,
                        "matkul": "ALPRO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Zalfaa Putri Ayudhia",
                            "Zharfan Dawud Harwiraputera",
                            "Ariq Heritsa Maalik",
                            "Rama Padliwinata",
                            "Orvala Azzurri Madhyastha",
                            "Nada Fajri Mufidah"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Chara Maria Emmanuel Yuliarta",
                            "Andhika Bayu Yudhistira Arda Putra",
                            "I Wayan Adi Wahyudi",
                            "Muhammad Azmi Faizuddin Permana"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "ABP",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Sanding Adhieguna Rachmat Yasin",
                            "Deni Panji Dirgantara"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "JARKOM",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Aulia Maharani",
                            "Muhamad Agil Fachrian"
                        ]
                    }
                ],
                "06:30 - 09:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Orvala Azzurri Madhyastha",
                            "Nada Fajri Mufidah",
                            "Fakhri Maulana Falah",
                            "Olaza Aurora Syafira",
                            "Muhammad Fadil Maulana Akbar",
                            "Muhammad Daffa Ferdiansyah"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Azriel Farasfauzan Sepvira",
                            "Ananda Ardian Pratama Putra",
                            "Windy Ramadhanti",
                            "Ahmad Fathan Hanif",
                            "Moh Adi Ikfini M"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "I Wayan Adi Wahyudi",
                            "Muhammad Azmi Faizuddin Permana"
                        ]
                    }
                ],
                "09:30 - 12:30": [
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Muhammad Haykal Kamil",
                            "Nia Madu Marliana",
                            "Ahmad Fathan Hanif",
                            "Muhammad Abdul Aziz"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "I Wayan Adi Wahyudi",
                            "Ryan Rizky Rizwandy",
                            "Alifya Fatimah Ariyanto",
                            "Rifki Adi Pramana",
                            "Muhammad Fachri Habibi"
                        ]
                    }
                ],
                "12:30 - 15:30": [
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "I Wayan Adi Wahyudi",
                            "Muhammad Fachri Habibi"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PPL",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Muhammad Aga Ananda Said Muharam",
                            "Maulana Akbar Ramadhan",
                            "Alya Ghaitsa Rizky Pertiwi",
                            "Fathaya Nur Annisa",
                            "Falia Aufa Najla'",
                            "Rere Chintya"
                        ]
                    }
                ]
            },
            "JUMAT": {
                "07:30 - 10:30": [
                    {
                        "ruang": None,
                        "matkul": "ALPRO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Ariq Heritsa Maalik",
                            "Mohammad Mirza Qusyairi",
                            "Aidil Arifin Nizar",
                            "Jaatsiyah Maulidina Astrianto",
                            "Muhammad Baari Adli",
                            "Hidayat Taufiqur Rahmah Achmad"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISOP",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Muhamad Agil Fachrian",
                            "Radli Maulana Arief",
                            "Windy Ramadhanti",
                            "Muhammad Aga Ananda Said Muharam",
                            "Ahmad Fakih",
                            "Sabila Amanda Putri Riyadi"
                        ]
                    }
                ],
                "13:30 - 16:30": [
                    {
                        "ruang": None,
                        "matkul": "ALPRO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Zalfaa Putri Ayudhia",
                            "Mohammad Mirza Qusyairi",
                            "Aidil Arifin Nizar",
                            "David Dharmawan Saputra",
                            "Rayhan Suryatama Raharyawhedi",
                            "Prins Naval Nuzeren"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Ihsani Hawa Arsytania",
                            "Muhammad Fadil Maulana Akbar",
                            "Muhammad Daffa Ferdiansyah",
                            "Mrizkyfirdaus@Student.Telkomuniversity.Ac.Id",
                            "Muhamad Rafli Susanto",
                            "Bagus Hariyadi"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Aulia Maharani",
                            "Nia Madu Marliana",
                            "Ardiansa Saputra"
                        ]
                    }
                ]
            },
            "SENIN": {
                "06:30 - 09:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Salsa Arifah Zakkiya",
                            "Muhammad Qalbun Saliim Bakhri",
                            "Rama Padliwinata",
                            "Karuna Dewa Satyananda",
                            "Rayhan Risq Arya Brinanta",
                            "Olaza Aurora Syafira"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Nia Madu Marliana",
                            "Reva Doni Aprilio",
                            "Ardiansa Saputra",
                            "Windy Ramadhanti",
                            "Moh Adi Ikfini M"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": []
                    },
                    {
                        "ruang": None,
                        "matkul": "WEBPRO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Deni Panji Dirgantara",
                            "Fauzan Reza Arnanda",
                            "Leonardho R Sitanggang",
                            "Ihsan Asfari Hanifan",
                            "Rizal Maidan Firdaus",
                            "I Komang Danda Priyowittesa"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISOP",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Muhamad Agil Fachrian",
                            "Radli Maulana Arief",
                            "Muhammad Aga Ananda Said Muharam",
                            "Aidil Arifin Nizar",
                            "Addin Amanatulloh Suparjo",
                            "Yunolva Anis Ramaziyah"
                        ]
                    }
                ],
                "09:30 - 12:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Ariq Heritsa Maalik",
                            "Talitha Nabila",
                            "Muhammad Qalbun Saliim Bakhri",
                            "Rama Padliwinata",
                            "Karuna Dewa Satyananda",
                            "Moh Naufal Mizan Saputro"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Aulia Maharani",
                            "Reva Doni Aprilio",
                            "Ardiansa Saputra",
                            "Windy Ramadhanti",
                            "Muhammad Abdul Aziz",
                            "Moh Adi Ikfini M"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "I Wayan Adi Wahyudi",
                            "Muhammad Farras Aditya",
                            "Muhammad Noer Ibnu Sina",
                            "Ryan Rizky Rizwandy",
                            "Muhammad Iqbal",
                            "Rifki Adi Pramana"
                        ]
                    }
                ],
                "12:30 - 15:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Talitha Nabila",
                            "Muhamad Rafli Susanto",
                            "Rayhan Suryatama Raharyawhedi",
                            "Bagus Hariyadi",
                            "Shidqi Fadhlurrahman Yusri",
                            "Muhammad Baari Adli"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Muhammad Abdul Aziz",
                            "Moh Adi Ikfini M"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Andhika Bayu Yudhistira Arda Putra",
                            "Muhammad Farras Aditya",
                            "Muhammad Noer Ibnu Sina",
                            "Ryan Rizky Rizwandy",
                            "Muhammad Iqbal",
                            "Rifki Adi Pramana"
                        ]
                    }
                ],
                "15:30 - 18:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Talitha Nabila",
                            "Zadosaadi Brahmantio Purwanto",
                            "Rayhan Risq Arya Brinanta",
                            "Olaza Aurora Syafira",
                            "Ihsani Hawa Arsytania",
                            "Muhamad Rafli Susanto"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Ardiansa Saputra"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Chara Maria Emmanuel Yuliarta",
                            "Andhika Bayu Yudhistira Arda Putra",
                            "Muhammad Farras Aditya"
                        ]
                    }
                ],
                "18:30 - 21:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Muhammad Qalbun Saliim Bakhri",
                            "Orvala Azzurri Madhyastha",
                            "Rayhan Risq Arya Brinanta",
                            "Olaza Aurora Syafira",
                            "Ihsani Hawa Arsytania",
                            "Muhammad Fadil Maulana Akbar"
                        ]
                    }
                ]
            },
            "SELASA": {
                "06:30 - 09:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Rayhan Risq Arya Brinanta",
                            "Ihsani Hawa Arsytania",
                            "Muhammad Daffa Ferdiansyah",
                            "Mrizkyfirdaus@Student.Telkomuniversity.Ac.Id",
                            "Moh Naufal Mizan Saputro",
                            "Shidqi Fadhlurrahman Yusri"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Ardiansa Saputra"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "WEBPRO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Fauzan Reza Arnanda",
                            "Leonardho R Sitanggang",
                            "Ihsan Asfari Hanifan",
                            "Rizal Maidan Firdaus",
                            "I Komang Danda Priyowittesa",
                            "Rizky Naufal Alghifari"
                        ]
                    }
                ],
                "09:30 - 12:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Moh Naufal Mizan Saputro",
                            "Adinda Arwa Salsabil",
                            "Alifya Fatimah Ariyanto",
                            "Dewa Made Wijaya",
                            "Alifya Aisyah Ariyanto"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Muhammad Abdul Aziz"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "WEBPRO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Fauzan Reza Arnanda",
                            "Leonardho R Sitanggang",
                            "Ihsan Asfari Hanifan",
                            "Rizal Maidan Firdaus",
                            "I Komang Danda Priyowittesa",
                            "Rizky Naufal Alghifari"
                        ]
                    }
                ],
                "12:30 - 15:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Orvala Azzurri Madhyastha",
                            "Andhika Putra",
                            "Harvian Khusnan Hafidz",
                            "Moh Naufal Mizan Saputro",
                            "Khalilullah Al Faath",
                            "Alifya Fatimah Ariyanto"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Ahmad Fathan Hanif"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Muhammad Noer Ibnu Sina",
                            "Rafly Athalla",
                            "Muhammad Fachri Habibi"
                        ]
                    }
                ],
                "15:30 - 18:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Salsa Arifah Zakkiya",
                            "Karuna Dewa Satyananda",
                            "Andhika Putra",
                            "Harvian Khusnan Hafidz",
                            "Khalilullah Al Faath",
                            "Shidqi Fadhlurrahman Yusri"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Muhammad Haykal Kamil",
                            "Ahmad Fathan Hanif"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISTER",
                        "kelas": None,
                        "dosen": None,
                        "asprak": []
                    }
                ],
                "18:30 - 21:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Andhika Putra",
                            "Harvian Khusnan Hafidz",
                            "Muhammad Fadil Maulana Akbar",
                            "Muhammad Daffa Ferdiansyah",
                            "Mrizkyfirdaus@Student.Telkomuniversity.Ac.Id",
                            "Muhamad Rafli Susanto"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "SISOP",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Zalfaa Putri Ayudhia",
                            "Muhammad Aga Ananda Said Muharam",
                            "Ahmad Fakih",
                            "Aidil Arifin Nizar",
                            "Addin Amanatulloh Suparjo",
                            "Yunolva Anis Ramaziyah"
                        ]
                    }
                ]
            },
            "SABTU": {
                "09:30 - 12:30": [
                    {
                        "ruang": None,
                        "matkul": "STD",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Harvian Khusnan Hafidz",
                            "Moh Naufal Mizan Saputro",
                            "Rayhan Suryatama Raharyawhedi",
                            "Bagus Hariyadi",
                            "Khalilullah Al Faath",
                            "Adinda Arwa Salsabil"
                        ]
                    },
                    {
                        "ruang": None,
                        "matkul": "ALPRO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Zharfan Dawud Harwiraputera",
                            "Jaatsiyah Maulidina Astrianto",
                            "Muhamad Raihan Ramadhan",
                            "Prins Naval Nuzeren",
                            "Nitamayega",
                            "Glorious Satria Dhamang Aji"
                        ]
                    }
                ],
                "14:30 - 17:30": [
                    {
                        "ruang": None,
                        "matkul": "PBO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Muhammad Haykal Kamil",
                            "Reva Doni Aprilio"
                        ]
                    }
                ],
                "06:30 - 09:30": [
                    {
                        "ruang": None,
                        "matkul": "WEBPRO",
                        "kelas": None,
                        "dosen": None,
                        "asprak": [
                            "Deni Panji Dirgantara",
                            "Maulana Akbar Ramadhan",
                            "Ananta Noviandanu"
                        ]
                    }
                ]
            }
        }

    }


@app.get('/dummy')
async def get_dummy():
    return {
        'status': 200,
        'success': True,
        'message': 'Success',
        'data': [
            {
                "ruang": None,
                "matkul": "ALPRO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Andi Muh. Syahrul Ulum",
                    "Rama Padliwinata",
                    "Mohammad Mirza Qusyairi",
                    "David Dharmawan Saputra",
                    "I Putu Sri Randha Yoga",
                    "Khalilullah Al Faath"
                ],
                "hari": "RABU",
                "jam": "09:30 - 12:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Satrio Nurcahya",
                    "Zadosaadi Brahmantio Purwanto",
                    "Muhammad Qalbun Saliim Bakhri",
                    "Fakhri Maulana Falah",
                    "Ihsani Hawa Arsytania",
                    "Andhika Putra"
                ],
                "hari": "RABU",
                "jam": "09:30 - 12:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Azriel Farasfauzan Sepvira",
                    "Ananda Ardian Pratama Putra",
                    "Reva Doni Aprilio",
                    "Sabrinaadindasari",
                    "Wana Ardilah Iwan",
                    "Muhammad Abdul Aziz"
                ],
                "hari": "RABU",
                "jam": "09:30 - 12:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Chara Maria Emmanuel Yuliarta",
                    "Naufal Rafi Adiansyah",
                    "Muhammad Farras Aditya",
                    "Alfransis Perugia Bennybeng Holle",
                    "Muhammad Noer Ibnu Sina",
                    "Ryan Rizky Rizwandy"
                ],
                "hari": "RABU",
                "jam": "09:30 - 12:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Satrio Nurcahya",
                    "Andi Muh. Syahrul Ulum",
                    "Muhammad Qalbun Saliim Bakhri",
                    "Rama Padliwinata",
                    "Muhammad Daffa Ferdiansyah",
                    "Mrizkyfirdaus@Student.Telkomuniversity.Ac.Id"
                ],
                "hari": "RABU",
                "jam": "06:30 - 09:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Azriel Farasfauzan Sepvira",
                    "Ananda Ardian Pratama Putra",
                    "Reva Doni Aprilio",
                    "Sabrinaadindasari",
                    "Wana Ardilah Iwan"
                ],
                "hari": "RABU",
                "jam": "06:30 - 09:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Chara Maria Emmanuel Yuliarta",
                    "Naufal Rafi Adiansyah",
                    "Alfransis Perugia Bennybeng Holle",
                    "Alifya Fatimah Ariyanto",
                    "Rafly Athalla",
                    "Muhammad Azmi Faizuddin Permana"
                ],
                "hari": "RABU",
                "jam": "06:30 - 09:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Satrio Nurcahya",
                    "Zadosaadi Brahmantio Purwanto",
                    "Andi Muh. Syahrul Ulum",
                    "Nada Fajri Mufidah",
                    "Olaza Aurora Syafira",
                    "Alfransis Perugia Bennybeng Holle"
                ],
                "hari": "RABU",
                "jam": "12:30 - 15:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Aulia Maharani",
                    "Azriel Farasfauzan Sepvira",
                    "Ananda Ardian Pratama Putra",
                    "Sabrinaadindasari",
                    "Wana Ardilah Iwan",
                    "Windy Ramadhanti"
                ],
                "hari": "RABU",
                "jam": "12:30 - 15:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Andhika Bayu Yudhistira Arda Putra",
                    "Naufal Rafi Adiansyah",
                    "Moh Adi Ikfini M",
                    "Muhammad Noer Ibnu Sina",
                    "Ryan Rizky Rizwandy",
                    "Alifya Fatimah Ariyanto"
                ],
                "hari": "RABU",
                "jam": "12:30 - 15:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Satrio Nurcahya",
                    "Talitha Nabila",
                    "Zadosaadi Brahmantio Purwanto",
                    "Andi Muh. Syahrul Ulum",
                    "Orvala Azzurri Madhyastha",
                    "Nada Fajri Mufidah"
                ],
                "hari": "RABU",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Aulia Maharani",
                    "Azriel Farasfauzan Sepvira",
                    "Ananda Ardian Pratama Putra",
                    "Nia Madu Marliana",
                    "Sabrinaadindasari",
                    "Wana Ardilah Iwan"
                ],
                "hari": "RABU",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Andhika Bayu Yudhistira Arda Putra",
                    "Naufal Rafi Adiansyah",
                    "Alfransis Perugia Bennybeng Holle",
                    "Rafly Athalla",
                    "Muhammad Azmi Faizuddin Permana"
                ],
                "hari": "RABU",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "SISOP",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Muhamad Agil Fachrian",
                    "Zalfaa Putri Ayudhia",
                    "Muhammad Aga Ananda Said Muharam",
                    "Mohammad Mirza Qusyairi",
                    "Ahmad Fakih",
                    "Sabila Amanda Putri Riyadi"
                ],
                "hari": "RABU",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "ALPRO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Zharfan Dawud Harwiraputera",
                    "Talitha Nabila",
                    "Andi Muh. Syahrul Ulum",
                    "Nada Fajri Mufidah",
                    "Mohammad Mirza Qusyairi",
                    "Aidil Arifin Nizar"
                ],
                "hari": "KAMIS",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Satrio Nurcahya",
                    "Salsa Arifah Zakkiya",
                    "Zadosaadi Brahmantio Purwanto",
                    "Rayhan Risq Arya Brinanta",
                    "Andhika Putra",
                    "Muhamad Rafli Susanto"
                ],
                "hari": "KAMIS",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Muhammad Haykal Kamil",
                    "Nia Madu Marliana",
                    "Sabrinaadindasari",
                    "Wana Ardilah Iwan",
                    "Ahmad Fathan Hanif"
                ],
                "hari": "KAMIS",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Chara Maria Emmanuel Yuliarta",
                    "Naufal Rafi Adiansyah",
                    "Alfransis Perugia Bennybeng Holle",
                    "Muhammad Fachri Habibi",
                    "Muhammad Azmi Faizuddin Permana"
                ],
                "hari": "KAMIS",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "WEBPRO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Deni Panji Dirgantara",
                    "Fauzan Reza Arnanda",
                    "Leonardho R Sitanggang",
                    "Rizky Naufal Alghifari",
                    "Maulana Akbar Ramadhan",
                    "Haqila Nur Nouvadila"
                ],
                "hari": "KAMIS",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "ALPRO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Zalfaa Putri Ayudhia",
                    "Zharfan Dawud Harwiraputera",
                    "Ariq Heritsa Maalik",
                    "Rama Padliwinata",
                    "Orvala Azzurri Madhyastha",
                    "Nada Fajri Mufidah"
                ],
                "hari": "KAMIS",
                "jam": "18:30 - 21:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Chara Maria Emmanuel Yuliarta",
                    "Andhika Bayu Yudhistira Arda Putra",
                    "I Wayan Adi Wahyudi",
                    "Muhammad Azmi Faizuddin Permana"
                ],
                "hari": "KAMIS",
                "jam": "18:30 - 21:30"
            },
            {
                "ruang": None,
                "matkul": "ABP",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Sanding Adhieguna Rachmat Yasin",
                    "Deni Panji Dirgantara"
                ],
                "hari": "KAMIS",
                "jam": "18:30 - 21:30"
            },
            {
                "ruang": None,
                "matkul": "JARKOM",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Aulia Maharani",
                    "Muhamad Agil Fachrian"
                ],
                "hari": "KAMIS",
                "jam": "18:30 - 21:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Orvala Azzurri Madhyastha",
                    "Nada Fajri Mufidah",
                    "Fakhri Maulana Falah",
                    "Olaza Aurora Syafira",
                    "Muhammad Fadil Maulana Akbar",
                    "Muhammad Daffa Ferdiansyah"
                ],
                "hari": "KAMIS",
                "jam": "06:30 - 09:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Azriel Farasfauzan Sepvira",
                    "Ananda Ardian Pratama Putra",
                    "Windy Ramadhanti",
                    "Ahmad Fathan Hanif",
                    "Moh Adi Ikfini M"
                ],
                "hari": "KAMIS",
                "jam": "06:30 - 09:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "I Wayan Adi Wahyudi",
                    "Muhammad Azmi Faizuddin Permana"
                ],
                "hari": "KAMIS",
                "jam": "06:30 - 09:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Muhammad Haykal Kamil",
                    "Nia Madu Marliana",
                    "Ahmad Fathan Hanif",
                    "Muhammad Abdul Aziz"
                ],
                "hari": "KAMIS",
                "jam": "09:30 - 12:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "I Wayan Adi Wahyudi",
                    "Ryan Rizky Rizwandy",
                    "Alifya Fatimah Ariyanto",
                    "Rifki Adi Pramana",
                    "Muhammad Fachri Habibi"
                ],
                "hari": "KAMIS",
                "jam": "09:30 - 12:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "I Wayan Adi Wahyudi",
                    "Muhammad Fachri Habibi"
                ],
                "hari": "KAMIS",
                "jam": "12:30 - 15:30"
            },
            {
                "ruang": None,
                "matkul": "PPL",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Muhammad Aga Ananda Said Muharam",
                    "Maulana Akbar Ramadhan",
                    "Alya Ghaitsa Rizky Pertiwi",
                    "Fathaya Nur Annisa",
                    "Falia Aufa Najla'",
                    "Rere Chintya"
                ],
                "hari": "KAMIS",
                "jam": "12:30 - 15:30"
            },
            {
                "ruang": None,
                "matkul": "ALPRO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Ariq Heritsa Maalik",
                    "Mohammad Mirza Qusyairi",
                    "Aidil Arifin Nizar",
                    "Jaatsiyah Maulidina Astrianto",
                    "Muhammad Baari Adli",
                    "Hidayat Taufiqur Rahmah Achmad"
                ],
                "hari": "JUMAT",
                "jam": "07:30 - 10:30"
            },
            {
                "ruang": None,
                "matkul": "SISOP",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Muhamad Agil Fachrian",
                    "Radli Maulana Arief",
                    "Windy Ramadhanti",
                    "Muhammad Aga Ananda Said Muharam",
                    "Ahmad Fakih",
                    "Sabila Amanda Putri Riyadi"
                ],
                "hari": "JUMAT",
                "jam": "07:30 - 10:30"
            },
            {
                "ruang": None,
                "matkul": "ALPRO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Zalfaa Putri Ayudhia",
                    "Mohammad Mirza Qusyairi",
                    "Aidil Arifin Nizar",
                    "David Dharmawan Saputra",
                    "Rayhan Suryatama Raharyawhedi",
                    "Prins Naval Nuzeren"
                ],
                "hari": "JUMAT",
                "jam": "13:30 - 16:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Ihsani Hawa Arsytania",
                    "Muhammad Fadil Maulana Akbar",
                    "Muhammad Daffa Ferdiansyah",
                    "Mrizkyfirdaus@Student.Telkomuniversity.Ac.Id",
                    "Muhamad Rafli Susanto",
                    "Bagus Hariyadi"
                ],
                "hari": "JUMAT",
                "jam": "13:30 - 16:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Aulia Maharani",
                    "Nia Madu Marliana",
                    "Ardiansa Saputra"
                ],
                "hari": "JUMAT",
                "jam": "13:30 - 16:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Salsa Arifah Zakkiya",
                    "Muhammad Qalbun Saliim Bakhri",
                    "Rama Padliwinata",
                    "Karuna Dewa Satyananda",
                    "Rayhan Risq Arya Brinanta",
                    "Olaza Aurora Syafira"
                ],
                "hari": "SENIN",
                "jam": "06:30 - 09:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Nia Madu Marliana",
                    "Reva Doni Aprilio",
                    "Ardiansa Saputra",
                    "Windy Ramadhanti",
                    "Moh Adi Ikfini M"
                ],
                "hari": "SENIN",
                "jam": "06:30 - 09:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [],
                "hari": "SENIN",
                "jam": "06:30 - 09:30"
            },
            {
                "ruang": None,
                "matkul": "WEBPRO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Deni Panji Dirgantara",
                    "Fauzan Reza Arnanda",
                    "Leonardho R Sitanggang",
                    "Ihsan Asfari Hanifan",
                    "Rizal Maidan Firdaus",
                    "I Komang Danda Priyowittesa"
                ],
                "hari": "SENIN",
                "jam": "06:30 - 09:30"
            },
            {
                "ruang": None,
                "matkul": "SISOP",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Muhamad Agil Fachrian",
                    "Radli Maulana Arief",
                    "Muhammad Aga Ananda Said Muharam",
                    "Aidil Arifin Nizar",
                    "Addin Amanatulloh Suparjo",
                    "Yunolva Anis Ramaziyah"
                ],
                "hari": "SENIN",
                "jam": "06:30 - 09:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Ariq Heritsa Maalik",
                    "Talitha Nabila",
                    "Muhammad Qalbun Saliim Bakhri",
                    "Rama Padliwinata",
                    "Karuna Dewa Satyananda",
                    "Moh Naufal Mizan Saputro"
                ],
                "hari": "SENIN",
                "jam": "09:30 - 12:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Aulia Maharani",
                    "Reva Doni Aprilio",
                    "Ardiansa Saputra",
                    "Windy Ramadhanti",
                    "Muhammad Abdul Aziz",
                    "Moh Adi Ikfini M"
                ],
                "hari": "SENIN",
                "jam": "09:30 - 12:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "I Wayan Adi Wahyudi",
                    "Muhammad Farras Aditya",
                    "Muhammad Noer Ibnu Sina",
                    "Ryan Rizky Rizwandy",
                    "Muhammad Iqbal",
                    "Rifki Adi Pramana"
                ],
                "hari": "SENIN",
                "jam": "09:30 - 12:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Talitha Nabila",
                    "Muhamad Rafli Susanto",
                    "Rayhan Suryatama Raharyawhedi",
                    "Bagus Hariyadi",
                    "Shidqi Fadhlurrahman Yusri",
                    "Muhammad Baari Adli"
                ],
                "hari": "SENIN",
                "jam": "12:30 - 15:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Muhammad Abdul Aziz",
                    "Moh Adi Ikfini M"
                ],
                "hari": "SENIN",
                "jam": "12:30 - 15:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Andhika Bayu Yudhistira Arda Putra",
                    "Muhammad Farras Aditya",
                    "Muhammad Noer Ibnu Sina",
                    "Ryan Rizky Rizwandy",
                    "Muhammad Iqbal",
                    "Rifki Adi Pramana"
                ],
                "hari": "SENIN",
                "jam": "12:30 - 15:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Talitha Nabila",
                    "Zadosaadi Brahmantio Purwanto",
                    "Rayhan Risq Arya Brinanta",
                    "Olaza Aurora Syafira",
                    "Ihsani Hawa Arsytania",
                    "Muhamad Rafli Susanto"
                ],
                "hari": "SENIN",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Ardiansa Saputra"
                ],
                "hari": "SENIN",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Chara Maria Emmanuel Yuliarta",
                    "Andhika Bayu Yudhistira Arda Putra",
                    "Muhammad Farras Aditya"
                ],
                "hari": "SENIN",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Muhammad Qalbun Saliim Bakhri",
                    "Orvala Azzurri Madhyastha",
                    "Rayhan Risq Arya Brinanta",
                    "Olaza Aurora Syafira",
                    "Ihsani Hawa Arsytania",
                    "Muhammad Fadil Maulana Akbar"
                ],
                "hari": "SENIN",
                "jam": "18:30 - 21:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Rayhan Risq Arya Brinanta",
                    "Ihsani Hawa Arsytania",
                    "Muhammad Daffa Ferdiansyah",
                    "Mrizkyfirdaus@Student.Telkomuniversity.Ac.Id",
                    "Moh Naufal Mizan Saputro",
                    "Shidqi Fadhlurrahman Yusri"
                ],
                "hari": "SELASA",
                "jam": "06:30 - 09:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Ardiansa Saputra"
                ],
                "hari": "SELASA",
                "jam": "06:30 - 09:30"
            },
            {
                "ruang": None,
                "matkul": "WEBPRO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Fauzan Reza Arnanda",
                    "Leonardho R Sitanggang",
                    "Ihsan Asfari Hanifan",
                    "Rizal Maidan Firdaus",
                    "I Komang Danda Priyowittesa",
                    "Rizky Naufal Alghifari"
                ],
                "hari": "SELASA",
                "jam": "06:30 - 09:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Moh Naufal Mizan Saputro",
                    "Adinda Arwa Salsabil",
                    "Alifya Fatimah Ariyanto",
                    "Dewa Made Wijaya",
                    "Alifya Aisyah Ariyanto"
                ],
                "hari": "SELASA",
                "jam": "09:30 - 12:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Muhammad Abdul Aziz"
                ],
                "hari": "SELASA",
                "jam": "09:30 - 12:30"
            },
            {
                "ruang": None,
                "matkul": "WEBPRO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Fauzan Reza Arnanda",
                    "Leonardho R Sitanggang",
                    "Ihsan Asfari Hanifan",
                    "Rizal Maidan Firdaus",
                    "I Komang Danda Priyowittesa",
                    "Rizky Naufal Alghifari"
                ],
                "hari": "SELASA",
                "jam": "09:30 - 12:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Orvala Azzurri Madhyastha",
                    "Andhika Putra",
                    "Harvian Khusnan Hafidz",
                    "Moh Naufal Mizan Saputro",
                    "Khalilullah Al Faath",
                    "Alifya Fatimah Ariyanto"
                ],
                "hari": "SELASA",
                "jam": "12:30 - 15:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Ahmad Fathan Hanif"
                ],
                "hari": "SELASA",
                "jam": "12:30 - 15:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Muhammad Noer Ibnu Sina",
                    "Rafly Athalla",
                    "Muhammad Fachri Habibi"
                ],
                "hari": "SELASA",
                "jam": "12:30 - 15:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Salsa Arifah Zakkiya",
                    "Karuna Dewa Satyananda",
                    "Andhika Putra",
                    "Harvian Khusnan Hafidz",
                    "Khalilullah Al Faath",
                    "Shidqi Fadhlurrahman Yusri"
                ],
                "hari": "SELASA",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Muhammad Haykal Kamil",
                    "Ahmad Fathan Hanif"
                ],
                "hari": "SELASA",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "SISTER",
                "kelas": None,
                "dosen": None,
                "asprak": [],
                "hari": "SELASA",
                "jam": "15:30 - 18:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Andhika Putra",
                    "Harvian Khusnan Hafidz",
                    "Muhammad Fadil Maulana Akbar",
                    "Muhammad Daffa Ferdiansyah",
                    "Mrizkyfirdaus@Student.Telkomuniversity.Ac.Id",
                    "Muhamad Rafli Susanto"
                ],
                "hari": "SELASA",
                "jam": "18:30 - 21:30"
            },
            {
                "ruang": None,
                "matkul": "SISOP",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Zalfaa Putri Ayudhia",
                    "Muhammad Aga Ananda Said Muharam",
                    "Ahmad Fakih",
                    "Aidil Arifin Nizar",
                    "Addin Amanatulloh Suparjo",
                    "Yunolva Anis Ramaziyah"
                ],
                "hari": "SELASA",
                "jam": "18:30 - 21:30"
            },
            {
                "ruang": None,
                "matkul": "STD",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Harvian Khusnan Hafidz",
                    "Moh Naufal Mizan Saputro",
                    "Rayhan Suryatama Raharyawhedi",
                    "Bagus Hariyadi",
                    "Khalilullah Al Faath",
                    "Adinda Arwa Salsabil"
                ],
                "hari": "SABTU",
                "jam": "09:30 - 12:30"
            },
            {
                "ruang": None,
                "matkul": "ALPRO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Zharfan Dawud Harwiraputera",
                    "Jaatsiyah Maulidina Astrianto",
                    "Muhamad Raihan Ramadhan",
                    "Prins Naval Nuzeren",
                    "Nitamayega",
                    "Glorious Satria Dhamang Aji"
                ],
                "hari": "SABTU",
                "jam": "09:30 - 12:30"
            },
            {
                "ruang": None,
                "matkul": "PBO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Muhammad Haykal Kamil",
                    "Reva Doni Aprilio"
                ],
                "hari": "SABTU",
                "jam": "14:30 - 17:30"
            },
            {
                "ruang": None,
                "matkul": "WEBPRO",
                "kelas": None,
                "dosen": None,
                "asprak": [
                    "Deni Panji Dirgantara",
                    "Maulana Akbar Ramadhan",
                    "Ananta Noviandanu"
                ],
                "hari": "SABTU",
                "jam": "06:30 - 09:30"
            }
        ]
    }
