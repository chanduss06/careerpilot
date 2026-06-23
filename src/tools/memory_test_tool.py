from src.memory.user_memory import (
    update_memory,
    load_memory
)


def test_memory(skill: str):

    update_memory(
        "latest_skill",
        skill
    )

    return load_memory()