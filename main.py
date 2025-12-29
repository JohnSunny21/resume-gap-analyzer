from core.text_cleaner import clean_text
from core.skill_extractor import extract_skills

sample_text = """
Worked with Python, Flask & AWS.
Experience in REST APIs and Docker!!
"""

resume_text = """
Backend developer with experience in Python, Spring Boot,
REST APIs, Docker, and AWS.
"""

print(clean_text(sample_text))

cleaned = clean_text(resume_text)
skills = extract_skills(cleaned)

print(skills)