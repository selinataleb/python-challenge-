import os
import csv

# Define the file
csvpath = "PyBank/Resources/budget_data.csv"

# define variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = None
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  

    for row in csvreader:
     
        date = row[0]
        profit_loss = int(row[1])

        # Calculate the total months and total profit/losses
        total_months += 1
        total_profit_losses += profit_loss

        if previous_profit_loss is not None:
            # Calculate the change from the previous month
            change = profit_loss - previous_profit_loss
            changes.append(change)

            # Condition for the greatest increase and decrease
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]

        # Update the previous profit/loss
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else 0

# Print the analysis to the terminal
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
print(output)

# Write the results to a text file
output_path = "PyBank/Analysis"

# Check if PyBank/Analysis is a file
if os.path.isfile(output_path):
    print(f"Error: {output_path} is a file, not a directory.")
else:
    os.makedirs(output_path, exist_ok=True)  # Ensure the directory exists

    # Write the output summary to a text file
    output_file = os.path.join(output_path, 'analysis.txt')  # Add file extension
    with open(output_file, 'w') as txtfile:
        txtfile.write(output)
