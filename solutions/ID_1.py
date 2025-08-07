#Multiples of 3 or 5

##If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

#My Solution

def three_five_divis_total(limit:int):
    """
    Find the sum of all the multiples of 3 or 5 below a given limit.
    """
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)

##CORRECT ANSWER - make note to use 999 not 1000 in function


##GPT4 SOLUTION

#notes it's very similar, so that's good. Note that it does not maintain a list which I suppose is better as one technically isnt needed
def sum_of_multiples(limit):
    total_sum = 0
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

result = sum_of_multiples(1000)
print(result)


