import csv 

with open("data.csv",'r') as file:
	reader = csv.reader(file) 

	Total=0
	count=0
	highest=0
	highest_name=""
	for row in reader:
             Total=Total + int(row[1])
             count=count + 1
             current_marks=int(row[1])
             current_name=row[0]
             if current_marks > highest:
                     highest=current_marks
                     highest_name=current_name

             print(row) 

average=Total/count
print({"average marks": average})
print({"highest marks": highest, "name of student with highest marks": highest_name})