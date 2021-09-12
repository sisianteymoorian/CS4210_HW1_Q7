#-------------------------------------------------------------------------# AUTHOR: #Sisian Teymoorian
# FILENAME: find_s.py
# SPECIFICATION: read  the  filecontact_lens.csv and output the hypothesisof Find-S algorithm
# FOR: CS 4200- Assignment #1
#-----------------------------------------------------------*/
#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv
num_attributes = 4
db = []
print("\n The Given Training Data Set \n")
#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:  
	reader = csv.reader(csvfile)  
	for i, row in enumerate(reader):      
		if i > 0: #skipping the header         
			db.append (row)         
			print(row)
print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)
#find the first positive training data in db and assign it to the vector hypothesis
for row in db:
	if row[-1] =='Yes'
		hypothesis = row[0 : num_attributes]
		break
for row in db:
	if row[-1] == 'Yes':
		for i, value in enumerate(row):
			if i < len(hypothesis) and hypothesis[i] != value:
				hypothesis[i] = '?'
print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)
