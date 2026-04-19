import streamlit as st
from model import calculate_match, get_missing_skills
from utils import extract_text_from_pdf

st.title("📄 AI Resume Screener")

# Upload Resume
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

# Job Description
job_desc = st.text_area("Paste Job Description")

if uploaded_file is not None and job_desc:
    
    # Extract text
    resume_text = extract_text_from_pdf(uploaded_file)

    # Calculate score
    score = calculate_match(resume_text, job_desc)

    # Get missing skills
    missing_skills = get_missing_skills(resume_text, job_desc)

    # Show score
    st.subheader(f"Match Score: {score}%")

    if score > 70:
        st.success("Great match! 👍")
    elif score > 40:
        st.warning("Decent match, can improve ⚡")
    else:
        st.error("Low match, needs improvement ❌")

    # NEW FEATURE 👇
    st.subheader("🔍 Why not selected?")
    st.write("Missing Skills:", missing_skills)

    st.subheader("💡 How to Improve")
    if missing_skills:
        st.write("👉 Try adding these skills:", ", ".join(missing_skills))
    else:
        st.write("👉 Your resume matches well!")