def track_dsa_progress(
    solved_problems: int,
    target_problems: int
) -> dict:

    progress = int(
        (solved_problems / target_problems) * 100
    )

    remaining = (
        target_problems - solved_problems
    )

    return {
        "progress_percent": progress,
        "solved_problems": solved_problems,
        "target_problems": target_problems,
        "remaining_problems": remaining
    }