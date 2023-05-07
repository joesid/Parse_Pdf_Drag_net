# Parse_Pdf_Drag_net

### Table Of Contents

[Getting Started]
[Usage]
[Contribuitng]
[License]
[Acknowledgements]

IT Manager/IT Support Specialist


CAUSE
I was required to assist with the broadcasting of "Awardee Letter" to our Client Customers, however the pdf files of the email sent had generic naming schmeme then with a single name at the end 

e.g "TL_Scholarship_Letter_name.pdf"  and since using a single name can cause a serious mismatch e.g one peron can have "Uche" as first name another can have it as last name.

I noticed a common trend on each of the letter that it was addressed as "Dear {FirstName} {LastName}

Then I wrote this code to read the first two strings(Names) after Dear then append it to the front of the filename, then parse the newfilename and truncate the name after "Letter" in the filename.

INDEX 3, 4 & 5 added  - 2nd May 2023
Sequel to the 1st cause, I was asked to assist in the broadcast of another set of letters, only this the letters were merged together in a single PDF and there weren't addressed in this format "Dear {FirstName} {LastName}, Luckily for me the name string sat together on it's own on a single line (at least that was my assumption)



SCRIPT FILE USAGE
The index1.py was designed to Parse the content of a Pdf document(a letter) then Take the first two strings after the first occurence of the word "Dear"

Then use this strings, to rename the file, by adding it to the front of the filename.

The index2.py, basically truncates every character after the string "Letter" in the filename but stops right before the extension ".pdf"

index3.py was to read the code and print out the text on each line and the line number.

index4.py was to read the line and copy it to a text, cause I assumed something was wrong with "Index3.py", however it turns out the pdf which I used to run test on index3, I had unwittingly modified to be text inaccessible 

index5, using line postion from index3.py or index4.py, it takes the string sitting on that line and append it to the front of the filename, joining it with a designated text format provided by me.

NOTE: The line counts is restarted on each page, so index5 seperates the pdf to a seperate file (page by page) and renames it with the aforementioned format 

### PREQUISITES

- PIP Version 23.1.1

- Python Version 3.10.11

- OS Windows 11 22H2 (Build 22621.5555)

### INSTALLING

### RUNNING THE TESTS

### USAGE


### CONTRIBUTING

