import streamlit as st
from model import (
    calculate_match,
    get_missing_skills,
    extract_skills,
    get_matched_skills
)
from utils import extract_text_from_pdf

st.title("📄 AI Resume Screener")

# Upload Resume
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

# Job Description
job_desc = st.text_area("Paste Job Description")

if uploaded_file is not None and job_desc:

    # Extract text
    resume_text = extract_text_from_pdf(uploaded_file)

    # Scores
    score = calculate_match(resume_text, job_desc)
    missing_skills = get_missing_skills(resume_text, job_desc)
    matched_skills = get_matched_skills(resume_text, job_desc)

    # 🎯 Match Score
    st.subheader(f"🎯 Match Score: {score}%")

    if score > 75:
        st.success("Great match! 👍")
    elif score > 50:
        st.warning("Decent match, can improve ⚡")
    else:
        st.error("Low match, needs improvement ❌")

    # ✅ Matched Skills
    st.subheader("✅ Matched Skills")
    if matched_skills:
        st.write(", ".join(matched_skills))
    else:
        st.write("No strong matches found")

    # ❌ Missing Skills
    st.subheader("❌ Missing Skills")
    if missing_skills:
        st.write(", ".join(missing_skills))
    else:
        st.write("No major skills missing")

    # 💡 Suggestions
    st.subheader("💡 How to Improve")

    if len(missing_skills) == 0 and score > 75:
        st.success("Your resume is well aligned with this role 🎉")
    elif missing_skills:
        st.write("👉 Try adding these skills:", ", ".join(missing_skills))

    else:
        st.write("⚠️ Improve project descriptions and keyword usage")

    # 🔍 Debug (optional – remove later)
    with st.expander("🔍 Debug Info"):
        st.write("Job Skills:", extract_skills(job_desc))
        st.write("Resume Skills:", extract_skills(resume_text))