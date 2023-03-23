#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

#I remeber this being the first problem that ran into memory issues with R

#I will probably need to find a generator solution or something similar?

#So logically we should start from the top of the number and count down - and a multiple has to be at most half of the number given
#to be a factor.

#My solution

#Best to create two function - a factor finder than then a prime "certifier"?

import collections
import math
import operator
import random
import itertools as it
import more_itertools

def find_factor(num=600_851_475_143):
    factors = []
    for i in range(1,num):
        if num%i==0:
            factors.append(i)
    return factors


#simply too slow - lets look to itertools for some help

def iter_index(iterable, value, start=0):
    "Return indices where a value occurs in a sequence or iterable."
    # iter_index('AABCADEAF', 'A') --> 0 1 4 7
    try:
        seq_index = iterable.index
    except AttributeError:
        # Slow path for general iterables
        it = islice(iterable, start, None)
        i = start - 1
        try:
            while True:
                yield (i := i + operator.indexOf(it, value) + 1)
        except ValueError:
            pass
    else:
        # Fast path for sequences
        i = start - 1
        try:
            while True:
                yield (i := seq_index(value, i+1))
        except ValueError:
            pass

def sieve(n):
    "Primes less than n"
    # sieve(30) --> 2 3 5 7 11 13 17 19 23 29
    data = bytearray((0, 1)) * (n // 2)
    data[:3] = 0, 0, 0
    limit = math.isqrt(n) + 1
    for p in it.compress(range(limit), data):
        data[p*p : n : p+p] = bytes(len(range(p*p, n, p+p)))
    data[2] = 1
    return iter_index(data, 1) if n > 2 else iter([])

def factor(n):
    "Prime factors of n."
    # factor(99) --> 3 3 11
    for prime in sieve(math.isqrt(n) + 1):
        while True:
            quotient, remainder = divmod(n, prime)
            if remainder:
                break
            yield prime
            n = quotient
            if n == 1:
                return
    if n >= 2:
        yield n

#Solved with factor and next three times - can write a func to do that
#Was highly performant, will have to try and understand how this works better

#zsh: killed     /usr/local/bin/python3 - Still too much to handle on M2 Mac?


#GPT 4 Solution

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime_factor(n):
    largest_factor = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_prime(i):
            largest_factor = max(largest_factor, i)
    return largest_factor

number = 600851475143
result = largest_prime_factor(number)
print(result)


import itertools

def prime_factors(n):
    factors = []
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors

def largest_prime_factor_itertools(n):
    return max(prime_factors(n))

number = 600851475143
result = largest_prime_factor_itertools(number)
print(result)


