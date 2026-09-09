def ifElse(age=18):
    if age<=13:
        print("You are a minor")
    elif age>=18 and age<60:
        print("You are an adult")
    elif age>13 and age<18:
        print("You are a teenager")
    else:
        print("You are an adult")