#Looping / Iterative / Repatative Statements:
#It is used to perform certain repetedly for finite number of times until test condition becomes false.
#---> For loop
#---> while loop (both are keywords)
'''n=int(input("Enter the number: "))
if n <= 0:
    print("it is invalid")
else:
    i=1
    while(i <= n):
        print(i)
        i=i+1'''
'''a=6
if a <= 0:
    print("not valid")
else:
    i=1
    while i <= a:
        print(i)
        i=i+1'''

#MULTIPLICATION TABLE:
'''a=int(input("enter the number: "))
if a<=0:
    print("invalid")
else:
    i=1
    while 10 >= i:
        print(a,"*",i,"=",a*i)
        i=i+1'''
#sumdigits:
'''a=int(input("Enter the number:"))
if a <= 0:
    print("Invalid")
else:
    s=0
    while a>0:
        d=a%3
        s=s+d
        a=a//3
    else:
        print("Sum of digit={}".format(s))'''



'''d="python"
if(d<=0):
    print("invalid")
else:
    i=0
    while(i<=d):
        print(i)
        i=i+1'''
#(here error occur coz we cannot compare a string with an integer )        
#Traceback (most recent call last):
#  File "<pyshell#19>", line 1, in <module>
#    if(d<=0):
#TypeError: '<=' not supported between instances of 'str' and 'int'



'''d="python"
i=0
while i < len(d):
    print(d[i])
    i=i+1
p
y
t
h
o
n'''


#FOR LOOP:
#for,in,else --> Keywords
#varname represents programmer choice
#iterable object ---> contains multiple objects like list, set, dict, tuple
'''a="python"
for i in a:
    print(i)
p
y
t
h
o
n'''

'''a=range(100,106)
i=0
while(i<len(a)):
    print(a[i])
    i=i+1
100
101
102
103
104
105'''

'''for j in a:
    print(j)
100
101
102
103
104
105'''

'''a=10
for i in a:
    print(i)'''
#Traceback (most recent call last):
 # File "<pyshell#3>", line 1, in <module>
  #  for i in a:
#TypeError: 'int' object is not iterable

'''a=[10,20,30,40]
for i in a:
    print(i)
10
20
30
40'''

'''n=int(input("Enter the number: "))
if(n<=0):
    print("Invalid")
else:
    for i in range(5,n+1):
        print(i)'''

#write a python program which will accept any integer value and generate even and odd numbers
'''n=int(input("Enter the number:"))
if(n<=0):
    print("invalid")
else:
    #for i in range(2,n+1,2):
       # print(i)
    for j in range(1,n+1,2):
        print(j)'''

#multiplictaion Table:
'''a=int(input("enter the number: "))
if a<=0:
    print("invalid")
else:
    for i in range(1,11):
        print(a,"*",i,"=",i*a)'''

#Natural numbers:
#a=int(input("enter the numbers:"))
'''if(a<=0):
    print("Invalid")
else:
    b=0
    for i in range(1,a+1):
        b=b+i
        print(b)'''
'''if(a<=0):
    print("Invalid")
else:
    for i in range(1,a+1):
        print(i**2)'''
'''if(a<=0):
    print("Invalid")
else:
    for i in range(1,a+1):
        print(i**3)'''
#SUM & AVERAGE:
'''n=int(input("Enter the iteration number:"))
if(n<=0):
    print("invalid")
else:
    lst=[]
    for i in range(n):
        b=int(input("Enter the number:"))
        lst.append(b)
    else:
        print(lst)
        s=0
        for b in lst:
            print(b)
            s=s+b
        else:
            print(s)
            print(s/n)'''
#SECOND APPROACH:
'''n=int(input("Enter the iteration number:"))
if(n<=0):
    print("invalid")
else:
    i=1
    s=0
    while(i<=n):
        b=int(input("Enter the number:"))
        s=s+b
        i=i+1
    else:
        print("sum:",s)
        print("Avg:",s/n)'''
#write a python program which will accepts list of values and sort them in accending and decending orders
#sortnumbers:
'''a=[10,20,30,40,50,60]
a.sort()
print(a)
[10, 20, 30, 40, 50, 60]
a.reverse()
print(a)
[60, 50, 40, 30, 20, 10]
max(a)
60
min(a)
10'''

#write a python program which will accepts list of names and sort them in accending and decending orders
#sortnumbers:
'''a=["raji","rani","rishi","reena"]
a.sort()
print(a)
['raji', 'rani', 'reena', 'rishi']
a.reverse()
print(a)
['rishi', 'reena', 'rani', 'raji']'''


    
        
    
       
            
    


    








