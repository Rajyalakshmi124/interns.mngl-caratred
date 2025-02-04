#BITWISE OPERATORS():
#=>Bitwise Operators applied only on Integer Values but not on float values.
#=>=>Bitwise Operators converts given Integer data into Binary format and performs operations on binary data in the form of Bit by Bit and hence they named as Bitwise Operators.
#1) Bitwise Left shift Operator ( << ):
#=>This operators shifts Specfied No. of Bits toward left side by adding no. Zeros which are equal to no.of bits at right side.
'''a=2 #(2* 2^3(2*2*2(8),8*2))
b=a<<3
print(b)
16
a=10 #(10* (2^3(2*2*2),(8),(10*8)))
b=a<<3
print(b)
80'''

#Bitwise Right shift Operator ( >> ):
#=>This operators shifts Specfied No. of Bits toward right side by adding no. Zeros which are equal to no.of bits at Left side.
'''a=10 #(10 // (2^2),(2*2)=>(4),10//4 ==> 2))
b=a>>2
print(b)
2
a=8
b=2
c=a>>b
print(c)
2'''

#Bitwise OR Operator ( | ):
'''   0 0 ==> 0
      0 1 ==> 1
      1 0 ==> 1
      1 1 ==> 0'''
'''a=4
b=5
c=a|b
print(c)
5'''
#Bitwise AND Operator ( & ):
''' 0 0 ==> 0
    0 1 ==> 0
    1 0 ==> 0
    1 1 ==> 1'''
'''a=10
b=2
c=a&b
print(c)
2'''

#Bitwise complement Operator ( ~ ):
'''a=10
b=~a
print(b)
-11'''

#Bitwise XOR Operator ( ^ ):
'''0 0 ==> 0
   0 1 ==> 1
   1 0 ==> 1
   1 1 ==> 0'''
'''a=10
b=20
c=a^b
print(c)
30'''


