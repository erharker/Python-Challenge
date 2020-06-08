#dependencies
import os
import csv 
election_data=os.path.join('..', 'Resources','election_data.csv')
 #open and read csv
with open(election_data) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",") 
    header = next(csvreader)
    print(header)  
#Create variables for candidates
    candidate1 = "Khan" 
    candidate2 = "Correy"
    candidate3 = "Li"
    candidate4 = "O'Tooley" 
 #Define Starting number of votes for each candidate
    votes1 = 0
    votes2 = 0
    votes3 = 0
    votes4 = 0  
#Loop through rows to count votes for each candidate 
    for row in csvreader:
        if row[2] == candidate1:
            votes1 = votes1 + 1
        elif row[2] == candidate2:
            votes2 = votes2 + 1
        elif row[2] == candidate3:
            votes3 = votes3 + 1
        elif row[2] == candidate4:
            votes4 = votes4 + 1    
#count total votes
totalvotes=votes1+votes2+votes3+votes4
#Calculate percent of votes won
candidate1_percentage = round((votes1/totalvotes)*100)
candidate2_percentage = round((votes2/totalvotes)*100)
candidate3_percentage = round((votes3/totalvotes)*100)
candidate4_percentage = round((votes4/totalvotes)*100)

#Print election results
print("Election Results")
print("-----------------------")
print("total votes:", totalvotes)
print("Khan:", candidate1_percentage,"%", votes1)
print("Correy:", candidate2_percentage,"%", votes2)
print("Li:", candidate3_percentage,"%", votes3)
print("O'Tooley:", candidate3_percentage, "%", votes4)
print("-----------------------")

#Determine Election winner 
if votes1 > votes2 and votes1 > votes3 and votes1 > votes4:
    print("Winner: Khan")
elif votes2 > votes1 and votes2 > votes3 and votes2 > votes4:
    print("Winner: Correy")
elif votes3 > votes1 and votes3 > votes2 and votes3 > votes4:
    print("Winner: Li")
elif votes4 > votes1 and votes4 > votes2 and votes4 > votes3:
    print("Winner: OTooley")
    
#print to text file
output_file = "Poll_Analysis.txt"
output_path = os.path.join("Poll_Analysis.txt")
with open(output_file, "w") as text_file:   
    text_file.write("Poll Analysis\n")
    text_file.write("------------------\n")
    text_file.write("total votes:"+ str(totalvotes))
    text_file.write("\n")
    text_file.write("Khan:"+ " "+ str(candidate1_percentage)+ "%" + " "+ str(votes1))
    text_file.write("\n")
    text_file.write("Correy:"+ " "+ str(candidate2_percentage)+ "%" + " " + str(votes2))
    text_file.write("\n")
    text_file.write("Li:"+ " " + str(candidate3_percentage)+"%" + " " + str(votes3))
    text_file.write("\n")
    text_file.write("O'Tooley:"+ " " + str(candidate3_percentage)+ "%" + " " + str(votes4))
    text_file.write("\n")
    text_file.write("-----------------------")
    text_file.write("\n")
    text_file.write("Winner: Khan")
