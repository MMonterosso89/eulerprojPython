#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

#Will refer back to itertools for this

import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_count = 0
check_val = 1
while prime_count < 10001:
    if is_prime(check_val):
        prime_count+=1
        print(f'{check_val} is prime number {prime_count}')
    check_val+=1

#Also kinda easy - given I had a prime finder made for me


#GPT Solution
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

result = nth_prime(10001)
print(result)

#Very similar - so that's good