import os
import markdown2
import pdfkit
from PyPDF2 import PdfMerger

path_wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

def md_to_pdf(md_file, pdf_file):
    # convert md to HTML
    with open(md_file, 'r', encoding='utf-8') as f:
        html_content = markdown2.markdown(f.read())
    pdfkit.from_string(html_content, pdf_file, configuration=config)  # save the HTML to a PDF


def convert_and_merge_md_files(folder_path, output_pdf):
    # collect all .md files in the folder
    md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
    pdf_files = []

    # convert each .md file to PDF
    for md_file in md_files:
        md_path = os.path.join(folder_path, md_file)
        pdf_path = os.path.join(folder_path, md_file.replace('.md', '.pdf'))
        md_to_pdf(md_path, pdf_path)
        pdf_files.append(pdf_path)

    # merge all PDFs into one
    merger = PdfMerger()
    for pdf_file in pdf_files:
        merger.append(pdf_file)

    # save the merged PDF
    merger.write(output_pdf)
    merger.close()

    # cleanup individual PDF files
    for pdf_file in pdf_files:
        os.remove(pdf_file)

    print(f"Merged PDF created at: {output_pdf}")


def main():
    folder_path = 'C:/Users/user/Documents/Obsidian Vault/- Second Year/CSCI 243'  # replace with the path to your folder with .md files
    output_pdf = 'C:/Users/user/Desktop/output/merged_output.pdf'  # name of the output merged PDF
    convert_and_merge_md_files(folder_path, output_pdf)


if __name__ == "__main__":
    main()
