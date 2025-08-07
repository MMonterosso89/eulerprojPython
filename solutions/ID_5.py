#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#I'm not sure how far to search for this but we start from the bottom and can break - I will naively range to 99999

import typing


list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def smallest_1_20_div(maxnum:int):
    for i in range(20,maxnum):
         if all(i % ele == 0 for ele in list):
              print(i)
              break
         
#works but not super performant? About 45s to solve or so. Will ask GPT to improve runtime on this
#ok yeah stride in multiples of highest number (20) is smart and will make much faster.

numbers = [i for i in range(1, 21)]

def smallest_1_20_div(maxnum: int):
    for i in range(20, maxnum, 20):
        if all(i % ele == 0 for ele in numbers):
            print(i)
            break

smallest_1_20_div(10**9)

#yep - about 10x faster! Also smarter list creation