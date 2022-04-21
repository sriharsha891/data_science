# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:11:17 2022

@author: sriharsha
"""

#Numpy 
import numpy as np

#Creating numpy arrays
#1d array using lists
l1 = [1,2,3,4,5]
arr1 = np.array(l1)
#note : arrays take only single data type
print(arr1)
print(type(arr1))

#2d array
l2 = [6,7,8,9,10]
arr2 = np.array([l1,l2],dtype = str)
print(arr2)
#l1 and l2 should be of same dimensions

#to get the dimensions of an array we use ndim method
dim = arr2.ndim
print(dim)
#ndim is not callable

#Intrinsic numpy functions to quickly generate an array.
r_arr = np.arange(1,150)
#we are generating array in a sequence.
print(r_arr.dtype)
print(r_arr)

#randomly distributed with exact spaces in arr using linspace
l_arr = np.linspace(2,10000,num=500,dtype = int)
print(l_arr)

#random module
rrr = np.random.randint(0,100,size = 100)
print(rrr)
#
rr = np.random.rand(6,6)
print(rr)


#creating arrays with constant values
n = [3,3,3]
arr_zero = np.zeros(n,dtype = int)
arr_ones = np.ones(n,dtype = int)
print(arr_zero)
print(arr_ones)

ar1 = np.zeros_like(l_arr)
print(ar1)































