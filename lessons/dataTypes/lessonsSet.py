def lesson_set():
    setVal = {"a","b","c","a",1}
    print(f"setVal: {setVal}")
    listVal = [1,2,11,1,1,2,3,4,5]
    print(f"converting list: {listVal} to set using set(list): {set(listVal)}")
    print(f"converting setVal: {setVal} to list using list(setVal): {list(setVal)}")
    print(f"union of setVal and listVal using setVal.union(listVal) : {setVal.union(listVal)}")
    print(f"union of setVal and set(listVal): {setVal | set(listVal)}")
    print(f"intersection of setVal and listVal using setVal.intersection(listVal) : {setVal.intersection(listVal)}")
    print(f"add 6 to setVal using setVal.add(6) : {setVal.add(6)}")
    print(f"updated setVal: {setVal}")
    print(f"remove 6 from setVal using setVal.remove(6) : {setVal.remove(6)}")
    print(f"updated setVal: {setVal}")
    print(f"discard 6 from setVal using setVal.discard(6) : {setVal.discard(6)}")
    print(f"updated setVal: {setVal}")
    print(f"pop item from setVal using setVal.pop() : {setVal.pop()}")
    print(f"updated setVal: {setVal}")
    print(f"clear setVal using setVal.clear() : {setVal.clear()}")
    print(f"updated setVal: {setVal}")