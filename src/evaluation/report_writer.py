import json
from datetime import datetime
from pathlib import Path


def save_report(
    report: dict,
    experiment_name: str,
) -> Path:
    """
    Save an evaluation report as a JSON file.
    """

    reports_directory = Path("reports")
    reports_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    report_path = reports_directory / (
        f"{experiment_name}_{timestamp}.json"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            report,
            file,
            indent=4,
            ensure_ascii=False,
        )

    return report_path