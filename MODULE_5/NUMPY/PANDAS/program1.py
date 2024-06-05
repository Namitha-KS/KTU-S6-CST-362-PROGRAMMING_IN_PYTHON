'''Consider a CSV file ‘employee.csv’ with the following
columns(name, gender, start_date ,salary, team)
Write commands to do the following using panda library.
1. print first 7 records from employees file
2. print all employee names in alphabetical order
3. find the name of the employee with highest salary
4. list the names of male employees
5. Display to which all teams employees belong'''

import pandas as pd
import csv

data = pd.read_csv('employee.csv')
print(data.head(7))

name = (data.sort_values(by="name")["name"])
print(name)

highest_salary = data["salary"].idxmax()
employee = data.loc[highest_salary]
print(f'EMPLOYEE WITH HIGHEST SALARY {employee["name"]} {employee["salary"]}')

male_employees = data[data["gender"] == "M"]["name"]
print(male_employees)

unique_teams = data["team"].unique()
print(unique_teams)