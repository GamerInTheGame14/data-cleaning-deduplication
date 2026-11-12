import pandas as pd


def clean_data(df):
    df = df.copy()

    # 1. Names: remove extra spaces and standardize capitalization
    df["name"] = (
        df["name"]
        .astype("string")
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.title()
    )

    # 2. Emails: remove spaces and convert to lowercase
    df["email"] = (
        df["email"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    # 3. Phones: keep digits only
    df["phone"] = (
        df["phone"]
        .astype("string")
        .str.replace(r"\D", "", regex=True)
    )

    # 4. Cities: standardize capitalization
    df["city"] = (
        df["city"]
        .astype("string")
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.title()
    )

    return df