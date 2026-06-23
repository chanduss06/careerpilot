import json
from pathlib import Path

MEMORY_FILE = Path(__file__).parent / "memory.json"


def load_memory():
    """
    Load memory from JSON file.
    """

    if not MEMORY_FILE.exists():
        return {}

    with open(MEMORY_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


def save_memory(data: dict):
    """
    Save memory to JSON file.
    """

    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def update_memory(key: str, value):
    """
    Update a specific memory field.
    """

    memory = load_memory()

    memory[key] = value

    save_memory(memory)

    return {
        "message": f"{key} updated successfully"
    }