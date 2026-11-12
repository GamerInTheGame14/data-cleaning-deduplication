import pandas as pd
from rapidfuzz import fuzz


def find_fuzzy_duplicates(df, threshold=85):
    possible_duplicates = []

    records = df.to_dict("records")

    for i in range(len(records)):
        for j in range(i + 1, len(records)):

            record1 = records[i]
            record2 = records[j]

            name1 = record1.get("name")
            name2 = record2.get("name")

            # Skip missing names
            if pd.isna(name1) or pd.isna(name2):
                continue

            # Calculate name similarity
            similarity = fuzz.ratio(
                str(name1),
                str(name2)
            )

            # Check email and phone matches
            email1 = record1.get("email")
            email2 = record2.get("email")

            phone1 = record1.get("phone")
            phone2 = record2.get("phone")

            email_match = (
                pd.notna(email1)
                and pd.notna(email2)
                and email1 == email2
            )

            phone_match = (
                pd.notna(phone1)
                and pd.notna(phone2)
                and phone1 == phone2
            )

            # Require similar names and a shared contact
            if similarity >= threshold and (
                email_match or phone_match
            ):
                possible_duplicates.append({
                    "id_1": record1["id"],
                    "id_2": record2["id"],
                    "name_1": name1,
                    "name_2": name2,
                    "similarity": round(similarity, 2),
                    "email_match": email_match,
                    "phone_match": phone_match
                })

    return pd.DataFrame(possible_duplicates)