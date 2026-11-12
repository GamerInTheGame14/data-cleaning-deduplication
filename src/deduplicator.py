def remove_exact_duplicates(df):
    df = df.copy()

    # Columns used to identify duplicate customers
    columns = ["name", "email", "phone", "city"]

    # Find duplicate records
    duplicate_mask = df.duplicated(
        subset=columns,
        keep="first"
    )

    # Count duplicates
    duplicate_count = int(duplicate_mask.sum())

    # Remove duplicates
    df = df.loc[~duplicate_mask].copy()

    return df, duplicate_count