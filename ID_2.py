#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#My solution

import typing

def fib_sum(seqmax:int, even_mode=True):
    start = [1,2]
    while start[-1] < seqmax:
        start.append(start[-1] + start[-2])
    
    if even_mode==True:
        return sum(val for val in start if val%2==0)
    else:
        return sum(start)

#CORRECT

#GPT4 Solution

#Again notice it's lack of list usage - perhaps I should rethink my need for those

def even_fibonacci_sum(limit):
    prev, current = 1, 2
    even_sum = 0

    while current <= limit:
        if current % 2 == 0:
            even_sum += current
        prev, current = current, prev + current

    return even_sum

result = even_fibonacci_sum(4_000_000)
print(result)
