# Data Cleaning & Deduplication Tool

A Python-based data cleaning and deduplication tool designed to transform messy customer datasets into clean, structured, and analysis-ready data.

The project demonstrates practical data processing, validation, duplicate detection, fuzzy matching, automated reporting, and testing.

## Features

- Import customer data from CSV files
- Standardize names, emails, phone numbers, and cities
- Detect invalid email formats
- Remove exact duplicate records
- Identify potential duplicates using fuzzy matching
- Export cleaned datasets to CSV and Excel
- Generate JSON data quality reports
- Run automated tests with pytest
- Continuous integration with GitHub Actions

## Technologies

- Python 3.11
- Pandas
- RapidFuzz
- OpenPyXL
- Pytest
- GitHub Actions

## Project Structure

```text
data-cleaning-deduplication/
├── .github/
│   └── workflows/
│       └── tests.yml
├── data/
│   └── customers_dirty.csv
├── src/
│   ├── cleaner.py
│   ├── validator.py
│   ├── deduplicator.py
│   ├── fuzzy_matcher.py
│   ├── exporter.py
│   └── reporter.py
├── tests/
│   └── test_pipeline.py
├── check_data.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/GamerInTheGame14/data-cleaning-deduplication.git
cd data-cleaning-deduplication
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the complete cleaning pipeline:

```bash
python check_data.py
```

The tool reads the sample dataset from:

`data/customers_dirty.csv`

It then cleans and validates the data, removes exact duplicates, and identifies potential fuzzy duplicates.

## Example Results

| Metric                    | Result |
| ------------------------- | -----: |
| Original records          |     15 |
| Invalid email formats     |      1 |
| Exact duplicates removed  |      3 |
| Final records             |     12 |
| Potential duplicate pairs |      1 |

These results are based on the included sample dataset.

## Output Files

After running the program, the following files are generated:

```text
output/
├── customers_cleaned.csv
├── customers_cleaned.xlsx
├── possible_duplicates.csv
└── report.json
```

### Cleaned Dataset

The cleaned CSV and Excel files contain standardized customer records with exact duplicates removed.

### Potential Duplicates

The `possible_duplicates.csv` file contains possible duplicate pairs detected using RapidFuzz.

Potential matches are flagged for manual review rather than automatically deleted.

### Data Quality Report

The `report.json` file provides a summary of the cleaning process, including record counts, invalid email formats, duplicate counts, and missing values.

## Automated Tests

Run the tests:

```bash
python -m pytest -v
```

The project includes five automated tests covering data cleaning, email validation, exact deduplication, fuzzy matching, and the complete sample pipeline.

## Continuous Integration

GitHub Actions automatically runs the test suite on pushes and pull requests.

## Limitations

- The current pipeline uses a predefined CSV input file.
- Email validation checks syntax, not mailbox existence.
- Phone numbers are normalized to digits without country-specific validation.
- Fuzzy matches are flagged for manual review.
- Exact deduplication retains the first matching record.

## Author

Developed as a Python data processing portfolio project.

## License

No license is currently specified.
