import streamlit as st
import requests
import pandas as pd

st.title("📊 View Attendance")

API_URL = "http://127.0.0.1:8000/api/attendance/"

# ✅ Option to view all or filter
option = st.radio("View By", ["All", "Date", "Student"])

try:
    if option == "All":
        # Fetch all attendance
        res = requests.get(API_URL)
        if res.status_code == 200:
            data = res.json()
            if len(data) == 0:
                st.warning("No attendance records found.")
            else:
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True)
        else:
            st.error("Failed to fetch attendance data from backend.")

    elif option == "Date":
        date = st.date_input("Select Date")
        if st.button("Show by Date"):
            res = requests.get(f"http://127.0.0.1:8000/api/attendance/by-date/{date}/")
            if res.status_code == 200:
                df = pd.DataFrame(res.json())
                if len(df) == 0:
                    st.info("No attendance for this date.")
                else:
                    st.dataframe(df, use_container_width=True)
            else:
                st.error(res.text)

    else:  # option == "Student"
        sid = st.text_input("Enter Student ID")
        if st.button("Show by Student"):
            res = requests.get(f"http://127.0.0.1:8000/api/attendance/by-student/{sid}/")
            if res.status_code == 200:
                df = pd.DataFrame(res.json())
                if len(df) == 0:
                    st.info("No attendance for this student.")
                else:
                    st.dataframe(df, use_container_width=True)
            else:
                st.error(res.text)

except Exception as e:
    st.error("Backend not reachable. Is Django running?")
