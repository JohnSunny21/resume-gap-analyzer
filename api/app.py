from fastapi import FastAPI
from pydantic import BaseModel


from core.text_cleaner import clean_text
from core.skill_extractor import extract_skills
from core.gap_analyzer import analyze_skill_gap
from core.scorer import calculate_match_score
from core.explainer import generate_explanation


app = FastAPI(
    title = "Resume Gap Analyzer API",
    description="Explainable AI_powered resume and job description gap analysis",
    version="1.0.0"
)


class AnalysisRequest(BaseModel):

    resume_text: str
    job_description_text: str



@app.post("/analyze")
def analyze_resume(request: AnalysisRequest):

    # Cleaning text
    resume_cleaned = clean_text(request.resume_text)
    jd_cleaned = clean_text(request.job_description_text)

    # Extract skills
    resume_skills = extract_skills(resume_cleaned)
    jd_skills = extract_skills(jd_cleaned)

    # Gap analysis
    gap = analyze_skill_gap(resume_skills, jd_skills)

    # Scoring
    score = calculate_match_score(gap)

    # Explanation

    explanation = generate_explanation(gap, score)

    return {
        "score": score,
        "gap_analysis": gap,
        "explanation": explanation
    }