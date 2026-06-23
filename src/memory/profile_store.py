from src.memory.user_memory import (
    load_memory,
    save_memory
)


def save_profile(
    name: str,
    target_role: str
):

    memory = load_memory()

    memory["user_profile"] = {
        "name": name,
        "target_role": target_role
    }

    save_memory(memory)

    return memory


def get_profile():

    memory = load_memory()

    return memory.get(
        "user_profile",
        {}
    )