from pathlib import Path


REPORTS_DIR = Path("reports")

REPORTS_DIR.mkdir(
    exist_ok=True
)


def save_report_to_drive(
    report_name: str,
    report_content: str
) -> dict:
    """
    Simulated Google Drive MCP.
    """

    report_path = (
        REPORTS_DIR /
        report_name
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            report_content
        )

    return {
        "status": "success",
        "report_name": report_name,
        "path": str(report_path),
        "message": f"{report_name} saved to Google Drive"
    }