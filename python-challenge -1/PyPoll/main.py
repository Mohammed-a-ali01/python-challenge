import os
import csv
from pathlib import Path

# Our file path
csv_file_path = Path('C:/Users/Moham/IdeaProjects/python-challenge/PyPoll/Resources/election_data.csv')

# Declare Variables
tot_votes = 0
Charles_votes = 0
Diana_votes = 0
Raymon_votes = 0

# Default CSV mode
with open(csv_file_path, newline="", encoding="utf-8") as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections, delimiter=",")

    header = next(csvreader)

    for row in csvreader:

        # count id
        tot_votes += 1

        # Count/verify each candidate
        if row[2] == "Charles Casper Stockham":
            Charles_votes += 1
        elif row[2] == "Diana DeGette":
            Diana_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_votes += 1

# Create dict to find winner, since there are only three individuals we can sort as follows
candidates = ["Charles", "Diana",  "Raymon"]
votes = [Charles_votes, Diana_votes, Raymon_votes]

# Winner using a dictionary
dict_candidates_and_votes = dict(zip(candidates, votes))
Candidate_key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Show the percentage of each candidate
Charles_percentage = (Charles_votes / tot_votes) * 100
Diana_percentage = (Diana_votes / tot_votes) * 100
Raymon_percentage = (Raymon_votes / tot_votes) * 100

output_file = Path('Analysis')

# Results to be shown and include three decimal places.
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {tot_votes}")
print(f"----------------------------")
print(f"Charles: {Charles_percentage:.3f}% ({Charles_votes})")
print(f"Diana: {Diana_percentage:.3f}% ({Diana_votes})")
print(f"Raymon: {Raymon_percentage:.3f}% ({Raymon_votes})")
print(f"----------------------------")
print(f"Winner: {Candidate_key}")
print(f"-----------")

# Ultimately results should look identical to output provided on Module 3
# This step is completely redundant but needs to be done for the criteria
output_file = Path('Analysis', 'election_results.txt')
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {tot_votes}\n")
    file.write("----------------------------\n")
    file.write(f"Charles Casper Stockham: {Charles_percentage:.2f}% ({Charles_votes})\n")
    file.write(f"Diana DeGette: {Diana_percentage:.2f}% ({Diana_votes})\n")
    file.write(f"Raymon Anthony Doane: {Raymon_percentage:.2f}% ({Raymon_votes})\n")
    file.write("----------------------------\n")
    file.write(f"Winner: {Candidate_key}\n")
    file.write("----------------------------\n")