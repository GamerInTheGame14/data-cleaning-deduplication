import pandas as pd

from src.cleaner import clean_data
from src.validator import validate_emails
from src.deduplicator import remove_exact_duplicates
from src.fuzzy_matcher import find_fuzzy_duplicates
from src.exporter import export_results
from src.reporter import generate_report


# Step 1: Load dataset
df = pd.read_csv(
    "data/customers_dirty.csv",
    dtype="string"
)

# Step 2: Clean data
cleaned_df = clean_data(df)

# Step 3: Validate emails
validated_df, invalid_count = validate_emails(cleaned_df)

# Step 4: Remove exact duplicates
final_df, duplicate_count = remove_exact_duplicates(
    validated_df
)

# Step 5: Find fuzzy duplicates
fuzzy_duplicates = find_fuzzy_duplicates(
    final_df,
    threshold=85
)

# Step 6: Export results
export_results(
    final_df,
    fuzzy_duplicates
)

# Step 7: Generate JSON report
report = generate_report(
    original_df=df,
    cleaned_df=final_df,
    invalid_count=invalid_count,
    duplicate_count=duplicate_count,
    fuzzy_duplicates=fuzzy_duplicates
)

# Step 8: Display summary
print("\nDATA CLEANING SUMMARY")
print("-" * 40)

for key, value in report["summary"].items():
    print(f"{key}: {value}")