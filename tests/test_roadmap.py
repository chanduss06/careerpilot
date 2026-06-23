from src.memory.roadmap_store import (
    save_completed_topic,
    get_roadmap_progress
)

save_completed_topic(
    "Arrays"
)

save_completed_topic(
    "Strings"
)

print(
    get_roadmap_progress()
)