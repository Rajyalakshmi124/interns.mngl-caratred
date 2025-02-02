#Operators in Python:
#=>An Operator is a symbol, which is used to perform certain operation.
#=>In Python Programming, we have 7 types of Operators. They are
#Arithmetic Operators:
#Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, and division.
#==>Addition(+,-,*,/,//,**,%)
'''a=10
b=20
print(a+b)
30'''
#==> Substraction(-)
'''a=10
b=20
print(a-b)
-10'''
#==> Multiplication(*)
'''a=2
b=3
print(a*b)
6'''
#==> Division(/)
'''a=10
b=5
print(a/b)
2.0'''
#==> Floor Divison(//)
'''a=10
b=2
print(a//b)
5'''
#==> Modulo Division(%)
'''a=10
b=5
print(a%b)
0'''
#==> Exponentiation(**)
'''a=2
b=4
print(a**b)
16'''

##Assignment Operator():=>The purpose of Assigment operator is that to transfer Right hand Side (RHS) value to Left Hand Side (LHS) Variable .
#=>We can use Assignment Operator in two ways.
#=>Single Line Assigment
'''a=10
b=20
print(a,b)
10 20'''
#=>Multi Line Assigment
'''a,b,c=10,20,30
print(a,b,c)
10 20 30'''

##3. Relational Operators(>,<,==,!=,>=,<=):
#=>The purpose of Relational Operators is that "To compare two or more number of values".
#=>Greater Than(>):
'''a=10
b=20
a>b
False
a=20
b=10
a>b
True'''
#=>Less Than(<):
'''a=10
b=20
a<b
True
b<a
False'''
#=>Equality(==):
'''a=10
b=20
print(a==b)
False
b=10
print(a==b)
True'''
#=>not equal to(!=):
'''a=10
b=20
print(a!=b)
True'''
#greater than or equal to(>=):
'''a=10
b=20
print(a>=b)
False
print(b>=a)
True'''
#Less Than or equal to(<=):
'''a=10
b=20
print(a<=b)
True
print(b<=a)
False'''
#Logical Operators in Python: =>The purpose of Logical Operators is that " To combine two or more number of Relational Expressions / Conditions".
#OR():
'''a=10
b=20
a>b or a<b
True'''
#AND():
'''a=10
b=30
a>b and a<b
False
a<b and b<a
False
a>b and b>a
False
a<b and b>a
True'''
#NOT():
'''a=10
b=20
b>a and b!=a
True
a==b
False
a!=b
True
not 0
True'''






