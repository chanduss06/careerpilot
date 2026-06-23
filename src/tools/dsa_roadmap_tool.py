from src.memory.skills_store import (
    get_skills
)

from src.memory.roadmap_store import (
    get_roadmap_progress
)


def generate_dsa_roadmap(level: str) -> dict:

    level = level.lower()

    skills = get_skills()

    completed_topics = get_roadmap_progress()

    if level == "beginner":

        roadmap = [
            "Arrays",
            "Strings",
            "Linked Lists",
            "Stacks",
            "Queues",
            "Trees",
            "Graphs"
        ]

    else:

        roadmap = [
            "Dynamic Programming",
            "Graphs",
            "Tries",
            "Segment Trees",
            "Advanced DP",
            "Competitive Programming"
        ]

    remaining_topics = [
        topic
        for topic in roadmap
        if topic not in completed_topics
    ]

    return {

        "detected_skills": skills,

        "completed_topics": completed_topics,

        "remaining_topics": remaining_topics,

        "next_topic": (
            remaining_topics[0]
            if remaining_topics
            else "Roadmap Completed"
        )
    }