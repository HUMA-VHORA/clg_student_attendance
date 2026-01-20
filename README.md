# 🎓 College Student Attendance System

A full-stack College Student Attendance Management System built using:

✅ Django + Django REST Framework (Backend APIs)

✅ PostgreSQL (Database)

✅ Streamlit (Frontend UI)

✅ Postman (API Testing)

This system allows teachers to add students, mark attendance, and view attendance reports via APIs or a simple web interface.

✅ Features
🔧 Backend (Django REST API)

Add Students (ID, Name, Department)

Mark Attendance (Present / Absent)

View Attendance Reports:

All Records

Date-wise

Student-wise

PostgreSQL database integration

REST APIs tested using Postman

Primary Key & Foreign Key relationship between Student and Attendance tables

🎨 Frontend (Streamlit)

Home Dashboard

Add Student Form

Mark Attendance Page

View Attendance in Table Format

🛠 Technology Stack

Python

Django

Django REST Framework

PostgreSQL / SQLite

Streamlit

Postman

Git & GitHub

📁 Project Structure
clg_student_attendance/
│
├── clg_attendance/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── students/                    # Students app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── attendance/                  # Attendance app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── streamlit_frontend/          # Streamlit frontend
│   ├── Home.py
│   └── pages/
│       ├── 1_Add_Student.py
│       ├── 2_Mark_Attendance.py
│       └── 3_View_Attendance.py
│
├── manage.py
└── README.md

Run Django Backend
python manage.py runserver

Backend runs at:

<http://127.0.0.1:8000/>

API Endpoints

Students API
<http://127.0.0.1:8000/api/students/>

Attendance API
<http://127.0.0.1:8000/api/attendance/>

Run Streamlit Frontend

Open new terminal:

cd streamlit_frontend
streamlit run Home.py

🧪 API Testing (Postman Example)
GET Attendance

GET <http://127.0.0.1:8000/api/attendance/>

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
