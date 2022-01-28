import os
import csv


csvpath = os.path.join("Resources","budget_data.csv")
   
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    num_months=0
    profit_loss=0
    net_total=0
    current_month = []
    current_profit_list = []
    max_profit = []
    min_profit = []

    for row in csvreader:

        num_months = num_months + 1 
        profit_loss = float(profit_loss) + float(row[1])

print("Total Months: " + str(num_months))
print("Total: $" + str(profit_loss))
avg_chg = float(profit_loss) / float(num_months)
print("Average Change: $" + str(avg_chg))


