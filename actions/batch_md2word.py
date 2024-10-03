import os
from md2word import convert_md_to_docx  # Assuming this is the name of your current script

# Specify the folder for Markdown and Word documents
MD_FOLDER = '../docs/markdown'
DOCX_FOLDER = '../docs/docx'

def convert_all_md_files():
    # List all markdown files in the folder
    md_files = [f for f in os.listdir(MD_FOLDER) if f.endswith(".md")]

    if not md_files:
        print("No Markdown files found to convert.")
        return

    for md_file in md_files:
        # Full path of the markdown file
        md_file_path = os.path.join(MD_FOLDER, md_file)

        # Create the corresponding docx filename
        docx_filename = md_file.replace('.md', '.docx')
        docx_file_path = os.path.join(DOCX_FOLDER, docx_filename)

        # Convert the markdown file to a Word document
        try:
            print(f"Converting {md_file_path} to {docx_file_path}...")
            convert_md_to_docx(md_file_path, docx_file_path)
            print(f"Successfully converted {md_file_path} to {docx_file_path}.")
        except Exception as e:
            print(f"Failed to convert {md_file_path}: {e}")

if __name__ == "__main__":
    convert_all_md_files()
