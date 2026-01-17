import spacy
import PyPDF2

nlp = spacy.load("en_core_web_sm")

SKILL_DB = [
    "python","java","sql","excel","machine learning","statistics",
    "power bi","git","react","deep learning"
]

def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def extract_skills(text):
    skills = []
    for skill in SKILL_DB:
        if skill in text:
            skills.append(skill.title())
    return list(set(skills))
