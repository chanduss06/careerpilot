from src.memory.user_memory import (
    update_memory,
    load_memory
)

update_memory(
    "latest_skill",
    "Python"
)

print(load_memory())