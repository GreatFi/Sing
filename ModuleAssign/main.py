"""
Main calculator file

"""
import inputModule 
import functionsModule
import Logicmodule



while True:

    num1 = inputModule.getnum1()
    num2 = inputModule.getnum2()
    op = inputModule.getOp()


    functionsModule.addition()
    functionsModule.diff()
    functionsModule.divide()
    functionsModule.multiply()

    Logicmodule.CheckOp(num1, num2, op)

    choice = ("Do you want to continue?: (yes/no)")
    if choice != "yes" :
        break



