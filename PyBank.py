#dependencies
import os
import csv 
budget_csv=os.path.join('..', 'Resources','budget_data.csv')
 #open and read csv
with open(budget_csv,) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",") 
    header = next(csvreader)   
# create lists
    months=[]
    profit_losses=[]
    average_profit=[]
    profit_change=[]
 #assign values to variables
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
#total number of months in dataset
    total_months=len(months)   
#Net total amount of profit
    total_profit=sum(profit_losses)    
#average of profit
    average_profit= total_profit/total_months
#greatest inc in profit/greatest dec in losses
    for i in range(len(profit_losses)-1):
        profit_change.append(profit_losses[i+1]-profit_losses[i])
        greatest_inc= max(profit_change)
        greatest_dec= min(profit_change)

        month_inc=str(months[profit_change.index(max(profit_change))+1])
        month_dec=str(months[profit_change.index(min(profit_change))+1])      
#Print Statements  
    print("Financial Analysis")
    print("--------------------")
    print("the total number of months is :", total_months)
    print("net total profit is:",total_profit)
    print("average profit is:", average_profit)
    print("greatest protfit increase is:", month_inc, greatest_inc)
    print("greatest profit deccrease is:", month_dec, greatest_dec)
   
#designate output file
output_file = "Financial_Analysis.txt"
output_path = os.path.join("Financial_Analysis.txt")
with open(output_file, "w") as text_file:
    
    text_file.write("Financial Analysis\n")
    text_file.write("------------------\n")
    text_file.write("Total Months:" + str(total_months))
    text_file.write("\n")
    text_file.write("Total Profit:" +str(total_profit))
    text_file.write("\n")
    text_file.write("Average Profit:" +str(average_profit))
    text_file.write("\n")
    text_file.write("Greatest Profit inc:" +str(month_inc)+" " + str(greatest_inc))
    text_file.write("\n")  
    text_file.write("Greatest Profit dec:" +str(month_dec)+" " + str(greatest_dec)) 
    

   
    


    