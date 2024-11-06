import os
from markdown_pdf import MarkdownPdf, Section
from PyPDF2 import PdfMerger


def convert_md_to_pdf(md_file, pdf_file):
    # initialize MarkdownPdf with desired settings
    pdf = MarkdownPdf(toc_level=1)  # toc_level controls the depth of table of contents in the PDF

    # read the content of the markdown file
    with open(md_file, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # create a section for the content
    section = Section(md_content)

    # add the section to the PDF
    pdf.add_section(section)

    # save the section to PDF
    pdf.save(pdf_file)


def convert_and_merge_md_files(folder_path, output_pdf):
    # collect all .md files in the folder
    md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
    pdf_files = []

    # convert each .md file to PDF
    for md_file in md_files:
        md_path = os.path.join(folder_path, md_file)
        pdf_path = os.path.join(folder_path, md_file.replace('.md', '.pdf'))
        convert_md_to_pdf(md_path, pdf_path)
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
    folder_path = 'C:/Users/user/Documents/Obsidian Vault/- Second Year/CSCI 243'  # replace with folder path
    output_pdf = 'C:/Users/user/Desktop/output/merged_output2.pdf'  # output merged PDF path
    convert_and_merge_md_files(folder_path, output_pdf)


if __name__ == "__main__":
    main()
