height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = round(weight / height ** 2)
if BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("normal weight")
elif BMI < 30:
    print("overweight")
elif BMI < 35:
    print("obese")
else:
    print("clinically obese")