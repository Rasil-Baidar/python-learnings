# This lesson is about numbers in Python.
import math

def lesson_numbers():
    print(f"Max between numbers max(10, 20, 0, 9) : {max(10, 20, 0, 9)}")
    print(f"Power of 2 to the power of 3 pow(2,3): {pow(2,3)}")
    print(f"Square root of 16 sqrt(16): {math.sqrt(16)}")
    print(f"Root of 16 base 3 math.pow(16,1/3): {math.pow(16,1/3)}")

def lesson_integers():
    integer_value = 10
    print(f"Integer value: {integer_value}")
    print(f" Adding 3 to integer value: {integer_value + 3}")
    print(f" Subtracting 3 from integer value: {integer_value - 3}")
    print(f" Multiplying integer value by 3: {integer_value * 3}")
    print(f" Dividing integer value by 3: {integer_value / 3}")
    print(f" Modulus of integer value by 3: {integer_value % 3}")
    print(f" Exponent of integer value by 3: {integer_value ** 3}")
    print(f" Floor division of integer value by 3: {integer_value // 3}")

def lesson_floats():
    float_value = 10.5123
    negative_float_value = -10.5
    print(f"Float value: {float_value}")
    print(f"Type of float value: {type(float_value)}")
    print(f" Ceiling value of float value: {math.ceil(float_value)}")
    print(f" Floor value of float value: {math.floor(float_value)}")
    print(f" Absolute value of negative float {negative_float_value} : {abs(negative_float_value)}")
    print(f" Rounded value of float value {float_value} to 2 decimal places: {round(float_value,2)}")
