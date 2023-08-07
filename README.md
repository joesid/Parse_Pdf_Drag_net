# Parse_Pdf_Drag_net

### Table Of Contents

[Getting Started]
[Usage]
[Contribuitng]
[License]
[Acknowledgements]

IT Manager/IT Support Specialist


CAUSE
I was required to assist with the broadcasting of an "Awardee Letter" to our Client Customers, however, the pdf files of the email sent had a generic naming scheme then with a single name at the end 

e.g "TL_Scholarship_Letter_name.pdf"  and since using a single name can cause a serious mismatch e.g one person can have "Uche" as their first name another can have it as their last name.

I noticed a common trend on each of the letters that it was addressed as "Dear {FirstName} {LastName}

Then I wrote this code to read the first two strings(Names) after Dear then append it to the front of the filename, then parse the new filename and truncate the name after "Letter" in the filename.

INDEX 3, 4 & 5 added  - 2nd May 2023
Sequel to the 1st cause, I was asked to assist in the broadcast of another set of letters, only the letters were merged together in a single PDF and there weren't addressed in this format "Dear {FirstName} {LastName}, Luckily for me the name string sat together on its own on a single line (at least that was my assumption)




### PREREQUISITES

- PIP Version 23.1.1

- Python Version 3.10.11

- OS Windows 11 22H2 (Build 22621.5555)

### INSTALLING

### RUNNING THE TESTS

### USAGE

SCRIPT FILE USAGE
The index1.py was designed to Parse the content of a Pdf document(a letter) and then Take the first two strings after the first occurrence of the word "Dear"

Then use these strings, to rename the file, by adding it to the front of the filename.

The index2.py basically truncates every character after the string "Letter" in the filename but stops right before the extension ".pdf"

index3.py was to read the code and print out the text on each line and the line number.

index4.py was to read the line and copy it to a text, cause I assumed something was wrong with "Index3.py", however it turns out the pdf which I used to run a test on index3, I had unwittingly modified to be text inaccessible 

index5, using line position from index3.py or index4.py, takes the string sitting on that line and appends it to the front of the filename, joining it with a designated text format provided by me.

NOTE: The line counts are restarted on each page, so index5 separates the pdf into a separate file (page by page) and renames it with the aforementioned format 


### CONTRIBUTING

