# src/tools/mock_interview_tool.py

def generate_mock_questions(role: str) -> dict:

    questions = {
        "python": [
            "What is a list?",
            "Difference between list and tuple?",
            "What is OOP?"
        ],

        "java": [
            "What is JVM?",
            "What is inheritance?",
            "Difference between interface and class?"
        ],

        "backend": [
            "What is REST API?",
            "What is authentication?",
            "Explain HTTP methods."
        ]
    }

    return {
        "role": role,
        "questions": questions.get(
            role.lower(),
            ["Tell me about yourself"]
        )
    }