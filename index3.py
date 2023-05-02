import PyPDF2

# Open the PDF file
pdf_file = open('rewrite.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Loop through each page in the PDF
for page in range(len(pdf_reader.pages)):
    # Get the text from the current page
    page_text = pdf_reader.pages[page].extract_text()

    # Split the page text into lines
    lines = page_text.split('\n')

    # Loop through each line and print the line number and content
    for line_num, line in enumerate(lines):
        print(f"Line {line_num}: {line}")
