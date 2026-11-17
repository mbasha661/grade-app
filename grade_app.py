"""
Streamlit Student Grade Manager - Social Eagle Week 1 Day 4.

The Day 2 terminal grade manager, moved into the browser with Streamlit.
The one big lesson: Streamlit reruns this whole script on every interaction,
so the student list must live in st.session_state, not a plain list.

Run:
    streamlit run grade_app.py
"""

import streamlit as st


def get_grade(mark):
    """Same grading scale as Day 2. Boundaries inclusive: 90 is an A."""
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"


st.title("Student Grade Manager")

# session_state survives Streamlit's full-script reruns; a plain list would not.
if "students" not in st.session_state:
    st.session_state.students = []

with st.form("add_student"):
    name = st.text_input("Name")
    mark = st.number_input("Mark", min_value=0, max_value=100, step=1)
    submitted = st.form_submit_button("Add")
    if submitted:
        if not name.strip():
            st.error("Please enter a name.")
        else:
            st.session_state.students.append(
                {"Name": name.strip(), "Mark": int(mark), "Grade": get_grade(mark)}
            )
            st.success(f"Added {name.strip()} ({int(mark)} -> {get_grade(mark)})")

if st.session_state.students:
    students = st.session_state.students
    st.table(students)

    marks = [s["Mark"] for s in students]
    col1, col2, col3 = st.columns(3)
    col1.metric("Average", f"{sum(marks) / len(marks):.1f}")
    col2.metric("Highest", max(marks))
    col3.metric("Lowest", min(marks))
else:
    st.info("No students yet. Add the first one above.")
