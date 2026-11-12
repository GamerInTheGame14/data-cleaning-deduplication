
import pandas as pd

from src.cleaner import clean_data
from src.validator import validate_emails
from src.deduplicator import remove_exact_duplicates
from src.fuzzy_matcher import find_fuzzy_duplicates


def test_clean_data():
    df = pd.DataFrame({
        "name": ["  john   smith  "],
        "email": [" JOHN@GMAIL.COM "],
        "phone": ["555-1234"],
        "city": ["new york"]
    })

    result = clean_data(df)

    assert result.loc[0, "name"] == "John Smith"
    assert result.loc[0, "email"] == "john@gmail.com"
    assert result.loc[0, "phone"] == "5551234"
    assert result.loc[0, "city"] == "New York"


def test_invalid_email():
    df = pd.DataFrame({
        "email": ["john@gmail.com", "invalid-email", None]
    })

    result, invalid_count = validate_emails(df)

    assert invalid_count == 1
    assert result.loc[0, "email"] == "john@gmail.com"
    assert pd.isna(result.loc[1, "email"])
    assert pd.isna(result.loc[2, "email"])


def test_exact_duplicates():
    df = pd.DataFrame({
        "id": ["1", "2", "3"],
        "name": ["John Smith", "John Smith", "Alice Brown"],
        "email": ["john@gmail.com", "john@gmail.com", "alice@gmail.com"],
        "phone": ["5551234", "5551234", "5555678"],
        "city": ["New York", "New York", "Chicago"]
    })

    result, duplicate_count = remove_exact_duplicates(df)

    assert duplicate_count == 1
    assert len(result) == 2
    assert result["id"].tolist() == ["1", "3"]


def test_fuzzy_duplicates():
    df = pd.DataFrame({
        "id": ["13", "14"],
        "name": ["James Anderson", "James Andersen"],
        "email": ["james@gmail.com", "james@gmail.com"],
        "phone": ["5556666", "5556666"],
        "city": ["San Francisco", "San Francisco"]
    })

    result = find_fuzzy_duplicates(df, threshold=85)

    assert len(result) == 1
    assert result.iloc[0]["id_1"] == "13"
    assert result.iloc[0]["id_2"] == "14"
    assert bool(result.iloc[0]["email_match"]) is True
    assert bool(result.iloc[0]["phone_match"]) is True


def test_full_dataset():
    df = pd.read_csv(
        "data/customers_dirty.csv",
        dtype="string"
    )

    cleaned = clean_data(df)

    validated, invalid_count = validate_emails(cleaned)

    final, duplicate_count = remove_exact_duplicates(validated)

    fuzzy = find_fuzzy_duplicates(final, threshold=85)

    assert len(df) == 15
    assert invalid_count == 1
    assert duplicate_count == 3
    assert len(final) == 12
    assert len(fuzzy) == 1
