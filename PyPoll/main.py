import csv

#starting values 
TotalVotes = 0
Candidates = []
VotesForCanadate = []

#to read and open the csv file 
with open('Resources/election_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#loop through the rows     
    for i, row in enumerate(reader):
# != means isnt equal to         
        if i != 0:
            TotalVotes += 1
            Candidate = row[0].split(',')[2]
 #if the candidate is in the candiadates list            
            if Candidate in Candidates:
                NumOfVotes = VotesForCanadate[Candidates.index(Candidate)]
                NumOfVotes += 1
                VotesForCanadate[Candidates.index(Candidate)] = NumOfVotes
 #if the candidate isnt already in the list add them                
            else:
                Candidates.append(Candidate)
                VotesForCanadate.append(1)
                
#prints the results 
print('Election Results\n-------------------------')
print(f'Total Votes: {TotalVotes}')
print('-------------------------')
for Candidate in Candidates:
#calaculates the percentage     
    print(f'{Candidate}: {round((VotesForCanadate[Candidates.index(Candidate)] / TotalVotes) * 100, 3)}% ({VotesForCanadate[Candidates.index(Candidate)]})')
print('-------------------------')
#pulls the biggest value for the winner 
print(f'Winner: {Candidates[VotesForCanadate.index(max(VotesForCanadate))]}')
print('-------------------------')

#write to txt file
Analysis = open("analysis/ElectionResults.txt", "w+")
Analysis.write('Election Results\n-------------------------\n')
Analysis.write(f'Total Votes: {TotalVotes}\n')
Analysis.write('-------------------------\n')
for Candidate in Candidates:  
    Analysis.write(f'{Candidate}: {round((VotesForCanadate[Candidates.index(Candidate)] / TotalVotes) * 100, 3)}% ({VotesForCanadate[Candidates.index(Candidate)]})\n')
Analysis.write('-------------------------\n')
Analysis.write(f'Winner: {Candidates[VotesForCanadate.index(max(VotesForCanadate))]}\n')
print('-------------------------')
Analysis.close()