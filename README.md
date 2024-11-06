# Markdown to Merged PDF Converter

This Python script converts all Markdown (`.md`) files in a specified folder into PDF files and then merges them into a single PDF. This is especially useful for organizing notes, combining documentation, or preparing project reports.

## Features

- **Converts Markdown files to PDF**: Each `.md` file in the folder is converted to a PDF.
- **Merges PDFs**: Combines all individual PDFs into a single merged PDF file.
- **Clean up**: Optionally deletes individual PDFs after merging.

## Requirements

- Python 3.x
- Libraries:
  - `markdown2` - for converting Markdown to HTML.
  - `pdfkit` - for converting HTML to PDF.
  - `PyPDF2` - for merging PDF files.
- [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) - an external tool that `pdfkit` uses for HTML-to-PDF conversion.

## Installation

1. **Install the required Python libraries**:

    ```bash
    pip install markdown2 pdfkit PyPDF2
    ```

2. **Install wkhtmltopdf**:
   - Download `wkhtmltopdf` from the official website: [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)
   - Follow the installation instructions for your OS.
   - Note the installation path (e.g., `C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe` on Windows) as you will need it to configure the script.

## Configuration

1. Open the script and ensure that the path to `wkhtmltopdf` is correctly specified:

    ```python
    path_wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"  # Adjust this if needed
    ```

2. Set the folder path containing your `.md` files and the output path for the merged PDF in the `main()` function:

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

## Troubleshooting

- **FileNotFoundError with wkhtmltopdf**:
  Ensure that `wkhtmltopdf` is installed and the path in `path_wkhtmltopdf` is correct.
- **Permission Errors**:
  Check that you have the necessary permissions for the folder where PDFs are saved.

## Example

If your folder contains:
- `notes1.md`
- `notes2.md`
- `summary.md`

Running this script will create a single PDF named `merged_output.pdf` that combines the content of these Markdown files.

