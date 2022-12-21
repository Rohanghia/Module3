#import os and csv

import os
import csv

#data path for the csv file
election_csv = os.path.join("C:/Users/RGhia/Desktop/Module3/pypoll", "Resource", "election_data.csv")

#assign variables
total_votes = 0
candidate_name =[]
stockham_votes = 0
degette_votes = 0
doane_votes = 0
unique_list = []

# open the csv file in read mode
with open(election_csv,) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #Skip the first row header
    csv_header = next(csv_reader)

    #read each row of the data after header
    for row in csv_reader:
        print(row[2])

        #calculate total number of votes
        total_votes += 1
        
        #append the total votes for each candidates
        for names in candidate_name:
            if row[2] not in candidate_name:
                candidate_name.append(row[2])
        
        #get votes casted for each candidate
        if row[2] == "Charles Casper Stockham":
            stockham_votes += 1
        elif row[2] == "Diana DeGette":
            degette_votes += 1
        else: 
            doane_votes += 1
           
    #calculate % of votes for each candidate
    stockham_percent = (stockham_votes / total_votes) 
    degette_percent = (degette_votes / total_votes) 
    doane_percent = (doane_votes / total_votes) 

    # to find which candidate won 
    winner = max(stockham_votes,degette_votes,doane_votes)

    if winner == stockham_votes:
        winner_name = "Charles Casper Stockham"
    elif winner == degette_votes:
        winner_name = "Diana DeGette"
    else: 
        winner_name = "Raymon Anthony Doane"

#print analysis
print(f'Election Results')
print(F'-------------------------------------------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------------------------------------------')
print(f'Charles Casper Stokham: {stockham_percent:.2%} (votes:{stockham_votes})')
print(f'Diane DeGette: {degette_percent:.2%} (votes:{degette_votes})')
print(f'Raymon Anthony Doane: {doane_percent:.2%} (votes:{doane_votes})')
print(f'-------------------------------------------------------------')
print(f'Winner is {winner_name} with {winner} votes!')
print(f'-------------------------------------------------------------')

##declaring data path for the output file as txt file
election_analysis = os.path.join("C:/Users/RGhia/Desktop/Module3/pypoll/analysis/election_data_analysis.txt")

#open file and specify to hold the contents
with open(election_analysis, 'w') as analysedfile:
# write new data
    analysedfile.write(f"Election Results\n")
    analysedfile.write(F'---------------------------------------------------------------------------\n')
    analysedfile.write(f'Total Votes: {total_votes}\n')
    analysedfile.write(f'---------------------------------------------------------------------------\n')
    analysedfile.write(f'Charles Casper Stokham: {stockham_percent:.2%} (votes:{stockham_votes})\n')
    analysedfile.write(f'Diane DeGette: {degette_percent:.2%} (votes:{degette_votes})\n')
    analysedfile.write(f'Raymon Anthony Doane: {doane_percent:.2%} (votes:{doane_votes})\n')
    analysedfile.write(f'---------------------------------------------------------------------------\n')
    analysedfile.write(f'Winner is {winner_name} with {winner} votes!\n')
    analysedfile.write(f'---------------------------------------------------------------------------\n')
        
