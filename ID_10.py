#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

#Sieve from itertools solves this

import math
import itertools as it

def iter_index(iterable, value, start=0):
    "Return indices where a value occurs in a sequence or iterable."
    # iter_index('AABCADEAF', 'A') --> 0 1 4 7
    try:
        seq_index = iterable.index
    except AttributeError:
        # Slow path for general iterables
        it = it.islice(iterable, start, None)
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

vals_gen = sieve(2000000)

sum(vals_gen)