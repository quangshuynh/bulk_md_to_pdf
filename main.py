import os
import markdown2
import pdfkit
from PyPDF2 import PdfMerger

# path to wkhtmltopdf executable
path_wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# path to CSS file
css_path = "styles.css"

# MathJax script to enable LaTeX rendering in HTML
mathjax_script = """
<script type="text/javascript" async
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
"""

def md_to_pdf(md_file, pdf_file):
    # Convert Markdown to HTML
    with open(md_file, 'r', encoding='utf-8') as f:
        html_content = markdown2.markdown(f.read(), extras=["fenced-code-blocks"])

    # Add MathJax for LaTeX rendering
    full_html = f"<!DOCTYPE html><html><head>{mathjax_script}</head><body>{html_content}</body></html>"

    # Save the HTML to a PDF using configured wkhtmltopdf and apply CSS
    pdfkit.from_string(full_html, pdf_file, configuration=config, css=css_path)

def convert_and_merge_md_files(folder_path, output_pdf):
    # Collect all .md files in the folder
    md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
    pdf_files = []

    # Convert each .md file to PDF
    for md_file in md_files:
        md_path = os.path.join(folder_path, md_file)
        pdf_path = os.path.join(folder_path, md_file.replace('.md', '.pdf'))
        md_to_pdf(md_path, pdf_path)
        pdf_files.append(pdf_path)

    # Merge all PDFs into one
    merger = PdfMerger()
    for pdf_file in pdf_files:
        merger.append(pdf_file)

    # Save the merged PDF
    merger.write(output_pdf)
    merger.close()

    # Cleanup individual PDF files
    for pdf_file in pdf_files:
        os.remove(pdf_file)

    print(f"Merged PDF created at: {output_pdf}")

def main():
    folder_path = 'C:/Users/user/Documents/Obsidian Vault/- Second Year/CSCI 243'  # Replace with your folder path
    output_pdf = 'C:/Users/user/Desktop/output/merged_output.pdf'  # Output merged PDF path
    convert_and_merge_md_files(folder_path, output_pdf)

if __name__ == "__main__":
    main()
