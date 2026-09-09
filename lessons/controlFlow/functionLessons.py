# functions with Docstrings

def calcHt(width:float, length:float) -> float:
    """
    Calculate the area of a rectangle
    """
    return width * length

def addAll(*nums:float) -> float:
    """
    Add all the numbers together
    """
    return sum(nums)

def display_person(**details):
    for key, value in details.items():
        print(f"{key}: {value}")