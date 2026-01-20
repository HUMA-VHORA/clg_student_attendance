import streamlit as st

st.set_page_config(page_title="College Attendance System", layout="wide")

st.title("🎓 College Attendance System")
st.subheader("Streamlit Frontend Connected to Django Backend")

st.success("Backend should be running at http://127.0.0.1:8000")

st.write("Use the sidebar to:")
st.write("✔ Add Students")
st.write("✔ Mark Attendance")
st.write("✔ View Attendance Reports")
