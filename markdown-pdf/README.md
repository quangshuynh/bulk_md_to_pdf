# Markdown to Merged PDF Converter

This Python script converts all Markdown (`.md`) files in a specified folder into PDF files and then merges them into a single PDF. This is especially useful for organizing notes, combining documentation, or preparing project reports.

## Features

- **Converts Markdown files to PDF**: Each `.md` file in the folder is converted to a PDF.
- **Merges PDFs**: Combines all individual PDFs into a single merged PDF file.
- **Clean up**: Optionally deletes individual PDFs after merging.

## Requirements

- Python 3.x
- Libraries:
  - `markdown-pdf ` - for converting Markdown to PDF.
  - `PyPDF2` - for merging PDF files.


## Installation

1. **Install the required Python libraries**:

    ```bash
    pip install markdown-pdf PyPDF2
    ```

## Configuration

1. Set the folder path containing your `.md` files and the output path for the merged PDF in the `main()` function:

    ```python
    folder_path = 'C:/Users/user/Documents/Obsidian Vault/- Second Year/CSCI 243'  # Your folder with .md files
    output_pdf = 'C:/Users/user/Desktop/output/merged_output.pdf'                   # Path for the merged output PDF
    ```

## Usage

1. Run the script with Python:

    ```bash
    python main.py
    ```

2. The script will:
   - Find all `.md` files in the specified folder.
   - Convert each `.md` file to an individual PDF.
   - Merge all individual PDFs into a single PDF named `merged_output.pdf` (or as specified in `output_pdf`).
   - Delete the individual PDFs (optional step in the script).

3. The merged PDF will be saved at the location specified in `output_pdf`.


## Example

If your folder contains:
- `notes1.md`
- `notes2.md`
- `summary.md`

Running this script will create a single PDF named `merged_output.pdf` that combines the content of these Markdown files.

