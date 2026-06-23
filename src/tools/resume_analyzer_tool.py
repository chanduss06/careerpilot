from src.memory.skills_store import save_skills


def analyze_resume(resume_text: str) -> dict:
    """
    Simple resume analyzer.
    """

    score = 60

    skills = ["python", "java", "sql", "git", "docker", "aws"]

    DISPLAY_NAMES = {
        "python": "Python",
        "java": "Java",
        "sql": "SQL",
        "git": "Git",
        "docker": "Docker",
        "aws": "AWS"
    }

    strengths = []
    missing_skills = []

    for skill in skills:

        if skill in resume_text.lower():

            strengths.append(
                DISPLAY_NAMES[skill]
            )

            score += 5

        else:

            missing_skills.append(
                DISPLAY_NAMES[skill]
            )

    save_skills(strengths)

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