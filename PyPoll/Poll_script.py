#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dependencies
import os
import csv

election_data_csv = os.path.join(".", "Resources", "election_data.csv")

#Columns 1-3: "Voter ID", "County", "Candidate"

#define variables
total_votes = 0

candidate_votes = {}
candidates = []

winner_vote_count = 0


# In[2]:


#Open and read the CSV file
with open(election_data_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #store the header row
    csv_header = next(csv_file)

    for row in csv_reader:
        
        #Calculate the total number of votes cast
        total_votes += 1

        #Generate a complete list of candidates who received votes
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
        
        #Calculate the total number of votes each candidate won
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1


# In[3]:


#Summarize election results:
election_results = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
)


# In[4]:


#Print analysis to the terminal (part 1: total votes)
print(election_results)


# In[5]:


#Export a text file with the analysis results
election_analysis_results = os.path.join(".", "analysis","election_analysis_results.txt")

with open(election_analysis_results, "w") as txt_file:
    #Write into text file (part 1: total votes)
    txt_file.write(election_results)
    
        #Calculate the percentage of votes each candidate won        
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]

        vote_percentage = float(votes / total_votes) * 100

        #The winner of the election based on popular vote
        if (votes > winner_vote_count):
            winner_vote_count = votes
            winning_candidate = candidate

        #Print analysis to the terminal (part 2: each candidate's results)
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results)
        
        #Write into text file (part 2: each candidate's results)
        txt_file.write(candidate_results)
            
    #Print analysis to the terminal (part 3: Winning candidate results)
    winning_candidate_results = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"----------------------------\n"
    )
    print(winning_candidate_results)

    #Write into text file (part 3: Winning candidate results)
    txt_file.write(winning_candidate_results)


# In[ ]:


#GOAL

#Election Results
#-------------------------
#Total Votes: 369711
#-------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#Winner: Diana DeGette
#-------------------------

