import os

directory = 'C:/Users/Joseph/Desktop/AB'

#This code simply parses a filenames in a directory and truncates every string after 'Letter" and ends just before .pdf
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        new_filename = filename.split(' Letter')[0] + ' Letter.pdf'
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
