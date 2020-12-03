import json
import csv

#open json file and load the data into a variable
with open('crimes.json') as f:
	data = json.load(f)

#delete enhancers and description data
for item in data:
	del item['enhancers']
	del item['outcomeDescription']
	del item['meritCrimeSuccess']
	del item['hackingSuccessEdu']
	del item['fedJudge']
	del item['psychBachelor']
	del item['created']
	del item['factionCEBonus']
	del item['playerID']
	del item['updated']

#indent json data for easier reading
with open('new_crimes.json','w') as f:
	json.dump(data,f,indent=2,sort_keys=True)

#open sorted new crimes json file
with open('new_crimes.json') as f:
	data = json.load(f)

#open a file for writing as csv
data_file = open('crimes.csv','w', newline='')

#create csv writer object
csv_writer = csv.writer(data_file)

#create a counter variable to help write headers into CSV file
count = 0

for item in data:
	if count == 0:
		
		#get and write headers to csv file
		header = item.keys()
		csv_writer.writerow(header)
		count += 1

	#write data to csv file
	csv_writer.writerow(item.values())

data_file.close()
	#print(item['id'],item['group'],item['category'],item['crime'],item['outcome'],item['status'],item['gainingType'],item['gainings'],item['nerveUsed'],item['nnb'])
