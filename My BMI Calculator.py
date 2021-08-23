print("welcome to my BMI calculator!\n\n\n")
#prompt for inputs
weight = int(input("Enter your weight in pounds.\n"))
heightft = float(input("Enter your height (feet).\n"))
heightin = float(input("Enter your height (inches).\n"))
#convert feet to inches
height = heightft*12 + heightin
#convert to BMI
BMI = (weight/(height**2))*703.0695
#compute BMI to find group
if BMI < 18.5:
    print("go eat some food.\n(underweight)")
elif BMI >= 18.5 and BMI < 25:
    print("your lookin good. ;)\n(normalweight)")
elif BMI >= 25 and BMI < 30:
    print("lay off the chips.\n(Overweight)")
else:
    print("get your ass off the couch.\n(Obese)")
