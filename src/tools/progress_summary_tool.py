def generate_progress_summary(
    completed_tasks: int,
    total_tasks: int
) -> dict:

    progress = int(
        (completed_tasks / total_tasks) * 100
    )

    return {
        "completed_tasks": completed_tasks,
        "total_tasks": total_tasks,
        "progress_percent": progress,
        "summary":
            f"You completed {completed_tasks} out of {total_tasks} tasks."
    }