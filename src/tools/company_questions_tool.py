# src/tools/company_questions_tool.py

def company_questions(company: str) -> dict:

    data = {
        "google": [
            "Explain hash maps.",
            "Design URL shortener.",
            "What is BFS?"
        ],

        "amazon": [
            "Leadership principles?",
            "Two Sum problem.",
            "Database indexing?"
        ]
    }

    return {
        "company": company,
        "questions": data.get(
            company.lower(),
            ["Tell me about yourself"]
        )
    }