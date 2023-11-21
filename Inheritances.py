'''Types Inheritance In Python
1. Single inheritance
2. Multiple inheritances
3. Multilevel inheritance
4. Hierarchical inheritance
5. Hybrid inheritance'''

#Single Inheritance
class A:
    def a(self):
        print("Class A")
class B(A):
    def b(self):
        print("Class B")
C=B()
C.a()
C.b()

#Multiple Inheritance
class A:
    def a(self):
        print("Class A")
class B(A):
    def b(self):
        print("Class B")
class C(B):
    def c(self):
        print("Class C")
d=C()
d.a()
d.b()
d.c()

#Multi-level inheritance(More Parent Class and one Child Class)
class A:
    def a(self):
        print("Class A")
class B:
    def b(self):
        print("Class B")
class C(B,A):
    def c(self):
        print("Class C")
d=C()
d.a()
d.b()
d.c()

#Hierarchical inheritance

class A:
    def a(self):
        print("Class A")
class B(A):
    def b(self):
        print("Class B")
class C(A):
    def c(self):
        print("Class C")
class D(A):
    def d(self):
        print("Class D")

d=B()
d.a()
d.b()
d=C()
d.c()
d=D()
d.d()

#Hybrid inheritance

class A:
    def a(self):
        print("Class A")
class B(A):
    def b(self):
        print("Class B")
class C(A):
    def c(self):
        print("Class C")
class D(B,C):
    def d(self):
        print("Class D")
d=D()
d.a()
d.b()
d.c()
d.d()


























