"""
Functions Module 

"""
from inputModule import num1, num2

def addition():
    sum = num1 + num2
    print(f"this is the sum: {sum}")
    return sum
def diff():
    difference = num1 - num2
    print(f"this is the difference of the two numbers: {difference}")
    return difference
def divide():
    quotient  = num1 / num2
    print(f"this is the quotient of two numbers: {quotient}")
    return quotient
def multiply():
    product = num1 * num2
    print(f"this is the product of two numbers: {product}")
    return product

