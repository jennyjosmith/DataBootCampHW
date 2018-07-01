
## import the standard stuff
import csv
import os

# Files
file_data = os.path.join("/Users/Admin/Desktop/budget_data.csv")
file_final = os.path.join("/Users/Admin/Desktop/budget_analysis.csv")

# Trackers for financial results
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
total_net = 0

# Read csv and create dictionaries
with open(file_data) as financial_data:
    reader = csv.reader(financial_data)

  # Read header row. Because we've already read the header row, the for loop
    # below will begin at the second line where the actual data begins.
    header_row = next(reader)

   # identify column indices (i mean, it's easy in this one cuz there are just 2,
# but still...)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
        ## the result of ^^ is that 0 indicates date and 1 indicates profit/loss
    
    # Extract first row to avoid appending to net_change_list, because the first
    # value in the net change list should be the difference between the
    # second row of data and the first row of data, not the first row of data less
    # the header row (no value)
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])



    for row in reader:

        # Calculate total months (# of rows, counter starts at 0)
        # Calculate the total net profit/los
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # Net change. 
        # Extracting all rows with column indices of 1 when we want to call the
        # revenue column and 0 when we want to call the date column.
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Crunch the results
results = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profit/Loss: ${total_net}\n"
    f"Net Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Profit Increase: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Profit Decrease: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Display the results
print(results)

# Export the results to text file
with open(file_final, "w") as txt_file:
    txt_file.write(results)
