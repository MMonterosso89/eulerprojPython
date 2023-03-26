#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
import math

def find_pytrips(c_square=1000):
    b_ceiling = math.floor(math.sqrt(c_square))
    #start b high, a low?
    a=1
    while a**2 + b_ceiling**2 != c_square:
        print(f'{a} squared and {b_ceiling} squared do not equal {c_square}')
        #not all combinations -  need double loop or check cartesian prod table
        b_ceiling-=1
        a+=1
        if b_ceiling == 0:
            break
    return a,b_ceiling
