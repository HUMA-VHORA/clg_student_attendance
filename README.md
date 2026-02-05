# 🎓 College Student Attendance System

A full-stack College Student Attendance Management System built using modern backend security practices.

🚀 Tech Stack

✅ Django + Django REST Framework (Backend APIs)
✅ PostgreSQL
✅ Redis Cache (Performance Optimization)
✅ JWT Authentication (SimpleJWT)
✅ Role-Based Access Control (RBAC)
✅ Custom Authorization Decorators
✅ Streamlit (Frontend UI)
✅ Postman (API Testing)
✅ Git & GitHub

🔐 Authentication & Authorization (RBAC)

This project implements secure authentication and authorization using JWT + Role-Based Access Control.

🔑 Authentication

JWT-based login using SimpleJWT

Access & Refresh tokens

Tokens include user role (Teacher / Student)

🛡 Authorization (RBAC)

Users are assigned roles using Django Groups

A custom decorator (@role_required) enforces access control

API access is granted based on user role

🎯 Role Access Matrix
Role Permissions
Teacher Add students, mark attendance, view all attendance
Student View own attendance & profile only

🔧 Custom Decorator Example
@role_required(['Teacher'])
def post(self, request):
    ...

✔ Centralized authorization
✔ Clean and reusable logic
✔ Production-ready RBAC

✅ Features
🔧 Backend (Django REST API)

🔐 JWT Authentication (Login & Token Refresh)
🛡 Role-Based Access Control (RBAC)
⚡ Redis Caching for faster API responses

👨‍🏫 Teacher Features

Add Students (Student ID, Name, Department)

Mark Attendance (Present / Absent)

View Attendance Reports:

All records

Date-wise

Student-wise

👨‍🎓 Student Features

View own student profile

View own attendance records only

🗄 PostgreSQL database integration
🔗 Proper Primary Key & Foreign Key relationship:

Student table

Attendance table

🧪 APIs tested using Postman

🎨 Frontend (Streamlit)

🏠 Home Dashboard
➕ Add Student Form
📝 Mark Attendance Page (Student dropdown)
📊 View Attendance in Table Format

The frontend communicates with secured Django REST APIs using JWT tokens.

🛠 Technology Stack

Python

Django

Django REST Framework

PostgreSQL

Redis

JWT (SimpleJWT)

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
├── users/                       # Authentication & JWT
│   ├── serializers.py
│   ├── views.py
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
│   ├── decorators.py            # RBAC decorator
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

▶️ Run Django Backend

Activate virtual environment and run:

python manage.py runserver

Backend runs at:

<http://127.0.0.1:8000/>

🔗 API Endpoints
🔐 Auth (JWT)

Login

POST /api/token/

Refresh Token

POST /api/token/refresh/

👨‍🎓 Students API
GET  /api/students/      (Teacher only)
POST /api/students/     (Teacher only)
GET  /api/students/{id} (Student – own data)

Example:

<http://127.0.0.1:8000/api/students/>

📝 Attendance API
GET  /api/attendance/              (Teacher)
POST /api/attendance/              (Teacher)
GET  /api/attendance/date/{date}   (Teacher)
GET  /api/attendance/student/{id}  (Student – own records)

Example:

<http://127.0.0.1:8000/api/attendance/>

▶️ Run Streamlit Frontend

Open a new terminal:

cd streamlit_frontend
streamlit run Home.py

⚠ Make sure Django backend is already running.

🧪 API Testing (Postman Example)

GET Attendance

GET <http://127.0.0.1:8000/api/attendance/>
Authorization: Bearer <access_token>

Response
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
    "status": "Absent",
    "student_id": 2,
    "name": "Student 2"
  }
]
