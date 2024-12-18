# BookBot

BookBot is a simple Python script designed to analyze a text file and generate a character count report. This is my first project, built to explore Python programming fundamentals and file handling.

## Features

- Counts the occurrence of each character (case-insensitive) in a text file.
- Reports the total number of words in the document.
- Provides a detailed count of each letter from A to Z.

## How It Works

1. The script reads a text file (`books/frankenstein.txt` by default).
2. It analyzes the content to count characters and spaces.
3. It prints a report summarizing the findings:
   - Total words in the document.
   - Frequency of each letter in the alphabet.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/bookbot.git
   ```
2. Navigate to the project folder:
   ```bash
   cd bookbot
   ```
3. Download the `frankenstein.txt` file from the following URL and place it in the `books/` directory:
   ```bash
   curl -o books/frankenstein.txt https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt
   ```

## Usage

Run the script using Python:
```bash
python main.py
```

## Example Output

```
--- Begin report of books/frankenstein.txt ---
45,123 words found in the document

The letter 'a' was found 2,345 times
The letter 'b' was found 1,234 times
...
--- End Report ---
```

## Customization

You can change the analyzed text file by modifying the `filepath` variable in the `main.py` file:
```python
filepath = 'path/to/your/file.txt'
```
