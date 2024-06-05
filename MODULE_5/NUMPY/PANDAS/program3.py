'''Given a file “auto.csv” of automobile data with the fields
index, company,body-style, wheel- base, length, engine-type,
num-of-cylinders, horsepower,average-mileage, and price,
write Python codes using Pandas to
1. Print total cars of all companies
2. Find the average mileage of all companies
3. Find the highest priced car of all companies'''

import numpy as np
import pandas as pd
import csv

data = pd.read_csv('auto.csv')
total_cars = len(data)
print(f"TOTAL CARS = {total_cars}")

avg_mileage = data["average-mileage"].mean()
print(f"AVERAGE MILEAGE = {avg_mileage}")

highest_priced_car = data["price"].idxmax()
car = data.loc[highest_priced_car]
print(f"{car['company']} {car['body-style']} IS THE HIGHEST PRICED CAR")

arr1 = np.arange(6).reshape((3, 2))
print(arr1)
arr2 = np.arange(6).reshape((3,2))
print(arr2)
arr3 = arr2[0].reshape((1, 2))
print(arr3)
arr4 = arr1 + arr3
print(arr4)
