import os
import csv
from pathlib import Path


file_directory = Path('C:/Users/Moham/IdeaProjects/python-challenge/PyBank/Resources/budget_data.csv')


tot_months = []
tot_profit = []
monthly_profit_change = []


with open(file_directory, newline="", encoding="utf-8") as budget:

    csvreader = csv.reader(budget, delimiter=",")


    header = next(csvreader)



    for row in csvreader:

        # Append the total months and total profit to their corresponding lists
        tot_months.append(row[0])
        tot_profit.append(int(row[1]))

    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(tot_profit) - 1):

        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(tot_profit[i + 1] - tot_profit[i])

# Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)


max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1



print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(tot_months)}")
print(f"Total: ${sum(tot_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change) / len(monthly_profit_change), 2)}")
print(f"Greatest Increase in Profits: {tot_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {tot_months[max_decrease_month]} (${(str(max_decrease_value))})")


file_output_directory = Path('Analysis')

with open(file_output_directory,"w") as file:

    file.write("Financial Analysis")
    file.write("----------------------------")
    file.write(f"Total Months: {len(tot_months)}")
    file.write(f"Total: ${sum(tot_profit)}")
    file.write(f"Average Change: {round(sum(monthly_profit_change) / len(monthly_profit_change), 2)}")
    file.write(f"Greatest Increase in Profits: {tot_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write(f"Greatest Decrease in Profits: {tot_months[max_decrease_month]} (${(str(max_decrease_value))})")