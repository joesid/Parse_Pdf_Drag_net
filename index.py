import os
from PyPDF2 import PdfReader, PdfWriter

# Set the directory path containing the PDF files
pdf_directory = 'C:/Users/Joseph/Desktop/ad'

# Loop through all PDF files in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        
        # Open the PDF file and read its contents
        pdf_file = open(os.path.join(pdf_directory, filename), 'rb')
        pdf_reader = PdfReader(pdf_file)
        page_count = len(pdf_reader.pages)
        parsed_string = ''
        
        # Loop through each page of the PDF
        for page in range(page_count):
            page_obj = pdf_reader.pages[page]
            text = page_obj.extract_text()
            
            # Search for the "Dear" string
            if 'Dear' in text:
                
                # Parse the name from the line after "Dear"
                start_index = text.index('Dear') + 5
                end_index = text.find('\n', start_index)
                parsed_string = text[start_index:end_index].strip()
                break
        
        # Close the PDF file
      
        
 # Create a new filename with the parsed string appended to the front
        new_filename = parsed_string + '_' + filename
        
        # Save a copy of the PDF file with the new filename
        new_pdf = PdfWriter()
        for page in range(page_count):
            new_pdf.add_page(pdf_reader.pages[page])
        with open(os.path.join(pdf_directory, new_filename), 'wb') as output_file:
            new_pdf.write(output_file)      
