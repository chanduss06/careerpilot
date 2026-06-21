from google.adk.agents import Agent

from src.tools.dsa_roadmap_tool import generate_dsa_roadmap
from src.tools.problem_recommender_tool import recommend_problems
from src.tools.dsa_progress_tool import track_dsa_progress

dsa_agent = Agent(
    name="dsa_agent",
    model="gemini-2.5-flash",

    description="DSA learning specialist",

    instruction="""
    You are a DSA mentor.

    Use generate_dsa_roadmap when
    the user asks:

    - DSA roadmap
    - Learning path
    - Study plan

    Generate a roadmap based on level.

    Use recommend_problems when
    the user asks:

    - Recommend problems
    - Practice questions
    - LeetCode questions
    - Coding problems

    Recommend problems based on topic.

    Use track_dsa_progress when
    the user provides:

    - Solved problems
    - Target problems

    Calculate DSA progress.
    """,

    tools=[
        generate_dsa_roadmap,
        recommend_problems,
        track_dsa_progress
    ]
)