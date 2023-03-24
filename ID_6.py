#Sum of squares

#Seems easy and tedious?

def sq_sum(maxnum:int):
    squares = []
    for num in range(1,maxnum+1):
        squares.append(num**2)
    return sum(squares)

def sum_sq(maxnum:int):
    start = 0
    for num in range(1,maxnum+1):
        start+=num
    return start**2

sum_sq(100) - sq_sum(100)

#This one was the easiest by far?


#GPT Solution
n = 100

sum_of_squares = sum(i**2 for i in range(1, n+1))
square_of_sum = sum(range(1, n+1))**2

difference = square_of_sum - sum_of_squares
print(difference)

#Also correct, and more concise