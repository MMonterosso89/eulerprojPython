#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#This seems pretty easy to me, just multiply the numbers (all three digits?) and then string split them and check
#for equality when reversed.

#100 to 999

import typing

def palin_check(num: int):
    str_num = str(num)
    rev_str_num = str_num[::-1]
    return str_num == rev_str_num

#I suppose you would want to start from the highest numbers and increment down - i.e 999x999


palins=[]
for i in range(999,99,-1):
    for j in range(999,99,-1):
        if palin_check(i*j):
            palins.append(i*j)
            print(f'Palindrome of {i*j} found via {i} * {j}')


max(palins)

#CORRECT


#GPT4 Solution

#Very similar - it also use my function name as I had asked a question about it. I notice it uses a tuple for the factors which is smart.

def palin_check(num: int):
    str_num = str(num)
    rev_str_num = str_num[::-1]
    return str_num == rev_str_num

largest_palindrome = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        product = i * j
        if palin_check(product) and product > largest_palindrome:
            largest_palindrome = product
            factors = (i, j)

print(f'Largest Palindrome of {largest_palindrome} found via {factors[0]} * {factors[1]}')

            
    

