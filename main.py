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
