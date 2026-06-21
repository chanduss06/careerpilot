def analyze_job_match(
    resume_text: str,
    job_description: str
) -> dict:

    skills = [
        "python",
        "java",
        "sql",
        "aws",
        "docker",
        "git",
        "javascript",
        "react",
        "node"
    ]

    matched = []
    missing = []

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    for skill in skills:

        if (
            skill in job_description
            and skill in resume_text
        ):
            matched.append(skill.title())

        elif skill in job_description:
            missing.append(skill.title())

    total_required = len(matched) + len(missing)

    score = (
        int((len(matched) / total_required) * 100)
        if total_required > 0
        else 0
    )

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }