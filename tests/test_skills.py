from src.memory.skills_store import (
    save_skills,
    get_skills
)

save_skills(
    [
        "Python",
        "SQL",
        "Git"
    ]
)

print(get_skills())