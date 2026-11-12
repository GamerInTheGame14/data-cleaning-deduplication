import re
import pandas as pd


EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)


def validate_emails(df):
    df = df.copy()

    invalid_count = 0

    for index, email in df["email"].items():

        # Missing emails are handled separately
        if pd.isna(email) or not str(email).strip():
            continue

        if not EMAIL_PATTERN.fullmatch(str(email)):
            df.at[index, "email"] = pd.NA
            invalid_count += 1

    return df, invalid_count