'''d={1:"Rohanth",3:"King",5:"Mahendra"}
r=d.items()
print("Items of",r)

d1={1:"Rohanth",3:"King",5:"Mahendra"}
d1.popitem() #Eliminates the Last index in the Dictionary by default
print(d1) #Should not use the Key values in the parantasis

d2={1:"Rohanth",3:"King",5:"Mahendra"}
a=d2.keys() #Prints the Values before the Colon
print(a)

d3={1:"Rohanth",3:"King",5:"Mahendra"}
b=d3.values() #Prints the Values after the Colon
print(b)

d4={1:"Rohanth",3:"King",5:"Mahendra"}
c=d4.copy()
print(c) # Copy function is used to copy the Dictionary

d5={1:"Rohanth",3:"King",5:"Mahendra"}
r=d5
print(r) #Another way to Copy the Dictionary

d6={1:"Rohanth",3:"King",5:"Mahendra"}
d=d6.clear()
print(d)

d7={1:"Rohanth",3:"King",5:"Mahendra"}
d7.pop(1)
print(d7)'''

d8={1:"Rohanth",3:"King",5:"Mahendra"}
d8.get(1)
print(d8)

d9={1:"Rohanth",3:"King",5:"Mahendra"}
d9.update(d9)
print(d9)









