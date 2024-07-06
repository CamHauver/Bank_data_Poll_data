# Bank_data_Poll_data
Two separate python scripts that analyze 1) bank financial data and 2) election poll data

# Bank_script
# PyBank: Bank data
#Dependencies
import os
import csv

#File to load and output
budget_data_csv = os.path.join(".", "Resources", "budget_data.csv")
budget_analysis_results = os.path.join(".","analysis", "budget_analysis_results")

#define variables  
total_months = 1
net_profit_loss = 0
net_change_list = []
monthly_change_list = []
greatest_monthly_increase = ["", 0]
greatest_monthly_decrease = ["", 999999999999999]


#Read in the CSV file, convert it into a list, loop through the data
with open(budget_data_csv, 'r') as csv_file:
  
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csv_reader)

    first_row = next(csv_reader)
    net_profit_loss += int(first_row[1])
    previous_profit_loss = int(first_row[1])
    
   
    for row in csv_reader:
        
        #calculate the total number of months included in the dataset ("Total Months:")
        total_months += 1
        
        #calculate the net total amount of "Profit/Losses" over the entire period ("Total: $")
        net_profit_loss += int(row[1])
        
        #calculate the average of the "Profit/Losses" changes over the entire period ("Average Change: +/- $")
        net_change = int(row[1]) - previous_profit_loss
        previous_profit_loss = int(row[1])
        net_change_list.append(net_change)
        
        #The greatest increase in profits (date and amount) over the entire period ("Greatest Increase in Profits: date (+/-$"))
        if (net_change > greatest_monthly_increase[1]):
            greatest_monthly_increase[0] = row[0]
            greatest_monthly_increase[1] = net_change

        #The greatest decrease in profits (date and amount) over the entire period
        if (net_change < greatest_monthly_decrease[1]):
            greatest_monthly_decrease[0] = row[0]
            greatest_monthly_decrease[1] = net_change   
            
average_change = sum(net_change_list)/len(net_change_list)
        
financial_analysis_summary = (
    f"Financial Analysis\n"
    f"\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_monthly_increase[0]} (${greatest_monthly_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_monthly_decrease[0]} (${greatest_monthly_decrease[1]})\n"
)
#Print the entire analysis to the terminal
print(financial_analysis_summary)

#export a text file with the results
with open(budget_analysis_results, "w") as txt_file:
    txt_file.write(financial_analysis_summary)

#GOAL

#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)


# Poll-script
# PyPoll: Election data
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

#Summarize election results:
election_results = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
)

#Print analysis to the terminal (part 1: total votes)
print(election_results)

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