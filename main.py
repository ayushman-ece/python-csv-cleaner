import csv
from cleaner import clean_csv


def main():
    print("=" * 42)
    print("           PYTHON CSV CLEANER")
    print("=" * 42)

    file_path = input("Enter the CSV file path: ").strip().strip('"')

    if not file_path:
        print("Error: File path cannot be empty.")
        return

    try:
        result = clean_csv(file_path)

        print("\nCleaning completed!")
        print(f"Original data rows: {result['original_rows']}")
        print(f"Cleaned data rows: {result['cleaned_rows']}")
        print(f"Empty rows removed: {result['empty_rows_removed']}")
        print(f"Duplicate rows removed: {result['duplicate_rows_removed']}")
        print(f"Cells trimmed: {result['cells_trimmed']}")
        print(f"Output file: {result['output']}")

    except (ValueError, FileExistsError, OSError, csv.Error) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
