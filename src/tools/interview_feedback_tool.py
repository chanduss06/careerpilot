# src/tools/interview_feedback_tool.py
from src.memory.interview_store import (
    save_interview_score
)

def evaluate_answer(answer: str) -> dict:

    score = min(
        len(answer.split()) * 2,
        100
    )

    feedback = []

    if len(answer.split()) < 20:

        feedback.append(
            "Answer is too short."
        )

    else:

        feedback.append(
            "Good detailed answer."
        )

    save_interview_score(score)

    return {
        "score": score,
        "feedback": feedback
    }