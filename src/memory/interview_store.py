from src.memory.user_memory import (
    load_memory,
    save_memory
)


def save_interview_score(
    score: int
):

    memory = load_memory()

    if "interview_scores" not in memory:
        memory["interview_scores"] = []

    memory["interview_scores"].append(
        score
    )

    save_memory(memory)

    return memory


def get_interview_scores():

    memory = load_memory()

    return memory.get(
        "interview_scores",
        []
    )