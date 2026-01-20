import streamlit as st
import requests

st.title("📝 Mark Attendance")

# ✅ Fetch students from backend
try:
    students = requests.get("http://127.0.0.1:8000/api/students/").json()
    if len(students) == 0:
        st.warning("No students found. Add students first!")
        st.stop()  # Stop page if no students
except Exception as e:
    st.error("Backend not reachable. Is Django running?")
    st.stop()

# Create dictionary for dropdown
student_dict = {f"{s['name']} (ID {s['student_id']})": s['id'] for s in students}

# Dropdown to select student
selected = st.selectbox("Select Student", student_dict.keys())
student_id = student_dict[selected]

# Attendance date and status
date = st.date_input("Date")
status = st.selectbox("Status", ["Present", "Absent"])

# Submit attendance
if st.button("Submit Attendance"):
    data = {
        "student_id": student_id,
        "date": str(date),
        "status": status
    }

    try:
        res = requests.post("http://127.0.0.1:8000/api/attendance/", json=data)
        if res.status_code == 201:
            st.success("Attendance Marked ✅")
        else:
            st.error(res.text)
    except Exception as e:
        st.error("Backend not reachable. Is Django running?")
