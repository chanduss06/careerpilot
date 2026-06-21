def analyze_resume(resume_text: str) -> dict:
    """
    Simple resume analyzer.
    """

    score = 60

    skills = ["python", "java", "sql", "git", "docker", "aws"]

    strengths = []
    missing_skills = []

    for skill in skills:
        if skill in resume_text.lower():
            strengths.append(skill.title())
            score += 5
        else:
            missing_skills.append(skill.title())

    return {
        "ats_score": min(score, 100),

        "strengths": strengths,

        "missing_skills": missing_skills,

        "recommended_projects": [
            "Full Stack Application",
            "REST API Project"
        ],

        "recommended_certifications": [
            "Google Cloud Fundamentals",
            "AWS Cloud Practitioner"
        ]
    }