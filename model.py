import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Skill database
SKILLS_DB = [
    "python", "java", "c", "c++",
    "machine learning", "deep learning", "nlp",
    "data analysis", "data science",
    "sql", "mysql",
    "tensorflow", "pytorch", "scikit-learn",
    "pandas", "numpy",
    "flask", "streamlit",
    "aws", "azure", "gcp",
    "computer vision", "power bi", "tableau", "excel"
]

# 🔹 Extract only valid skills
def extract_skills(text):
    text = text.lower()
    found_skills = set()

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)

    # Handle synonyms
    if "ml" in text:
        found_skills.add("machine learning")
    if "dl" in text:
        found_skills.add("deep learning")
    if "sklearn" in text:
        found_skills.add("scikit-learn")
    if "data analytics" in text:
        found_skills.add("data analysis")

    return found_skills


# 🔹 Hybrid scoring (TF-IDF + Skill Match)
def calculate_match(resume_text, job_desc):

    # TF-IDF similarity
    documents = [resume_text, job_desc]
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(documents)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    tfidf_score = float(similarity[0][0]) * 100

    # Skill-based score
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    if len(job_skills) > 0:
        skill_score = (len(resume_skills & job_skills) / len(job_skills)) * 100
    else:
        skill_score = 0

    # Final score (weighted)
    final_score = (0.4 * tfidf_score) + (0.6 * skill_score)

    return round(final_score, 2)


# 🔹 Missing skills
def get_missing_skills(resume_text, job_desc):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    missing = job_skills - resume_skills
    return list(missing)[:10]


# 🔹 Matched skills (NEW 🔥)
def get_matched_skills(resume_text, job_desc):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    matched = resume_skills & job_skills
    return list(matched)