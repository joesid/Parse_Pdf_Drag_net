import os
import PyPDF2

# Open the PDF file
pdf_file = open('rewrite.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Create a directory to save the page files
if not os.path.exists('page_files'):
    os.mkdir('page_files')

# Loop through each page in the PDF
for page_num, page in enumerate(pdf_reader.pages):
    # Get the text from the current page
    page_text = page.extract_text()

    # Split the page text into lines
    lines = page_text.split('\n')

    # Get the fourth line's content as the file name
    file_name = lines[5]

    # Remove any characters that are not allowed in file names
    file_name = ''.join(c for c in file_name if c.isalnum() or c.isspace())

    # Save the page as a separate file with the fourth line's content as its file name
   # file_path = f"page_files/{file_name}_page_{page_num+1}.pdf"
    file_path = f"page_files/{file_name}_2022_National_Award_Letter_Signed.pdf"
    with open(file_path, 'wb') as f:
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(page)
        pdf_writer.write(f)

# Close the PDF file
pdf_file.close()
