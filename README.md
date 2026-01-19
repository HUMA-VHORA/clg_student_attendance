# College Student Attendance System

A **Django-based Student Attendance Management System** using **PostgreSQL** and **REST APIs**.  
This project allows teachers to **add students, mark attendance, and view reports** (date-wise & student-wise) via **Postman** or a frontend.

## ✅ Features

- Add Students (ID, Name, Department)  
- Mark Attendance (Present / Absent)  
- View Attendance Reports:  
  - All records  
  - Date-wise  
  - Student-wise  
- PostgreSQL database integration  
- REST API support (tested with Postman)  
- Primary Key & Foreign Key relationship between Student and Attendance tables

---

## 🛠 Technology Stack

- Python 3.13  
- Django 6.x  
- PostgreSQL  
- Postman (for API testing)  
- VS Code (recommended)

---

## 📁 Project Structure

clg_attendance/
│
├── attendance/
│   ├── migrations/
│   ├── __init**.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── students/
│   ├── migrations/
│   ├──__init**.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── clg_attendance/
│   ├──__pycache**/
│   ├──__init**.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md

Create a virtual environment & activate
python -m venv myenv

Configure PostgreSQL

Create database:

CREATE DATABASE clg_attendance_db;

Run Migrations
python manage.py makemigrations
python manage.py migrate

Run Server
python manage.py runserver

Server will start at:

<http://127.0.0.1:8000/>

🔹 Example JSON for Postman

GET-<http://127.0.0.1:8000/api/attendance/>
[
    {
        "id": 1,
        "date": "2026-01-01",
        "status": "Present",
        "student_id": 1,
        "name": "Student 1"
    },
    {
        "id": 2,
        "date": "2026-01-01",
        "status": "Present",
        "student_id": 2,
        "name": "Student 2"
    }
]

📈 Reports

Date-wise: /api/attendance/by-date/2026-01-17/

Student-wise: /api/attendance/by-student/1/

✅ Notes

Make sure PostgreSQL server is running before starting Django server.

Avoid pushing myenv/ and sensitive credentials to GitHub.

Use Postman to test APIs before creating frontend.
