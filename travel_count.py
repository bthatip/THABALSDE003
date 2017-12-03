'''
This File invokes uses NLTK module to give the count of Travel word
- NLTK is used for Tokenization and Filtering
- Generate list of Tokens and Counts the word Travel
 
Author: Bala Vineeth Netha Thatipamula
'''

# Relavant Libraries
import os
from subprocess import call
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Making txt files from PDF files
pdf_files = [file for file in os.listdir('./Reports') if '.pdf' in file]
for pdf_file in pdf_files:
    call(["pdftotext", "Reports/" + pdf_file])

# Get the List of txt files from the current directory
text_files = [file for file in os.listdir('./Reports') if '.txt' in file]

# Processing each text file containg the text
for txt_file in text_files:
    travel_counter = 0
    with open("Reports/" + txt_file, 'rb') as myfile:
        text_content = myfile.read().decode('utf-8')

    tokens = word_tokenize(text_content)
    punctuations = ['(',')',';',':','[',']',',']
    stop_words = stopwords.words('english')
    filtered_tokens = [ word.lower() for word in tokens if not word in stop_words and  not word in punctuations ]
    # print tokens
    travel_counter += filtered_tokens.count('travel')
    print"*********************"
    print("Name: {} ---- Travel count:{}".format( txt_file[:-4], travel_counter ))
