from pathlib import Path


def export_results(cleaned_df, fuzzy_duplicates, output_dir="output"):
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Export cleaned data to CSV
    cleaned_df.to_csv(
        output_path / "customers_cleaned.csv",
        index=False,
        encoding="utf-8-sig"
    )

    # Export cleaned data to Excel
    cleaned_df.to_excel(
        output_path / "customers_cleaned.xlsx",
        index=False,
        engine="openpyxl"
    )

    # Export possible fuzzy duplicates
    fuzzy_duplicates.to_csv(
        output_path / "possible_duplicates.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("\nEXPORT COMPLETED SUCCESSFULLY!")
    print(f"Files saved to: {output_path.resolve()}")