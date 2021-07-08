import os
import csv

# set a csv file path for the data
poll_csv = os.path.join('Resources','election_data.csv')

# define function that will calculate Election Results from
# data that is in the same format as the csv file
def election_results(election_data):

    # set the number of Vote Counts to zero
    # for a fresh count that is not using residual
    # data from a previous run
    VoteTotalCount = 0
    
    # create a list that that will contain
    # each vote for the candidate
    votes = []
    
    
    CandidateTally = []
    
    
    # create a list that will contain only unique
    # values of Candidate names.
    IndividualCandidates = []
    
    percent = []
     
    # using a for loop, cycle through each row contained in the loaded dataset
    for row in election_data:

        # implement a counter 
        # to count the total number of votes
        VoteTotalCount += 1

        # create a list of each unique name each time it
        # appears in the loaded dataset
        if row[2] not in IndividualCandidates:
            IndividualCandidates.append(row[2])

        #print last row of IndividualCandidates to verify data
        #print(IndividualCandidates[-1])
        
        # make a list of all the votes that were looped 
        # through in the loaded dataset.
        votes.append(row[2])
        
        #print last row of votes list to verify data
        #print(votes[-1])
        
    # add a second loop that will cycle through
    # each iteration (or Candidate) in
    # the IndividualCandidates list 
    for i in IndividualCandidates:
        # add the count of each iteration or candidate from the Votes list
        # to the CandidateTally list
        CandidateTally.append(votes.count(i))
        
        #print last row of CandidateTally to verify data
        #print(CandidateTally[-1])
        
        # the count of votes divided by the total amount of votes
        # would yield the win percentage
        # since this formula is within a for loop and nested within
        # an .append method, each iteration or candidate will have
        # a percentage calculated and added to the list Percent.
        percent.append(round(votes.count(i)/VoteTotalCount*100,3))
        
        #print the last row to verify calculations add to 100
        #print(percent[-1])

    # find the winner using index position of 
    # MaxTally within the CandidateTally list
    MaxTally = max(CandidateTally)
    
    # set winner to the candidate who's index locaition
    # matches within the CandidateTally
    # The name from the IndividaulCandidates list will be displayed based
    # on the index value
    winner = IndividualCandidates[CandidateTally.index(MaxTally)]
    
    # print results
    #print "Election Resulsts" within Python
    print('Election Results')
    
    #print "-------------------------------" within Python
    print('--------------------------------')
    
    #print the value of the Vote counter that was implemented
    print(f'Total Votes: {VoteTotalCount}')
    
    #print "-------------------------------" within Python
    print('--------------------------------')
    
    # loop through each iteration (or Candidate) in the range
    # of the length of the list IndividualCandidates
    for i in range(len(IndividualCandidates)):
        # print each iteration (or Candidate), percent
        # and CandidateTally based on the index position of the iteration
        print(f'{IndividualCandidates[i]}: {percent[i]}% {CandidateTally[i]}')
    
    #print "-------------------------------" within Python
    print('--------------------------------')
    
    #print the winner based on the index of the MaxTally
    print(f'Winner: {winner}')
    
    #print "-------------------------------" within Python    
    print('--------------------------------')

    
    
    # set path for text file
    election_results_output = os.path.join("Analysis","ElectionResulsts.txt")

    # write out results to text file
    with open(election_results_output, "w") as txtfile:
        
        #write "Election Resulsts" within the textfile
        txtfile.write('Election Results')
        
        #write "-------------------------------" within the textfile
        txtfile.write('\n------------------------------------')
        
        #write the value of the Vote counter that was implemented within the text file    
        txtfile.write(f'\nTotal Votes: {VoteTotalCount}')
        
        #write "-------------------------------" within the textfile        
        txtfile.write('\n------------------------------------')
        
        # loop through each iteration (or Candidate) in the range
        # of the length of the list IndividualCandidates        
        for i in range (len(IndividualCandidates)):
            
            # write each iteration (or Candidate), percent
            # and CandidateTally based on the index position of the iteration 
            # to the text file             
            txtfile.write(f'\n{IndividualCandidates[i]}: {percent[i]}% {CandidateTally[i]}')

        # write "-------------------------------" within the textfile            
        txtfile.write('\n------------------------------------')
        
        # write the winner based on the index of the MaxTally        
        txtfile.write(f'\nWinner: {winner}')
        
        # write "-------------------------------" within the textfile
        txtfile.write('\n------------------------------------')


# read in the CSV file
with open(poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # adjust for header
    csv_header = next(csvfile)
    
    # use function
    election_results(csvreader) 
