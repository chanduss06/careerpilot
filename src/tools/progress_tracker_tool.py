def track_progress(
    completed_skills: str,
    target_skills: str
) -> dict:

    completed = completed_skills.lower().split()
    target = target_skills.lower().split()

    progress = int(
        (len(completed) / len(target)) * 100
    )

    remaining = [
        skill
        for skill in target
        if skill not in completed
    ]

    return {
        "progress_percent": progress,
        "completed_skills": completed,
        "remaining_skills": remaining
    }