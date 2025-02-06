#IF-ELIF-ELSE:
'''num=int(input("Enter the number: "))
result=1
i=num
if num < 0:
    print("Factorial is not defined for negative numbers")
elif num == 0 or num == 1:
    print("factorial of",num,"is 1")
else:
    while i>1:
        result *= i
        i -= 1
    print("factorial of",num,"is",result)'''
        
#MATCH--CASE STATEMENTS:
#match case are keywords
#it can be integer, char, string and bool
'''import sys
print("_"*50)
print("\tArithmetic operations")
print("_"*50)
print('\t1.Addition:')
print('\t2.substraction:')
print('\t3.multiplication:')
print('\t4.Division:')
print('\t5.Modulo Division:')
print('\t6.Exponentional:')
print('\t7.Exit:')
print("_"*50)
a=int(input("Enter your choice"))
match(a):
    case 1:
        a,b=float(input("Enter First value for Addition")),float(input("Enter Secondt value for Additions"))
        print("sum({},{})={}".format(a,b,a+b))
    case 2:
        a=float(input("Enter First value for substraction:"))
        b=float(input("Enter second value for substraction:"))
        print("sub({},{})={}".format(a,b,a-b))
    case 3:
        a=float(input("Enter First value for multiplication:"))
        b=float(input("Enter second value for multiplication:"))
        print("mul({},{})={}".format(a,b,a*b))
    case 4:
        a=float(input("Enter First value for Division:"))
        b=float(input("Enter second value for Division:"))
        print("div({},{})={}".format(a,b,a/b))
        print("floor ({},{})={}".format(a,b,a//b))
    case 5:
        a=float(input("Enter First value for Modulo Division:"))
        b=float(input("Enter second value for Modulo Division:"))
        print("mod({},{})={}".format(a,b,a%b))
    case 6:
        a=float(input("Enter Base:"))
        b=float(input("Enter Power:"))
        print("exp({},{})={}".format(a,b,a**b))
    case 7:
        print("\nThanks for using")
        sys.exit()
        
    case _:
        print("ur choice of selection is wrong!")'''
        
        
        


