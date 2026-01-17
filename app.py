import streamlit as st
from resume_parser import extract_text, extract_skills
from skill_gap import analyze_gap
from job_recommendation import recommend_roles
from learning_path import generate_learning_path

st.title("🚀 Skill Gap Analysis System")

# Manual Skill Input
manual_skills = st.text_input(
    "Enter your skills manually (comma separated)",
    placeholder="Python, SQL, Excel"
)

# Resume Upload
resume = st.file_uploader("Upload Resume (PDF)", type="pdf")

job_role = st.selectbox(
    "Select Target Job Role",
    ["Data Analyst", "ML Engineer", "Java Developer", "Frontend Developer"]
)

if st.button("Analyze Skills"):

    all_skills = []

    # Skills from resume
    if resume:
        text = extract_text(resume)
        resume_skills = extract_skills(text)
        all_skills.extend(resume_skills)

    # Skills from manual input
    if manual_skills:
        typed_skills = [s.strip().title() for s in manual_skills.split(",")]
        all_skills.extend(typed_skills)

    # Remove duplicates
    all_skills = list(set(all_skills))

    if not all_skills:
        st.error("Please upload a resume or enter skills manually.")
    else:
        st.write("### Combined Skills")
        st.write(all_skills)

        matched, missing, score = analyze_gap(all_skills, job_role)

        st.write("### Skill Match Score:", score, "%")
        st.write("Matched Skills:", matched)
        st.write("Missing Skills:", missing)

        st.write("### Learning Path")
        st.table(generate_learning_path(missing))

        st.write("### Recommended Job Roles")
        st.table(
            recommend_roles(all_skills)[["job_role", "match_score"]]
        )
