### PLP_Python_week4_assignment 

# File Handling and Exception Handling

A Python program that reads files, modifies their content, and writes to new files with comprehensive error handling.

## Features

- Reads text files
- Handles various file errors (not found, permission issues, etc.)
- Modifies content (converts to uppercase)
- Writes modified content to new files
- User-friendly interface

### Python script: [file_processor.py](file_processor.py)

## Requirements

- Python3 installed on your computer
- The script file (`file_processor.py`)
- The file you want to process (e.g., `sample.txt`) in the same folder
- Basic knowledge of using terminal/command prompt

## Usage
1. Navigate to the project directory in your terminal
2. Run the script using Python:

    ```bash
    python file_processor.py
    ```
3. Follow the prompts to input and output filenames, e.g.:
- Enter the input filename (`sample.txt`)
- Enter **any** output filename (e.g., `output.txt`, `result.pdf`, `UPPERCASE.md`)
4. The modified content (converted to uppercase) will be saved to the new file

## Example:
```
$ python file_processor.py
Upload a file: sample.txt
Save as: result.pdf
Success! File saved as 'result.pdf'
```
**Note:** The output file will contain uppercase text content regardless of the extension. If you save as `.pdf`, it will be a text file with PDF extension; not a formatted PDF document.

## Error Handling

The program handles:
- File not found errors
- Permission errors
- Other unexpected errors