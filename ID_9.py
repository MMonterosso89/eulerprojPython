#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
import math
import sympy

def find_pytrips(c_square=1000**2):
    b_ceiling = math.floor(math.sqrt(c_square))
    #start b high, a low?
    a=1
    for i in range(b_ceiling,1,-1):
        for j in range(a,b_ceiling):
            if i**2 + j**2 == c_square and:
                print(f'{i} squared and {j} squared equal {c_square}')
                break

##Understood entire question wrong - restart
def pytrip_prod(seekval=1000):
    b_ceiling = math.floor(math.sqrt(seekval**2))
    #start b high, a low?
    a=1
    for i in range(b_ceiling,1,-1):
        for j in range(a,b_ceiling):
            if i+j+math.sqrt(i**2+j**2) == seekval:
                return i*j*(1000-(i+j))
#Correct!
#Not sure if this works?
import sympy as sp
a = sp.symbols("a")
b = sp.symbols("b")
c = sp.symbols("c")

f = a**2+b**2

sp.solve(f,a)


#GPT Solution
def find_pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c

result = find_pythagorean_triplet()
print(f"The product of the Pythagorean triplet (a, b, c) for which a + b + c = 1000 is: {result}")

#Wow