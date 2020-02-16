import os
import csv

cvspath=os.path.join("Resources","houston_election_data.csv")

with open(cvspath,"r") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    for row in csvreader:
        print(row)
        if row==5: break