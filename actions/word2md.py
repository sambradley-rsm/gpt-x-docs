import os
import re
from docx import Document

# Specify the folder for Word and Markdown documents
DOCX_FOLDER = '../docs/docx'
MD_FOLDER = '../docs/markdown'

def convert_docx_to_md(docx_file, md_file):
    # Load the Word document
    doc = Document(docx_file)
    
    md_lines = []

    # Parse each paragraph in the Word document
    for para in doc.paragraphs:
        style = para.style.name.lower()
        text = para.text.strip()

        if not text:
            continue

        # Determine Markdown equivalent based on Word styles
        if style.startswith('heading 1'):
            md_lines.append(f'# {text}')
        elif style.startswith('heading 2'):
            md_lines.append(f'## {text}')
        elif style.startswith('heading 3'):
            md_lines.append(f'### {text}')
        elif style.startswith('heading 4'):
            md_lines.append(f'#### {text}')
        elif style.startswith('list bullet'):
            md_lines.append(f'- {text}')
        else:
            # Handle bold text and hyperlinks
            md_line = parse_and_extract_bold_and_links(para)
            md_lines.append(md_line)

    # Write the Markdown content to a file
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))

    print(f"Converted {docx_file} to {md_file}")

def parse_and_extract_bold_and_links(paragraph):
    md_line = ''


    for run in paragraph.runs:
        text = run.text
        if run.bold:
            text = f'**{text}**'

        # Check if the run is part of a hyperlink by checking the hyperlinks in the paragraph
        for hyperlink in paragraph.hyperlinks:
            print(hyperlink.text, hyperlink.url)
            if text in hyperlink.text:
                text = f'[{text}]({hyperlink.url})'
                break

        md_line += text

    return md_line

# List .docx files and prompt for selection
def select_docx_file():
    files = [f for f in os.listdir(DOCX_FOLDER) if f.endswith(".docx")]
    if not files:
        print("No Word files found.")
        return None
    print("Select a Word file to convert to Markdown:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    
    choice = input(f"Enter the number (1-{len(files)}): ")
    try:
        selected_file = files[int(choice) - 1]
        return os.path.join(DOCX_FOLDER, selected_file)
    except (IndexError, ValueError):
        print("Invalid choice.")
        return None

if __name__ == "__main__":
    docx_file = select_docx_file()
    if docx_file:
        md_filename = os.path.basename(docx_file).replace('.docx', '.md')
        md_file = os.path.join(MD_FOLDER, md_filename)
        
        # Normalize the path to ensure correct separators
        md_file = md_file.replace('\\', '/')
        
        convert_docx_to_md(docx_file, md_file)