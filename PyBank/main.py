import os
import csv

#set path
budgetdata_csv = "/Users/mayraterrazas/UCI-Folder/python-challenge/PyBank/Resources/budget_data.csv"

#variables in data
Total_Months = []
Total_Profit = []
Profit_Change = [] 

#read and open csv
with open(budgetdata_csv, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #skip header row
    csv_header = next(csv_file)
    
    #loops
    for row in csv_reader:
        
        Total_Months.append(row[0])
        
        Total_Profit.append(int(row[1]))

    for i in range(len(Total_Profit)-1):
        Profit_Change.append(Total_Profit[i+1]-Total_Profit[i])
 
#greatest increase and decrease in profits

Greatest_Increase = max(Profit_Change)
Greatest_Decrease = min(Profit_Change)

Greatest_Decrease = Profit_Change.index(min(Profit_Change)) + 1
Greatest_Increase = Profit_Change.index(max(Profit_Change)) + 1

#output path
output_file = os.path.join("/Users/mayraterrazas/UCI-Folder/python-challenge/PyBank/analysis/financial_analysis.txt")

with open(output_file, 'w') as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(Total_Months)}")
    file.write("\n")
    file.write(f"Total: ${sum(Total_Profit)}")
    file.write("\n")
    file.write(f"Average Change: {(sum(Profit_Change)/len(Profit_Change))}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {Total_Months[Greatest_Increase]} (${(str(Greatest_Increase))}")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {Total_Months[Greatest_Decrease]} (${(str(Greatest_Decrease))}")
    
 
#print to terminal    
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(Total_Months)}")
print(f"Total: ${sum(Total_Profit)}")
print(f"Average Change: {(sum(Profit_Change)/len(Profit_Change))}")
print(f"Greatest Increase in Profits: {Total_Months[Greatest_Increase]} (${(str(Greatest_Increase))}")
print(f"Greatest Decrease in Profits: {Total_Months[Greatest_Decrease]} (${(str(Greatest_Decrease))}")