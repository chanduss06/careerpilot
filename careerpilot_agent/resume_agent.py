from google.adk.agents import Agent

from src.tools.resume_analyzer_tool import analyze_resume
from src.tools.job_match_tool import analyze_job_match
from src.tools.skill_gap_roadmap_tool import generate_skill_gap_roadmap
from src.tools.job_recommendation_tool import recommend_jobs
from src.tools.progress_tracker_tool import track_progress

from src.tools.report_export_tool import (
    export_resume_report
)

resume_agent = Agent(
    name="resume_agent",
    model="gemini-2.5-flash",

    description="Resume specialist",

    instruction="""
    You are a resume review expert.

    Use analyze_resume when
    the user wants resume review.

    Use analyze_job_match when
    the user provides both:

    - Resume
    - Job Description

    Return skill gap analysis.

    Use generate_skill_gap_roadmap when
    the user asks:

    - How to learn missing skills
    - Roadmap for missing skills
    - Learning plan

    Generate a week-by-week roadmap.

    Use recommend_jobs when
    the user asks:

    - Suitable jobs
    - Best roles for me
    - What jobs can I get
    - Career recommendations

    Recommend job roles based on skills.

    Use track_progress when
    the user provides:

    - Completed skills
    - Target skills

    Calculate progress percentage
    and remaining skills.
    """,

    tools=[
        analyze_resume,
        analyze_job_match,
        generate_skill_gap_roadmap,
        recommend_jobs,
        track_progress,
        export_resume_report
    ]
)