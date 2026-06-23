from google.adk.agents import Agent

from src.tools.progress_summary_tool import (
    generate_progress_summary
)

from src.tools.goal_tracker_tool import (
    track_goal
)

from src.tools.github_tools import (
    fetch_repo_stats,
    fetch_recent_commits
)

progress_agent = Agent(
    name="progress_agent",
    model="gemini-2.5-flash",

    description="Career progress tracker",

    instruction="""
    You help users track learning
    and career progress.

    Use generate_progress_summary when:

    - completed tasks
    - finished tasks
    - progress summary

    Use track_goal when:

    - career goals
    - learning goals
    - target goals
    """,

    tools=[
        generate_progress_summary,
        track_goal,
        fetch_repo_stats,
        fetch_recent_commits
    ]
)