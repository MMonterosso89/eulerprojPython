def triangle_number(stopval = 1000):
    dict = {}
    for t in range(0,stopval):
        dict[t] = sum(range(1,t+1))
    return dict

# in order to have 501 divisors - it has to be larger than 501 - likely much larger...
#actually glad to learn about about the sqrt number theory rule from GPT

import math

def count_divisors(n):
    count = 0

    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if n // i == i:
                count+=1
            else:
                count+=2
    return count


def check_divisors(entry_dict):
    divisor_dict = {}
    for value in entry_dict.values(): 
        divisor_dict[value] = count_divisors(value)
    return divisor_dict


#max_key = max(divisors, key=lambda k: divisors[k]) # we have found it somewhere

def search_divisors(div_dict):
    for entry in div_dict.keys(): 
        if div_dict[entry] > 501:
            print(f'large divisor entry found at triangle number {entry} with {div_dict[entry]} total divisors')
            break


#

trinums = triangle_number(20000)

divisors = check_divisors(trinums)

search_divisors(divisors)

#12375 - incorrect?

count_divisors(12375)

#7479: 192
count_divisors(7479)