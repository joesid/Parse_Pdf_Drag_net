# Parse_Pdf_Drag_net

IT Manager/IT Support Specialist


CAUSE
I was required to assist with the broadcasting of "Awardee Letter" to our Client Customers, however the pdf files of the email sent had generic naming schmeme then with a single name at the end 

e.g "TL_Scholarship_Letter_name.pdf"  and since using a single name can cause a serious mismatch e.g one peron can have "Uche" as first name another can have it as last name.

I noticed a common trend on each of the letter that it was addressed as "Dear {FirstName} {LastName}

Then I wrote this code to read the first two strings(Names) after Dear then append it to the front of the filename, then parse the newfilename and truncate the name after "Letter" in the filename.



SCRIPT FILE USAGE
The index1.py was designed to Parse the content of a Pdf document(a letter) then Take the first two strings after the first occurence of the word "Dear"

Then use this strings, to rename the file, by adding it to the front of the filename.

The index2.py, basically truncates every character after the string "Letter" in the filename but stops right before the extension ".pdf"


SOFTWARE VERSION USED

PIP Version 23.1.1 Python Version 3.10.11

OS Windows 11 22H2 (Build 22621.5555)
