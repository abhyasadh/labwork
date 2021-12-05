#BMI
height=float(input("Enter your height (in metre): "))
weight=float(input("Enter your weight (in kg): "))
bmi=weight/(height**2)
print("BMI: {} kg/m\u00b2".format(bmi))