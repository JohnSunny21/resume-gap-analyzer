def generate_explanation(gap_analysis: dict, score_info: dict) -> dict:
    """   
    Generates human-readable explanations and recommendations
    """

    summary = (
        f"Your resume matches {score_info['matched_required_skills']} "
        f"out of {score_info['total_required_skills']} required skills "
        f"({score_info['score']}%)."
    )


    strengths = []

    for category,skills in gap_analysis["matched"].items():
        for skill in skills:
            strengths.append(f"{skill} ({category})")

    for category,skills in gap_analysis["extra"].items():
        for skill in skills:
            strengths.append(f"{skill} ({category}, bonus)")

    gaps = []

    for category, skills in gap_analysis["missing"].items():
        for skill in skills:
            gaps.append(f"{skill} ({category})")


    recommendations = []

    if gaps:
        recommendations.append(
            "Consider learning or gaining experience in the missing skills listed above."
        )

    recommendations.append(
        "Update your resume to clearly highlight matched skills using concrete examples."
    )

    if score_info["score"] < 70:
        recommendations.append(
            "Focus on required skills first to significantly improve your match score."
        )


    return {
        "overall_summary": summary,
        "strengths": strengths,
        "gaps": gaps,
        "recommendations": recommendations
    }
