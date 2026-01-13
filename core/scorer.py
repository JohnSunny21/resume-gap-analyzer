def calculate_match_score(gap_analysis: dict) -> dict:
    """  
    
    Calculates an explainable match score based on gap analysis.
    
    """

    total_required = 0
    total_matched = 0

    for category in gap_analysis["matched"]:
        matched_count = len(gap_analysis["matched"].get(category,[]))
        missing_count = len(gap_analysis["missing"].get(category, []))


        total_matched += matched_count
        total_required += matched_count + missing_count


    if total_required == 0:
        score = 0.0
    else:
        score = round((total_matched / total_required) * 100, 2)


    return {
        "score": score,
        "total_required_skills": total_required,
        "matched_required_skills": total_matched,
        "missing_required_skills": total_required - total_matched,
        "summary":f"Matched {total_matched} out of {total_required} required skills"
    }