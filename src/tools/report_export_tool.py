# src/tools/report_export_tool.py

from src.mcp.drive_mcp import (
    save_report_to_drive
)


def export_resume_report(
    report_data: dict
) -> dict:

    report_content = str(
        report_data
    )

    return save_report_to_drive(
        "resume_report.txt",
        report_content
    )