import streamlit as st
import requests
import pandas as pd  # Don't forget this import!

st.title("➕ Add Student")

# Form to add student
student_id = st.text_input("Student ID")
name = st.text_input("Student Name")
department = st.text_input("Department")

if st.button("Add Student"):
    if student_id and name and department:
        data = {
            "student_id": student_id,
            "name": name,
            "department": department
        }
        try:
            res = requests.post("http://127.0.0.1:8000/api/students/", json=data)
            if res.status_code == 201:
                st.success("Student Added Successfully ✅")
            else:
                st.error(res.text)
        except Exception as e:
            st.error("Backend not reachable. Is Django running?")
    else:
        st.warning("Please fill all fields")

# Always show student list below the form
st.subheader("📋 Student List")

try:
    res = requests.get("http://127.0.0.1:8000/api/students/")
    if res.status_code == 200:
        students = res.json()
        if len(students) == 0:
            st.info("No students found.")
        else:
            df = pd.DataFrame(students)
            st.dataframe(df, use_container_width=True)
    else:
        st.error("Failed to fetch students from backend.")
except Exception as e:
    st.error("Backend not reachable. Is Django running?")
