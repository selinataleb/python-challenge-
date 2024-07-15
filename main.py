import os
import csv

# Define the file
csvpath = "PyPoll/Resources/election_data.csv"

# define variables
total_votes = 0
candidate_votes = {}

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        # Extract the data
        total_votes += 1
        candidate = row[2]

        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# Calculate the winner and percentages
winner = ""
winning_count = 0
results = []

for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    if votes > winning_count:
        winning_count = votes
        winner = candidate

# Print to terminal
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)
output += '\n'.join(results)
output += (
    f"\n-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)
print(output)

# Write the results to a text file
output_path = "PyPoll/Analysis"
with open(output_path, 'w') as txtfile:
    txtfile.write(output)
