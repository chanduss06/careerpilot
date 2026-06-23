from src.memory.user_memory import (
    load_memory,
    save_memory
)


def save_skills(skills: list):

    memory = load_memory()

    existing_skills = memory.get(
        "skills",
        []
    )

    combined_skills = list(
        set(
            existing_skills + skills
        )
    )

    memory["skills"] = combined_skills

    save_memory(memory)

    return memory


def get_skills():

    memory = load_memory()

    return memory.get(
        "skills",
        []
    )