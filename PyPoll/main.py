import os
import csv

#Variables
total_votes = 0
candidates_votes = {}
winner_votes = 0
percentage_votes = {}


#Filepath
csvpath = os.path.join('/Users/sheshie/Documents/Bootcamp/Homework/python-challenge/PyPoll/Resources/election_data.csv')

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    for row in csvreader:

        total_votes = total_votes + 1

        if row[2] in candidates_votes:
            candidates_votes[row[2]] += 1
        else:
            candidates_votes[row[2]] = 1
        


for key, value in candidates_votes.items():
    percentage_votes[key] =round((value/total_votes)* 100 , 3)
            
        
    if percentage_votes[key] > winner_votes:
          winner_votes = candidates_votes[key]
          winner = key
        
        

 
#Analysis
print(f"Election Results")
print(f"--------------------------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------------------")
for key, value in candidates_votes.items():
    print(key, ':' , str(percentage_votes[key]),'%',' ','(',candidates_votes[key],')')
print(f"--------------------------------")
print(f"Winner: {winner}")
print(f"--------------------------------")

#Txt Format
with open("pypoll.txt", "w") as text:
    text.write(f"Election Results")
    text.write(f"--------------------------------")
    text.write(f"Total Votes: {total_votes}")
    text.write(f"--------------------------------")
    for key, value in candidates_votes.items():
        text.write(key, ':' , str(percentage_votes[key]),'%',' ','(',candidates_votes[key],')')
    text.write(f"--------------------------------")
    text.write(f"Winner: {winner}")
    text.write(f"--------------------------------")