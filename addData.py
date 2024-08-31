import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://presensikaryawan-bcb5b-default-rtdb.firebaseio.com/"
})

ref = db.reference('Employees')

data = {
    "0001":
        {
            "name": "Muhammad Rafiansyah",
            "position": "Programmer",
            "starting_year" : 2024,
            "total_attendance": 36,
            "last_attendance_time": "2024-07-10 18:09:39"
        },
    
    "0002":
        {
            "name": "Harsya Helmansyah",
            "position": "Marketing",
            "starting_year" : 2023,
            "total_attendance": 304,
            "last_attendance_time": "2024-02-11 09:54:21"
        },
    
    "0003":
        {
            "name": "Rozaan Alexander",
            "position": "Assistant Project Manager",
            "starting_year" : 2021,
            "total_attendance": 324,
            "last_attendance_time": "2024-01-21 09:01:42"
        },

    "0004":
        {
            "name": "Ayatullah Rachman",
            "position": "Developer Game",
            "starting_year" : 2024,
            "total_attendance": 30,
            "last_attendance_time": "2024-01-10 09:01:42"
        },
    
    "0005":
        {
            "name": "Geren Haekal",
            "position": "Presiden Direktur",
            "starting_year" : 2024,
            "total_attendance": 40,
            "last_attendance_time": "2024-03-13 09:01:42"
        },

    "0006":
        {
            "name": "Margareta Lola",
            "position": "Programmer",
            "starting_year" : 2024,
            "total_attendance": 25,
            "last_attendance_time": "2024-04-20 09:01:42"
        },
    
    "0007":
        {
            "name": "Iqbal Andi Pradana",
            "position": "Arduino",
            "starting_year" : 2024,
            "total_attendance": 45,
            "last_attendance_time": "2024-02-11 09:01:42"
        },
    
    "0008":
        {
            "name": "Hasan Albana",
            "position": "Frontend",
            "starting_year" : 2024,
            "total_attendance": 25,
            "last_attendance_time": "2024-05-21 09:01:42"
        },
    
    "0009":
        {
            "name": "Anisya Anggreini",
            "position": "Akuntansi",
            "starting_year" : 2024,
            "total_attendance": 25,
            "last_attendance_time": "2024-05-21 09:01:42"
        }
    
    
    
    
    
}

for key, value in data.items():
    ref.child(key).set(value)
