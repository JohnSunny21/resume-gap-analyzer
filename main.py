from core.text_cleaner import clean_text
from core.skill_extractor import extract_skills
from core.gap_analyzer import analyze_skill_gap
from core.scorer import calculate_match_score
from core.explainer import generate_explanation



sample_text = """
Worked with Python, Flask & AWS.
Experience in REST APIs and Docker!!
"""

resume_text = """
Backend developer with experience in Python, Spring Boot,
REST APIs, Docker, and AWS.
"""



# print(clean_text(sample_text))

# cleaned = clean_text(resume_text)
# skills = extract_skills(cleaned)

# print(skills)



resume_text = """
Backend developer with experience in Python, Spring Boot,
REST APIs, Docker, and AWS.
"""

jd_text = """
Looking for a backend engineer skilled in Python, Django,
REST API, Docker, Kubernetes, and AWS.
"""

resume_skills = extract_skills(clean_text(resume_text))
jd_skills = extract_skills(clean_text(jd_text))

gap = analyze_skill_gap(resume_skills, jd_skills)

score = calculate_match_score(gap)
explanation = generate_explanation(gap, score)

print(explanation)