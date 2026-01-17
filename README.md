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
├── clg_attendance/ # Django project settings
│ ├── settings.py # Database and apps configuration
│ ├── urls.py # Project-level URL routes
│ └── wsgi.py
│
├── students/ # Student app
│ ├── models.py # Student model
│ ├── views.py # Student API views
│ ├── urls.py # Student API URLs
│ └── admin.py
│
├── attendance/ # Attendance app
│ ├── models.py # Attendance model
│ ├── views.py # Attendance API views
│ ├── urls.py # Attendance API URLs
│ └── admin.py
│
├── manage.py
└── requirements.txt

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
Add Student (POST)
{
  "student_id": "CSE001",
  "name": "Rahul Sharma",
  "department": "CSE"
}

Mark Attendance (POST)
{
  "student_id": 1,
  "date": "2026-01-17",
  "status": "Present"
}

📈 Reports

Date-wise: /api/attendance/by-date/2026-01-17/

Student-wise: /api/attendance/by-student/1/

✅ Notes

Make sure PostgreSQL server is running before starting Django server.

Avoid pushing myenv/ and sensitive credentials to GitHub.

Use Postman to test APIs before creating frontend.
