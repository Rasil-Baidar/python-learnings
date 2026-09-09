def lesson_range():
    print(f"range(start, stop, step)")
    print(f"range(10) : {list(range(10))}")
    print(f"range(1,10) : {list(range(1,10))}")
    print(f"range(1,10,2) : {list(range(1,10,2))}")
    print(f"Even numbers using range:{list(range(2,21,2))}")
    print(f"--------------------------------\n")
    print(f"Multiplication table of 5 using range:")
    for num in range(0,11):
        print(f"5 * {num}: {5 * num}")