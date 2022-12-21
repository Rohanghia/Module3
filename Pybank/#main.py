#import os and csv

import os
import csv

#data path for the csv file
budget_csv = os.path.join("C:/Users/RGhia/Desktop/Module3/pybank","Resources", "budget_data.csv")

#create variables
total_months = 0
total_amount = 0
highest_increase = 0
highest_decrease = 0
monthly_change = []
month_of_change = []
highest_increase_month = 0
highest_decrease_month = 0

#read = open(budget_csv, "r")
#read.close()

#open the the file
with open(budget_csv, "r") as read:
    csv_read=csv.reader(read, delimiter=",")
    #read the header of first row
    csv_header = next(csv_read)
    first_row = next(csv_read)

    #calculate total number of months
    total_months = total_months + 1
    
    #calculate total profit and loss
    total_amount = total_months + int(first_row[1])
    previous_amount = int(first_row[1])

    # read through header on each row
    for row in csv_read:
        # total number of months
        total_months = total_months + 1

        #calculate profit and loss for entire period
        total_amount = total_amount + int(first_row[1])

        #calculate changes to final change/previous change and append monthly change
        final_change = int(row[1]) - previous_amount
        previous_amount = int(row[1])
        monthly_change.append(final_change)
        month_of_change.append(row[0])

        # calculate highest_increase
        if final_change > highest_increase:
            highest_increase = final_change
            highest_increase_month = row[0]

        # calculate highest_decrease
        if final_change < highest_decrease:
            highest_decrease = final_change
            highest_decrease_month = row[0]

    #calculate the average
    monthly_average_change = sum(monthly_change)/ len(monthly_change)

    #print analysis
    print(f'Financial analysis')
    print(f'---------------------------')
    print(f'Total Months:{total_months}')
    print(f'total:${total_amount}')
    print(f'Average Change: ${monthly_average_change:.2f}')
    print(f'Greatest Incease in Profits:, {highest_increase_month},(${highest_increase})')
    print(f'Greatest Decrease in Profits:,{highest_decrease_month},(${highest_decrease})')

#declaring data path for the output file as txt file
budget_analysis = os.path.join("C:/Users/RGhia/Desktop/Module3/pybank/analysis/budget_data_analysis.txt")

#open file and specify to hold the contents
with open(budget_analysis, 'w') as analysedfile:
# write new data
    analysedfile.write(f"Financial Analysis\n")
    analysedfile.write(f"---------------------------\n")
    analysedfile.write(f"Total Months: {total_months}\n")
    analysedfile.write(f"Total: ${total_amount}\n")
    analysedfile.write(f"Average Change: ${monthly_average_change:.2f}\n")
    analysedfile.write(f"Greatest Increase in Profits: {highest_increase_month}, (${highest_increase})\n")
    analysedfile.write(f"Greatest Decrease in Profits: {highest_decrease_month}, (${highest_decrease})\n")