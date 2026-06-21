def generate_dsa_roadmap(level: str) -> dict:

    level = level.lower()

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

    return {
        "roadmap": roadmap
    }