from google.adk.agents import Agent

from src.tools.mock_interview_tool import generate_mock_questions
from src.tools.interview_feedback_tool import evaluate_answer
from src.tools.company_questions_tool import company_questions

interview_agent = Agent(
    name="interview_agent",
    model="gemini-2.5-flash",

    description="Interview preparation specialist",

    instruction="""
    You are an interview coach.

    Use generate_mock_questions when
    the user asks:

    - Mock interview
    - Interview questions
    - Practice questions

    Use evaluate_answer when
    the user submits an answer.

    Use company_questions when
    the user asks:

    - Google interview questions
    - Amazon interview questions
    - Company-specific preparation
    """,

    tools=[
        generate_mock_questions,
        evaluate_answer,
        company_questions
    ]
)