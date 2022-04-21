# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 18:32:16 2022

@author: sriharsha
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 18:29:07 2022

@author: sriharsha

Task

Now, let'sA use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:

Function Description

Complete the average function in the editor below.

average has the following parameters:

int arr: an array of integers
Returns

float: the resulting float value rounded to 3 places after the decimal

"""

def average(array):
    # your code goes here
    s = set([])
    for i in arr:
        s.add(i)
    array = s
    su = 0
    for j in array:
        su += j
    return su/len(array)
        
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)