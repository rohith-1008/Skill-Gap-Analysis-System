import pandas as pd

def analyze_gap(user_skills, job_role):
    jobs = pd.read_csv("data/job_roles.csv")
    job_skills = jobs[jobs.job_role == job_role]["skills"].values[0]
    job_skills = set(job_skills.split(","))

    user_skills = set(user_skills)

    matched = user_skills & job_skills
    missing = job_skills - user_skills

    score = round((len(matched) / len(job_skills)) * 100, 2)

    return matched, missing, score
