def create_reminder(
    task: str,
    time: str
) -> dict:

    return {
        "task": task,
        "time": time,
        "message":
            f"Reminder set for {task} at {time}"
    }