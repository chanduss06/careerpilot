from src.mcp.calendar_mcp import (
    create_study_event
)

def schedule_study_session(
    title: str,
    date: str,
    duration_hours: int
):
    return create_study_event(
        title,
        date,
        duration_hours
    )