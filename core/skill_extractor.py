from utils.skill_dictionary import SKILL_DICTIONARY

def extract_skills(cleaned_text: str) -> dict:
    """  
    Extracts skills from cleaned text using a predefined skill dictionary.

    Retuns:
    {
        category: {skills}
        
    }
    """

    extracted_skills = {category: [] for category in SKILL_DICTIONARY}

    for category, skills in SKILL_DICTIONARY.items():
        for skill in skills:
            if skill in cleaned_text:
                extracted_skills[category].append(skill)


    return extracted_skills