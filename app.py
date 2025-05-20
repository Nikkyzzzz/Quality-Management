import streamlit as st
from datetime import datetime, timedelta

# ---- TITLE ----
st.title("📚 Exam Preparation Checklist")
st.subheader("From Task 1 to 101 - Let's go unit by unit!")

# ---- TIME MANAGEMENT ----
exam_time = datetime.now().replace(hour=9, minute=30, second=0, microsecond=0) + timedelta(days=1)
now = datetime.now()
time_left = exam_time - now

hours_left = time_left.total_seconds() / 3600
st.info(f"⏰ Time left until exam: **{int(hours_left)} hours and {int((hours_left%1)*60)} minutes**")

# ---- DIVIDE TIME PER UNIT ----
unit_names = ['Unit 1 (1–16)', 'Unit 2 (17–40)', 'Unit 3 (41–65)', 'Unit 4 (66–85)', 'Unit 5 (86–101)']
unit_lengths = [16, 24, 25, 20, 16]
total_tasks = sum(unit_lengths)
unit_times = [(length / total_tasks) * hours_left for length in unit_lengths]

st.markdown("### 🕒 Suggested Time Allocation per Unit:")
for unit, time in zip(unit_names, unit_times):
    st.write(f"- **{unit}**: {int(time)} hr {int((time % 1) * 60)} min")

# ---- CHECKLIST FUNCTION ----
def checklist(unit_name, start, end):
    st.markdown(f"### ✅ {unit_name}")
    for i in range(start, end + 1):
        st.checkbox(f"Task {i}", key=f"{unit_name}_task_{i}")

# ---- CHECKLISTS BY UNIT ----
checklist("Unit 1 (1–16)", 1, 16)
checklist("Unit 2 (17–40)", 17, 40)
checklist("Unit 3 (41–65)", 41, 65)
checklist("Unit 4 (66–85)", 66, 85)
checklist("Unit 5 (86–101)", 86, 101)

st.success("✨ All the best for your exam! You've got this!")
