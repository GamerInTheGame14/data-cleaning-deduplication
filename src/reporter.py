import json
from pathlib import Path
from datetime import datetime, timezone


def generate_report(
    original_df,
    cleaned_df,
    invalid_count,
    duplicate_count,
    fuzzy_duplicates,
    output_dir="output"
):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Count missing values in final dataset
    missing_values = {
        column: int(count)
        for column, count in cleaned_df.isna().sum().items()
    }

    # Build report
    report = {
        "generated_at": datetime.now(
            timezone.utc
        ).isoformat(),

        "summary": {
            "original_records": len(original_df),
            "final_records": len(cleaned_df),
            "exact_duplicates_removed": duplicate_count,
            "invalid_emails_found": invalid_count,
            "possible_fuzzy_duplicate_pairs": len(fuzzy_duplicates)
        },

        "data_quality": {
            "missing_values_by_column": missing_values,
            "total_missing_values": sum(missing_values.values())
        }
    }

    report_file = output_path / "report.json"

    with open(report_file, "w", encoding="utf-8") as file:
        json.dump(
            report,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("\nREPORT GENERATED SUCCESSFULLY!")
    print(f"Report saved to: {report_file.resolve()}")

    return report