#DICTIONARY DATATYPE:
#dict is one of the pre-defined class and treated as Dict Data Type
#=>The purpose of dict data type is that " To Organize / store the data in the form of (Key,Value)
#=>In (Key,Value), The values of Key represents Unique and values of Value may or may not be unique.
#=>On the object of dict, we can't perform Indexing and slcing Operation bcoz values of Key itself acts index.
'''a={10:"raji",20:"reena",30:"rani",40:"rishi"}
print(a,type(a))
{10: 'raji', 20: 'reena', 30: 'rani', 40: 'rishi'} <class 'dict'>'''
#pre-defined functions in dict
#clear():it is used for removing all the entires of dict objct.
'''a={'A': 25.67, 'K': 30, 'S': 100.34, 'M': 80}
print(a)
{'A': 25.67, 'K': 30, 'S': 100.34, 'M': 80}
a.clear()
print(a)'''
#pop(): =>it is used for removing (Key,Value) from dict object by passing Value of Key.
'''a={'A': 25.67, 'K': 30, 'S': 100.34, 'M': 80}
print(a)
{'A': 25.67, 'K': 30, 'S': 100.34, 'M': 80}
a.pop("S")'''
#popitem():=>This Function is used for removing the last (Key,Value ) from dict object
'''a={'A': 25.67, 'K': 30, 'S': 100.34, 'M': 80}
print(a)
{'A':25.67,'K':30,'S':100.34,'M': 80}
a.popitem()
('M', 80)
print(a)
{'A': 25.67, 'K': 30, 'S': 100.34}'''
#get():=>it is used for obtaining value of Value by passing value of Key.
'''a={'Apple': 25.67, 'Kiwi': 30, 'Sberry': 100.34, 'Mango': 80}
print(a)
{'Apple':25.67,'Kiwi':30,'Sberry':100.34,'Mango': 80}
v1=a.get("Apple")
print(v1)
25.67
v1=a.get("Guava")
print(v1)
None'''
#keys():=>This Function obtains list of keys from non-empty dict object.
