import os
import csv

#set path
electiondata_csv = "/Users/mayraterrazas/UCI-Folder/python-challenge/PyPoll/Resources/election_data.csv"

# Variables & lists
total_votes = 0
candidate_options = []
candidate_votes = {}
winner = ""
winner_count = 0

#read and open csv
with open(electiondata_csv, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # skip header
    csv_header = next(csv_file)

    #loops
    for row in csv_reader:
        
        #total votes and candidates
        total_votes = total_votes + 1
        candidate_name  = row[2]
        
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
        
        #Add up votes
        candidate_votes[candidate_name] = candidate_votes[candidate_name] +1

    #elected winner 
    for candidate in candidate_votes:
        
        votes = candidate_votes.get(candidate)
        vote_percentage = (votes/total_votes) * 100
        
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
            
        voter_counts = f"{candidate}: {vote_percentage}%({votes})"
        print(voter_counts)

#output path
output_file = os.path.join("/Users/mayraterrazas/UCI-Folder/python-challenge/PyPoll/analysis/election_results.txt")

#output data        
with open(output_file, 'w') as file:
    
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"{voter_counts}")
    file.write("\n")
    file.write("----------------------------") 
    file.write("\n") 
    file.write(f"Winner: {winner_count}")
    file.write("\n")
    file.write("----------------------------")
    
print("Election Results")
print("\n")
print("-------------------------")
print("\n")
print(f"Total Votes: {total_votes}")
print("\n")
print("-------------------------")
print("\n")
print(f"{voter_counts}")
print("\n")
print("-------------------------")
print("\n")
print(f"Winner: {winner}")
print("\n")
print("-------------------------")