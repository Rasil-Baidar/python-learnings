def lesson_for_loops():
    stringVal = "Hello, World!"
    print(f"Lopping through a string {stringVal}")
    for index,str in enumerate(stringVal):
        print(f"Character: {str} at index {index}")
    
    listVals = [1,2,3,4,5]
    print(f"Lopping through a list {listVals}")
    for listVal in listVals:
        if(listVal==1):
            continue
        print(f"Number: {listVal}")
    
    dictVal = {"name":"Rasil", "age":20, "city":"Sydney"}

    for key in dictVal:
        print(f"Key: {key}")

    for key,val in dictVal.items():
        print(f"Key: {key} Value: {val}")

    names = ["Alice", "Bob", "Charlie"]
    scores = [90, 75, 82]
    for name,score in zip(names,scores):
        print(f"Name: {name} Score: {score}")
 
