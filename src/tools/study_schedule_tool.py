def create_study_schedule(
    topic: str,
    days: int
) -> dict:

    schedule = []

    for day in range(1, days + 1):
        schedule.append(
            f"Day {day}: Study {topic}"
        )

    return {
        "topic": topic,
        "schedule": schedule
    }