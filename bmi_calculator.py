# Creating a BMI calculator using Python

name1 = "Ram"
height_m1 = 4
weight_kg1 = 70

name2 = "Shyam"
height_m2 = 5
weight_kg2 = 80

name3 = "CV Raman"
height_m3 = 3
weight_kg3 = 72

def bmi_calculator(name, height_m, weight_kg):

    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    
    print(bmi)
    if bmi < 20:
        return name + " is not overweight"
    else:
        return name + "It is overweight"
    
result1 = bmi_calculator(name1, height_m1, weight_kg1)
print(result1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
print(result2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)
print(result3)