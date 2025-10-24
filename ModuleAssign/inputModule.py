"""
Module to get all the input
"""
def getnum1() :
    num1 = int(input("input your first number: "))
    return num1

def getnum2() :
    num2 = int(input("enter your second number: "))
    return num2
#operation input
def getOp():
    op = input("enter your operation: sum \nproduct \nquotient \ndifference ")
    return op