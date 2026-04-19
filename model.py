from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
SKILLS_DB = [
    "python", "java", "c", "c++",
    "machine learning", "deep learning", "nlp",
    "data analysis", "data science",
    "sql", "mysql",
    "tensorflow", "pytorch", "scikit-learn",
    "pandas", "numpy",
    "flask", "streamlit",
    "aws", "azure", "gcp",
    "computer vision" , "power bi", "tableau", "excel" 
]
def calculate_match(resume_text, job_desc):
    
    documents = [resume_text, job_desc]

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    score = round(float(similarity[0][0]) * 100, 2)
    
    return score


import re

def extract_skills(text):
    text = text.lower()
    
    found_skills = []
    
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)
    
    return set(found_skills)
def get_missing_skills(resume_text, job_desc):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    missing = job_skills - resume_skills
    return list(missing)