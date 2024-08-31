import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': ""
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
        }
    
    
    
    
    
}

for key, value in data.items():
    ref.child(key).set(value)
