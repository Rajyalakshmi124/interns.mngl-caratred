#IF-ELSE:
'''n=int(input("Enter the number: "))
if n%2==0:
    print("Even")
else:
    print("odd")'''

'''n=int(input("Enter the number: "))
if n==0:
    print("{} is Zero".format(n))
else:
    if n>0:
        print("{} is Positive".format(n))
    else:
        print("{} is Negative".format(n))'''
        
#NESTED IF-ELSE STATEMENTS:
'''a=int(input("Enter the digit: "))
if(a==1):
    print("{} is One".format(a))
if(a==1):
    print("{} is TWO".format(a))
if(a==1):
    print("{} is THREE".format(a))
if(a==1):
    print("{} is FOUR".format(a))
if(a==1):
    print("{} is FIVR".format(a))
if(a==1):
    print("{} is SIX".format(a))
if(a==1):
    print("{} is SEVEN".format(a))
if(a==1):
    print("{} is EIGHT".format(a))
else:
    print("{} is number".format(a))'''
#emp payslip:
'''eno=int(input("Enter Employee Number: "))
ename=input("Enter the Employee Name: ")
basicsal=float(input("Enter Employee Basic Salary: "))
if(basicsal>=10000):
    da=(20/100)*basicsal
    ta=(15/100)*basicsal
    hra=(12/100)*basicsal
    cca=(21/100)*basicsal
    ma=(2/100)*basicsal
    gpf=(1/100)*basicsal
    lic=(1/100)*basicsal
else:
    da=(25/100)*basicsal
    ta=(15/100)*basicsal
    hra=(12/100)*basicsal
    cca=(2/100)*basicsal
    ma=(2/100)*basicsal
    gpf=(2/100)*basicsal
    lic=(10/100)*basicsal
netsal=(basicsal+da+ta+hra+cca+ma)-(gpf+lic)
print("\Employee pay slip for month of feb")
print("_"*60)
print("\tEmployee Number:{}".format(eno))
print("\tEmployee Name:{}".format(ename))
print("\tEmployee Basic Salary:{}".format(basicsal))
print("\tEmployee DA:{}".format(da))
print("\tEmployee TA:{}".format(ta))
print("\tEmployee HRA:{}".format(hra))
print("\tEmployee CCA:{}".format(cca))
print("\tEmployee MA:{}".format(ma))
print("\tEmployee GPF:{}".format(gpf))
print("\tEmployee LIC:{}".format(lic))
print("_"*60)
print("\tEmployee Net Salary:{}".format(netsal))
print("_"*60)'''


