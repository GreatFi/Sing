
"""
Logic Module for the simple calculator

"""
import functionsModule

def CheckOp(num1, num2, op):
    if (op == "sum"): 
        functionsModule.addition(num1, num2)
    elif (op == "difference"):
        functionsModule.diff(num1, num2)
    elif (op == "quotient"):
        if (num2 == 0):
            print("undefined")
        else:
            functionsModule.divide(num1, num2)
    elif (op == "product"):
        functionsModule.multiply(num1, num2)
    else:
        print("invalid operator")
