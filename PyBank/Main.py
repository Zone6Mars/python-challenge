import os
import csv

#set file path where csv file resides
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    #print(f"CSV Header: {csv_header}")

    #create lists that can be filled from the csv and referrenced later
    MonthCount = []
    Profit_loss = []
    Profit_Change = []
    
    # Read each row of data after the header
    #for row in csvreader:
        #print(row)
    
   
    #cycle through each row in the csvfile
    for row in csvreader:
        #add the first column values into a list called "MonthCount"
        MonthCount.append(row[0])
        #convert all values in csv to an integer from the second column
        #and add to the "Profit_loss" list
        Profit_loss.append(int(row[1]))
    
    #cycle through each row in the range of the length of the list "Profit_Change" minus 1
    #to give the number of iterations to calculate
    for i in range(len(Profit_loss)-1):
        #the result of subtracting the value below the 
        #current iteration (i+1) - the current iteration (i)
        #within the "Profit_loss" list is added to the list "Profit_Change" 
        Profit_Change.append(Profit_loss[i+1]-Profit_loss[i])
        
        #print (Profit_Change)

#print(MonthCount)

#Get the largest number in the "Profit_Change" list
LargestIncrease = max(Profit_Change)
#Get the smallest number in the "Profit_Change"
SmallestDecrease = min(Profit_Change)
#print(increase)
#print(decrease)

#find the index within the "Profit_Change" list where the maximum value occured
month_increase = Profit_Change.index(LargestIncrease)+1
#find the index within the "Profit_Change" list where the maximum value occured
month_decrease = Profit_Change.index(SmallestDecrease)+1
#print(month_increase)
#print(month_decrease)

#print "Financial Analysis" within Python
print("Financial Analysis")
#print "-------------------------------" within Python
print("-------------------------------")

#The length of the list "MonthCount" list will tell how many month
#are in the dataset, so we would print the count
print(f"Total Months:{len(MonthCount)}")

#Adding each integer from the list "Profit_loss" would tell
#the overall or total Profit or Loss of the dataset, so we would 
#print the sum
print(f"Total: ${sum(Profit_loss)}")

#Adding each integer from the list "Profit_Change" dividied by
#the length of the list "Profit_Change" would give the Average change 
#in Profit or Loss for the dataset. We woluld sum the "Profit_Change"
#list and divide it by the length of the "Profit_Change" list

#Rounding the data to the second decimal would equate to rounding
#to the nearest whole penny.
print(f"Average Change: {round(sum(Profit_Change)/len(Profit_Change),2)}")

#The index "month_increase" of the "MonthCount" list will return the month
#at that index. The value of the variable "LargestIncrease" will return the amount
#of the Largest Profit Increase
print(f"Greatest Increase in Profits: {MonthCount[month_increase]} (${(str(LargestIncrease))})")

#The index "month_decrease" of the "MonthCount" list will return the month
#at that index. The value of the variable "SmallestDecrease" will return the amount
#of the Largest Profit Loss
print(f"Greatest Decrease in Profits: {MonthCount[month_decrease]} (${(str(SmallestDecrease))})")

# set path for text file
budget_output = os.path.join("Analysis", "BankResults.txt")    
    
# write the results to a text file
with open(budget_output, 'w') as txtfile:
        
        #write "Financial Analysis" within the textfile
        txtfile.write('Financial Analysis')
        
        #write "-------------------------------" within the textfile         
        txtfile.write('\n------------------------------------')
        
        #write the length of the list "MonthCount" because it will tell how many month
        #are in the dataset, so we would write the count to the text file        
        txtfile.write(f"\nTotal Months:{len(MonthCount)}")
        
        #Adding each integer from the list "Profit_loss" would tell
        #the overall or total Profit or Loss of the dataset, so we would 
        #write the sum to the text file
        txtfile.write(f"\nTotal: ${sum(Profit_loss)}")
        
        #Adding each integer from the list "Profit_Change" dividied by
        #the length of the list "Profit_Change" would give the Average change 
        #in Profit or Loss for the dataset. We woluld sum the "Profit_Change"
        #list and divide it by the length of the "Profit_Change" list

        #Rounding the data to the second decimal would equate to rounding
        #to the nearest whole penny.  Write the calculation to the textfile
        txtfile.write(f"\nAverage Change: {round(sum(Profit_Change)/len(Profit_Change),2)}")

        #The index "month_increase" of the "MonthCount" list will return the month
        #at that index. The value of the variable "LargestIncrease" will return the amount
        #of the Largest Profit Increase. write the month and amount to the text file        
        txtfile.write(f"\nGreatest Increase in Profits: {MonthCount[month_increase]} (${(str(LargestIncrease))})")
        
        #The index "month_decrease" of the "MonthCount" list will return the month
        #at that index. The value of the variable "SmallestDecrease" will return the amount
        #of the Largest Profit Loss. write the month and the amoun to the text file
        txtfile.write(f"\nGreatest Decrease in Profits: {MonthCount[month_decrease]} (${(str(SmallestDecrease))})")
