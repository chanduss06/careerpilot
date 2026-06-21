 from google.adk.agents import Agent

from src.tools.study_schedule_tool import (
    create_study_schedule
)

from src.tools.reminder_tool import (
    create_reminder
)

scheduler_agent = Agent(
    name="scheduler_agent",
    model="gemini-2.5-flash",

    description="Study scheduler",

    instruction="""
    You help users plan learning.

    Use create_study_schedule when:

    - study plan
    - study schedule
    - learning schedule

    Use create_reminder when:

    - reminder
    - remember
    - schedule task
    """,

    tools=[
        create_study_schedule,
        create_reminder
    ]
)