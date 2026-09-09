def lesson_while_loop():
    count = 0
    while count < 10:
        print(f"Count: {count}")
        count+=1
    print("--------------------------------\n")
    sum = 0
    num = 1
    while num<=100:
        sum+=num
        print(f"Number: {num} is {sum}")
        num+=1
    print(f"Sum of number from 1 to 100 is {sum}")