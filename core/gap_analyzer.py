def analyze_skill_gap(resume_skills: dict, jd_skills: dict) -> dict:
    """  
    Compares resume skills with job descriptionn skills.

    Retuns:
    {
        "matched": {},
        "missing": {},
        "extra"  : {}
    }
    """

    result = {
        "matched": {},
        "missing": {},
        "extra": {}
    }

    for category in jd_skills:
        resume_set = set(resume_skills.get(category, []))
        jd_set = set(jd_skills.get(category, []))

        matched = resume_set & jd_set
        missing = jd_set - resume_set
        extra = resume_set - jd_set


        result["matched"][category] = list(matched)
        result["missing"][category] = list(missing)
        result["extra"][category] = list(extra)


    return result