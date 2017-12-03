'''
This File invokes both pdfs.py file and travel_count.py
First: It invokes pdfs.py           --      Downloads the PDFs to Reports Folder/Directory
Second: It invokes travel_count.py  --      Counts Travel word in all the PDFs

Author: Bala Vineeth Netha Thatipamula
'''

#Relavant Libraries
import os
from subprocess import call

#First Call - pdfs.py
call(["mkdir", "Reports"])
call(["scrapy", "runspider", "pdfs.py"])

#Second Call - travel_count.py
call(["python", "travel_count.py"])

#Third Call - Remove all the txt files
dir_name = "./Reports"
reports = os.listdir(dir_name)
for item in reports:
    if item.endswith(".txt"):
        os.remove(os.path.join(dir_name, item))
