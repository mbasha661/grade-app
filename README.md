# Streamlit Student Grade Manager - Social Eagle Week 1 Day 4

The Day 2 terminal grade manager as a Streamlit web app: a form to add a
student (name + mark), a results table with name / mark / grade, and the
class average, highest and lowest shown as metrics.

## Setup and run

```bash
mkdir grade-app && cd grade-app
python -m venv venv
source venv/bin/activate          # Windows PowerShell: venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run grade_app.py        # not: python grade_app.py
```

The app opens at http://localhost:8501

## What went wrong before session_state

With a plain `students = []` at the top of the file, every "Add" click made
Streamlit rerun the whole script, so the list was recreated empty and the
previous student disappeared. Moving the list into `st.session_state` keeps it
alive across reruns - that is the difference between a Streamlit app and the
Day 2 terminal script.
