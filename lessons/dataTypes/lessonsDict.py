def lesson_dict():
    dictVal = {
        "name": "Rasil",
        "age": 28,
        "city": "Sydney"
    }
    print(f"dictVal: {dictVal}")
    print(f"name in dictVal: {dictVal['name']}")
    print(f"age in dictVal: {dictVal['age']}")
    print(f"city in dictVal: {dictVal['city']}")
    print(f"dictVal.keys(): {dictVal.keys()}")
    print(f"dictVal.values(): {dictVal.values()}")
    print(f"dictVal.items(): {dictVal.items()}")
    print(f"dictVal.get('name'): {dictVal.get('name')}")
    print(f"dictVal.get('abc','default'): {dictVal.get('abc','default')}")
    print(f"pop item from dictVal: {dictVal.popitem()}")
    print(f"updated dictVal: {dictVal}")
    print(f"pop age from dictVal: {dictVal.pop('age')}")
    print(f"updated dictVal: {dictVal}")
    dictVal.update({"age": 24})
    print(f"updated dictVal: {dictVal}")
    dictVal.clear()
    print(f"updated dictVal: {dictVal}")
    dictVal.update({"name": "Rasil", "age": 28, "city": "Sydney"})
    print(f"updated dictVal: {dictVal}")
