#Import the libraries needed
import os
import csv

#Establish connection with data source
cvspath_read=os.path.join("Resources","budget_data.csv")
with open(cvspath_read,"r",encoding="UTF-8") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    
    #Define output variables
    profits_greatest_increase=[0,""]
    profits_greatest_decrease=[0,""]
    previous_month=next(csvreader)
    total_profits=int(previous_month[0])
    month_count=1
    sum_of_change=0
    
    #Perform calculations
    for row in csvreader:
        total_profits+=int(row[0])
        month_count+=1
        profits_delta=int(row[0])-int(previous_month[0])
        if int(profits_delta)>int(profits_greatest_increase[0]):
            profits_greatest_increase=[profits_delta,row[1]]
        if int(profits_delta)<int(profits_greatest_decrease[0]):
            profits_greatest_decrease=[profits_delta,row[1]]
        sum_of_change+=profits_delta
        previous_month=row

#Print results
print(f"""
Financial Analysis
-------------------------------
Total Months: {month_count}
Total: ${total_profits}
Average Change: ${round(sum_of_change/(month_count-1),2)}
Greatest Increase in Profits: {profits_greatest_increase[1]} (${profits_greatest_increase[0]})
Greatest Decrease in Profits: {profits_greatest_decrease[1]} (${profits_greatest_decrease[0]})
""")    

#Export Results
cvspath_write=os.path.join("Results.csv")
with open(cvspath_write,"w",newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=",")
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------------"])
    csvwriter.writerow([f"Total Months: {month_count}"])
    csvwriter.writerow([f"Total: ${total_profits}"])
    csvwriter.writerow([f"Average Change: ${round(sum_of_change/(month_count-1),2)}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {profits_greatest_increase[1]} (${profits_greatest_increase[0]})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {profits_greatest_decrease[1]} (${profits_greatest_decrease[0]})"])
