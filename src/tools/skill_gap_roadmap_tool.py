def generate_skill_gap_roadmap(
    missing_skills: list
) -> dict:

    roadmap = []

    for i, skill in enumerate(missing_skills, start=1):

        roadmap.append(
            f"Week {i}: Learn {skill}"
        )

    return {
        "roadmap": roadmap
    }