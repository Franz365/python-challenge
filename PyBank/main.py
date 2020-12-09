# PyBank main script

import os
import csv

# Create a variable that contains the path to the data file
budget_csv = os.path.join("Resources", "PyBank_budget_data.csv")
print(budget_csv)
# Open and read csv
with open(budget_csv, "r") as csv_file:

    # split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # skip the first row as it contains headers
    next(csv_reader, None)
    
    # define  lists of months and profits
    months = []
    profits = []

    # add every month into the list
    for row in csv_reader:
        months.append(row[0])
        profits.append(float(row[1]))
    
    # total number of months in included in the dataset
    months_number = len(months)   
   

    # net total of profits
    net_total = 0
    for number in profits:
        net_total += number
   

    # calculate changes
    change = []
    old_number = profits[0]
    for number in profits:
        change.append(number - old_number)
        old_number = number
    
    # average of the changes
    average = sum(change) / (len(change)-1)
    

    # greatest increase in profits
    increase = max(change)
    

    # greates decrease
    decrease = min(change)
    

    # adding the months
    dictionary = dict(zip(change, months))
    

# print financial analysis in terminal
print("Financial Analaysis")
print("----------------------------")
print(f"Total Months: {months_number}")
print(f"Total: ${net_total}")
print(f"Average Change: {average}")
print(f"Greatest Increase in Profits: {dictionary[increase]} (${increase})")
print(f"Greatest Decrease in Profits: {dictionary[decrease]} (${decrease})")

# create txt file with analysis
f = open("Analysis/Analysis.txt", "w" )
f.write(
    "Financial Analaysis\n"
    "----------------------------\n"
    f"Total Months: {months_number}\n"
    f"Total: ${net_total}\n"
    f"Average Change: {average}\n"
    f"Greatest Increase in Profits: {dictionary[increase]} (${increase})\n"
    f"Greatest Decrease in Profits: {dictionary[decrease]} (${decrease})\n"
    )