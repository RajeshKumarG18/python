import sys

data_set = []
with open("life-expectancy(2).csv") as data_file:
    for line in data_file:
        if line.startswith("Entity"): continue;
        
        row = line.split(",")
        row[2] = int(row[2]) # convert year to integer
        row[3] = float(row[3]) # convert life expectancy to float
        data_set.append(row)
        
# min max life expectancy
min_exp = 1000
min_year = None
min_country = None

for i in data_set:
    if i[3] < min_exp:
        min_exp = i[3]
        min_year = [2]
        min_country = [0]
        
max_exp = 0
max_year = None
max_country = None

for i in data_set:
    if i[3] > max_exp:
        max_exp = i[3]
        max_year = [2]
        max_country = [0]
        
print(f"{max_country} in {max_year} has the highest of {max_exp}")
print(f"{min_country} in {min_year} has the lowest of {min_exp}")

input_year = int(input("what year would you like to look at {1950-2019}? "))

if input_year < 1950 or input_year > 2019:
    print("year out of range")
    sys.exit()

year_list = [i for i in data_set if i[2] == input_year]        

min_exp = 1000
min_year = None
min_country = None
for i in year_list:
    if i[3] < min_exp:
        min_exp = i[3]
        min_country = i[0]
        
max_exp = 0
max_year = None
max_country = None
total_sum = 0

for i in year_list:
    total_sum += i[3]
    if i[3] > max_exp:
        max_exp = i[3]
        max_country = i[0]

average = total_sum / len(year_list)       
print()
print(f"for the year {input_year}:")
print(f"The average life expectancy across all countries was {average:.2f}")
print(f"In {input_year}, {max_country} had the highest life expectancy of {max_exp}")
print(f"In {input_year}, {min_country} had the lowest life expectancy of {min_exp}")  

