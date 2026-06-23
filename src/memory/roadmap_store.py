from src.memory.user_memory import (
    load_memory,
    save_memory
)


def save_completed_topic(
    topic: str
):

    memory = load_memory()

    if "roadmap_progress" not in memory:
        memory["roadmap_progress"] = []

    if topic not in memory["roadmap_progress"]:
        memory["roadmap_progress"].append(
            topic
        )

    save_memory(memory)

    return memory


def get_roadmap_progress():

    memory = load_memory()

    return memory.get(
        "roadmap_progress",
        []
    )