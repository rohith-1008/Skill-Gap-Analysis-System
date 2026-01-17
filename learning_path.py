import pandas as pd

def generate_learning_path(missing_skills):
    courses = pd.read_csv("data/courses.csv")
    return courses[courses.skill.isin(missing_skills)]
