📂 Python CSV Cleaner

**A modular Python utility that cleans CSV files by trimming whitespace, removing empty rows, and eliminating duplicate records.**

---

## 📌 Overview

Messy CSV files often contain unnecessary spaces, blank rows, and duplicate records that make data difficult to analyze. Python CSV Cleaner automates these basic cleaning tasks and saves the cleaned data to a separate file.

The application uses Python's built-in `csv` module to read and write CSV data and `pathlib` to validate file paths. Its modular structure separates data-cleaning logic from user interaction.

## ✨ Features

- Trim leading and trailing whitespace from cells
- Remove completely empty data rows
- Identify and remove duplicate records
- Preserve the original CSV file
- Save cleaned data to a separate output file
- Validate file paths and CSV file extensions
- Prevent accidental overwriting of existing output files
- Display a summary of the cleaning process
- Keep the application modular and easy to extend

## 🛠️ Tech Stack

- Python 3
- `csv` — reading and writing CSV files
- `pathlib` — filesystem path handling
- Lists, tuples, sets, functions, and exception handling

No third-party packages are required.

## 📁 Project Structure

```text
python-csv-cleaner/
├── main.py
├── cleaner.py
└── README.md
```

- **`main.py`** handles user input, runs the cleaning process, and displays the results.
- **`cleaner.py`** contains the CSV validation, whitespace trimming, empty-row removal, duplicate detection, and output-writing logic.

## 🚀 Getting Started

### Prerequisites

Python 3.8 or newer.

### Run the application

1. Download or clone the repository.
2. Open the project folder in your terminal.
3. Run:

```bash
python main.py
```

4. Enter the path of the CSV file you want to clean.
5. Check the summary and locate the generated cleaned file.

## 💻 Example

Suppose the input file, `sample.csv`, contains:

```csv
Name,City
 Alice , Bhopal

Rahul,Indore
Rahul,Indore
Priya,Delhi
```

After running the cleaner, `sample_cleaned.csv` contains:

```csv
Name,City
Alice,Bhopal
Rahul,Indore
Priya,Delhi
```

The program reports the number of original data rows, cleaned data rows, empty rows removed, duplicate rows removed, and cells trimmed.

## 🧠 Concepts Learned

- Reading and writing CSV files
- Working with file paths using `pathlib`
- Cleaning strings with `strip()`
- Traversing lists and processing records
- Using tuples and sets for duplicate detection
- Validating files and handling exceptions
- Separating core logic from the main program
- Preventing accidental file overwrites

## ⚠️ Safety Notes

- The original CSV file remains unchanged.
- The cleaned file is saved beside the original file.
- If the output filename already exists, the program stops instead of overwriting it.
- Duplicate detection compares complete cleaned data rows.
- Always review the cleaned output before using it for important analysis.

## 🔮 Future Improvements

- Add column-specific cleaning rules
- Handle missing values with configurable options
- Validate column names and data types
- Generate a detailed cleaning report
- Support custom output locations
- Add automated unit tests
- Build a graphical user interface

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub: [@ayushman-ece](https://github.com/ayushman-ece)

---

*Built with Python to practise data cleaning, CSV processing, and modular programming.*