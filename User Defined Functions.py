'''def Rohanth(*):
    print("Rohanth is KING")
    return
Rohanth()
Rohanth()

def add(x,y):
    return (x+y)
print(add(1,2))

def mod(a,b):
    return (a%b)
print(mod(10,2))

def add(*a):
    sum=0
    for i in a:
       sum=sum+i
    print("The Lavda sum is",sum)
add(1,2,6,541,51,51)

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(10))

r=lambda a,b,c,d,e,f:a+b+c+d+e+f #Ananomous Funnction Must be done in only single line after the colon & Indentaion should not not be followed
print(r(10,20,30,40,50,60))'''

def lavda(a):
    return a**a
l1=[1,2,3,4]
l2=l1(filter(lavda,l1))
print(l2)




