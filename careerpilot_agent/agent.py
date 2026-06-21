from google.adk.agents import Agent

from careerpilot_agent.dsa_agent import dsa_agent
from careerpilot_agent.resume_agent import resume_agent
from careerpilot_agent.interview_agent import interview_agent

root_agent = Agent(
    name="careerpilot_orchestrator",
    model="gemini-2.5-flash",
    description="Main orchestrator for CareerPilot AI",
    instruction="""
    You are CareerPilot AI.

    Route requests intelligently:

    - Resume related → resume_agent
    - DSA related → dsa_agent
    - Interview related → interview_agent

    Do not answer specialized questions yourself when a specialist exists.
    """,

    sub_agents=[
        resume_agent,
        dsa_agent,
        interview_agent
    ]
)