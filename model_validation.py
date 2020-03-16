# Werth Consulting Group
# Legal Innovators
# Machine Learning with Personality Test
# Model Validation
# February, March 2020
#
# This function accepts a csv file, with each point consisting of:
# 	(A) A predicted classification
#	(B) Actual classification
# After downloading the data, the program compares the predicted
# classification against the actual classification, and returns
# the percentage of accurate predictions.

# Note: If return value is less than or equal to 0.25, the model
# performs equally to a random model.


#in progress, not working as of now
import csv

#Takes the data from a file, and converts it into a list
#of string values, which will later be converted to float
with open('test.csv') as csv_file:
	reader = csv.reader(csv_file)
	count = 0
	data = []

	for row in reader:
		data.append(row)

print data
accuracy = 0

for i in range(3):
	a = (float(data[i][0]))
	b = (float(data[i][1]))

	if(a / b > .25):
		accuracy+= 1

fin = ((accuracy / len(data)) * 100)
print('Accuracy of model is ' + str(fin) + '%')