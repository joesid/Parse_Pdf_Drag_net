import PyPDF2

# Open the PDF file
pdf_file = open('test.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

#Create a new text file
text_file = open('output.txt', 'w')

# Loop through each page in the PDF
for page in range(len(pdf_reader.pages)):
    # Get the text from the current page
    page_obj = pdf_reader.pages[page]
    page_text = page_obj.extract_text()

     # Print the page text
    print(page_text)

    #Write the page text to the text file
    text_file.write(page_text)
    
   

# Close the PDF file
pdf_file.close()
