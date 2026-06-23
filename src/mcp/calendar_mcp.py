import json
from pathlib import Path

CALENDAR_FILE = Path("calendar/events.json")

def create_study_event(
    title: str,
    date: str,
    duration_hours: int
) -> dict:

    event = {
        "title": title,
        "date": date,
        "duration_hours": duration_hours
    }

    with open(
        CALENDAR_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        events = json.load(file)

    events.append(event)

    with open(
        CALENDAR_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            events,
            file,
            indent=4
        )

    return {
        "status": "success",
        "event": event,
        "message": f"Event '{title}' scheduled"
    }