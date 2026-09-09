def ifElse(age=18):
    if age<=13:
        print("You are a minor")
    elif age>=18 and age<60:
        print("You are an adult")
    elif age>13 and age<18:
        print("You are a teenager")
    else:
        print("You are an adult")
    print("--------------------------------\n")
    status = "adult" if age>=18 else "minor"
    print(f"Status: {status}")

def isPositive(num):
    status = "positive" if num>=0 else "negative"
    print(f"Number {num} is {status}")

def isEven(num):
    status = 'even' if num%2==0 else 'odd'
    print(f"Number {num} is {status}")