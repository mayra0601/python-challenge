import os
import csv

#set path
budgetdatacsv = "/Users/mayraterrazas/UCI-Folder/python-challenge/PyBank/Resources"

#open csv
with open(budgetdatacsv) as csv_file:
    csvreader = csv.reader(csv_file, delimeter= ",")
    