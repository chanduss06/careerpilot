# src/tools/interview_feedback_tool.py

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

    return {
        "score": score,
        "feedback": feedback
    }