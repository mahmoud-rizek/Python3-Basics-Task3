
h = int(input("Enter your height: "))
w = int(input("Enter your width: "))

bmi = w / (h*h)

if bmi > 0 :
    if bmi <= 16 :
        print("you are very underweight")
    elif bmi <= 18.5:
        print("you are underweight")
    elif bmi <= 25:
        print("Congratolat! you are Healthy")
    elif bmi <= 30:
        print("you are overweight")
    else:
        print("you are very overweight")

else:
    print("Enter valid data")