def track_goal(
    goal: str,
    current_status: str
) -> dict:

    return {
        "goal": goal,
        "status": current_status,
        "next_step":
            f"Continue working towards: {goal}"
    }