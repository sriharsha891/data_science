# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:47:48 2022

@author: sriharsha
"""
# =============================================================================
# n = int(input("Enter number of elements : "))
#  
# 
# a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
# a.sort()
# print(a)
# print(a[-2])
# =============================================================================

# =============================================================================
# n = int(input())
# a = list(map(int,input().strip().split()))[:n]
# a.sort() 
# s = list(set(a))
# print(s[-2])
# 
# =============================================================================

# =============================================================================
#  n = int(input())
#     arr = map(int, input().split())
#     set_arr = set(arr)
#     list_arr = list(set_arr)
#     new_arr = sorted(list_arr)
#     length_of_arr = len(new_arr)
#     print(new_arr[length_of_arr-2])
# =============================================================================
# =============================================================================
# areas = ["hallway", 11.25, "kitchen", 18.0,
#         "chill zone", 20.0, "bedroom", 10.75,
#          "bathroom", 10.50, "poolhouse", 24.5,
#          "garage", 15.45]
# #del(areas[-3])
# del(areas[-4:-2])
# print(areas)
# =============================================================================
def pal(num):
  c=0  
  for i in range(0,len(num)):
        if num[i]==num[(len(num)-1)-i]:
            c +=1
  if c==len(num):      
      print(f"{num} is a Palindrome number")
  else:
      print(f"{num} is not a Palindrome number ")
num=input("Enter the number: ")   
pal(num)