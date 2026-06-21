def recommend_jobs(skills: str) -> dict:

    skills = skills.lower()

    jobs = []

    if "python" in skills:
        jobs.append("Python Developer")

    if "sql" in skills:
        jobs.append("Data Analyst")

    if "flask" in skills:
        jobs.append("Backend Developer")

    if "javascript" in skills:
        jobs.append("Full Stack Developer")

    if "java" in skills:
        jobs.append("Software Engineer")

    return {
        "recommended_jobs": jobs
    }