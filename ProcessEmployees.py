"""
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
"""

import csv

# open the file

employees = open("employee_data.csv", "r")
employee_file = csv.reader(employees, delimiter=",")
next(employee_file)


# create an empty dictionary

new_employee = {}

# use a loop to iterate through the csv file
for record in employee_file:
    if record[9] == "TS":
        new_salary = float(record[5]) * 1.10
        name = f"{record[1]} {record[2]}"
        new_employee[name] = new_salary 
        print( print(f'Employee Name: {name} Current Salary: {record[9]}')
        for key,value in new_employee[name].items():
            print("=========================================")
            print(f'Employee Name: {key} New Salary: {value}')

    # check if the employee fits the search criteria


print( print(f'Employee Name: {name} Current Salary: {record[9]}')
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per image


print()
print("=========================================")
print()

# print out the total difference between the old salary and the new salary as per image.
