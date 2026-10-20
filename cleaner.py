
import csv
from pathlib import Path


def clean_csv(input_path):
    source = Path(input_path).expanduser()

    if not source.exists() or not source.is_file():
        raise ValueError("Input file does not exist.")

    if source.suffix.lower() != ".csv":
        raise ValueError("Please provide a CSV file.")

    output = source.with_name(f"{source.stem}_cleaned.csv")

    if output.exists():
        raise FileExistsError(
            f"Output already exists: {output}\n"
            "Rename or remove it before running again."
        )

    with source.open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        raise ValueError("The CSV file is empty.")

    header = [cell.strip() for cell in rows[0]]

    if not any(header):
        raise ValueError("The CSV header is empty.")

    cleaned_rows = []
    seen = set()
    empty_rows = 0
    duplicate_rows = 0
    trimmed_cells = 0

    for row in rows[1:]:
        if not any(cell.strip() for cell in row):
            empty_rows += 1
            continue

        cleaned_row = []

        for cell in row:
            stripped = cell.strip()
            if stripped != cell:
                trimmed_cells += 1
            cleaned_row.append(stripped)

        record = tuple(cleaned_row)

        if record in seen:
            duplicate_rows += 1
            continue

        seen.add(record)
        cleaned_rows.append(cleaned_row)

    with output.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(cleaned_rows)

    return {
        "output": str(output),
        "original_rows": len(rows) - 1,
        "cleaned_rows": len(cleaned_rows),
        "empty_rows_removed": empty_rows,
        "duplicate_rows_removed": duplicate_rows,
        "cells_trimmed": trimmed_cells,
    }
