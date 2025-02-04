#MEMBERSHIP OPERATOR:
#=>The purpose of Membership Operators in python is that "To verify / check the existence of whether the value present in sequence or collection obejcts"
#we have 2 Membership Operators.
#==> in: =>Here sequence objects represents (str,bytes, bytearray and range) and collect objects represents (list, tuple,set,frozenset,dict)
#==> not in:
'''a=[10,20,30,40,50,60,70]
60 in a
True
100 in a
False
100 not in a
True'''

#Identity Operators() :The purpose of Identity Operators is that to "To compare the memory addresses of two objects"
#is , is not
'''a=[10,20,30,40,50,60,70]
print(a,id(a))
[10, 20, 30, 40, 50, 60, 70] 3047142697408
b=[10,20,30,40,50,60,70]
print(b,id(b))
[10, 20, 30, 40, 50, 60, 70] 3047142579584
a is b
False
a is not b
True'''
'''a="raji"
b="raji"
print(a,id(a))
raji 3047142761584
print(b,id(b))
raji 3047142761584
a is b
True
a is not b
False'''
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=a+b
print(c)
