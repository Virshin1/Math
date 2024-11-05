class Maths:
    def __init__(self,operation,first,second):
        if(operation=='*'):
            print(first*second)
        elif(operation=='+'):
            print(first+second)
        elif(operation=='-'):
            print(first-second)
        elif(operation=='/'):
            print(first/second)
        else:
            return 'Enter a valid operation'

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
operator=input("Enter any action (+,-,*,/)")[0]
question=Maths(operator,num1,num2)