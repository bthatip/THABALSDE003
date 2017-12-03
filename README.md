# THABALSDE003

## Project Description:
In this project, I had to download all the reports from http://ir.expediainc.com/annuals.cfm. After downloading all the PDF files from this page, I have to use NLTK module to find the count of word "Travel" in all these PDF files.

## Technologies Used:
- **Python** -  Python 2.7.12
- **Scrapy** - A Fast and Powerful Web-Crawler Framework - Uses Python
- **NLTK** - Natural Language Tool Kit - For Processing Text Documents

## Relavant Files: 
- **main.py**: This python file is used to run both the files pdfs.py and travel_counter.py
- **pdfs.py**: This file is used for downloading all the PDF documents from http://ir.expediainc.com/annuals.cfm
- **travel_counter.py**: This file is used for counting *"Travel"* word in all the downloaded PDF files.

## How to Run:
- Download/Clone the files from the repository. 
- Then go into the folder/directory in which the project is present and open the terminal and just type **_python main.py_**.

## Results:
- Upon running *python main.py*, It will download all the Reports (PDFs) in a directory called **_Reports_**.
- It will display all the Names of the files along with Count of Travel word in each of the downloaded PDF files on the terminal. 
