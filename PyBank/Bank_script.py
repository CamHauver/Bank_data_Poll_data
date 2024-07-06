#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[3]:


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


# In[4]:


#export a text file with the results
with open(budget_analysis_results, "w") as txt_file:
    txt_file.write(financial_analysis_summary)


# In[5]:


#GOAL

#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)

