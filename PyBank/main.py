
#Dependencies
import os
import csv

#Variables
months = []
profit_loss = []
total_profit = []


#File Path
csvpath = os.path.join('/Users/sheshie/Documents/Bootcamp/Homework/python-challenge/PyBank/Resources/budget_data.csv')



with open(csvpath, newline= '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)
    

    for row in csvreader:

        months.append(row[0])
        total_profit.append(int(row[1]))
        

    for i in range(len(total_profit)-1):
        profit_loss.append(total_profit[i+1]-total_profit[i])

increase = max(profit_loss)
decrease = min(profit_loss)

monthly_increase = profit_loss.index(max(profit_loss))+1
monthly_decrease = profit_loss.index(min(profit_loss))+1


    

#Analysis

print (f"Financial Analysis")
print(f"-------------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(profit_loss)/len(profit_loss),2)}")
print(f"Greatest Increase in Profits: {months[monthly_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {months[monthly_decrease]} (${(str(decrease))})")



#Txt Format
with open("pybank.txt", "w") as text:
    text.write(f"Financial Analysis")
    text.write(f"-------------------------------")
    text.write(f"Total Months:{len(months)}")
    text.write(f"Total: ${sum(total_profit)}")
    text.write(f"Average Change: ${round(sum(profit_loss)/len(profit_loss),2)}")
    text.write(f"Greatest Increase in Profits: {months[monthly_increase]} (${(str(increase))})")
    text.write(f"Greatest Decrease in Profits: {months[monthly_decrease]} (${(str(decrease))})")




