from src.tools.report_export_tool import (
    export_resume_report
)

sample_report = {
    "ats_score": 85,
    "strengths": [
        "Python",
        "SQL",
        "Git"
    ]
}

print(
    export_resume_report(
        sample_report
    )
)