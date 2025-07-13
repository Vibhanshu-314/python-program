#import ctypes
# 
#class MyArray: 
#    def __init__(self):
#        self.n=0
#        self.capacity=1
#        #call _amke_array() to allocate an array of size capacity
#        self.A=self._make_array(self.capacity)
#        # self.A holds an actual array object
#        
#        
#    def __len__(self):
#        return self.n    
#    
#    def __getitem__(self,k):
#        # jese hum acces krna chte hai arr[0],arr[1]
#        if 0<=k<=self.n:
#            return self.A[k]
#        raise IndexError("index out of bounds")
#    def append(self,element):
#        if self.n==self.capacity:# jub array full hoga (n=capacity)
#            self._resize(2*self.capacity)
#            self.A[self.n]=element # bhai n pe hi store krenge n-1 tk store hongi phle kin value
#            
#            self.n+=1
#    def _resize(self,new_cap):
#        B=self._make_array(new_cap)     
#        for i in range(self.n):
#            B[i]=self.A[i]    # cpoy all old values stoerd in arr A
#            self.A=B
#            self.capacity=new_cap
#    def _make_array(self, size):
#        return (size * ctypes.py_object)()
#
#
#arr=MyArray()
#arr.append(10)
#arr.append(20)
#arr.append(30)
#print("length",len(arr))
#print(arr)
#

import numpy as np
# chatgpt numpy question 
###question 1
# creating an array
#a=np.array([i for i in range(2,21,2)])
#print(a)

######question 2
#a=np.array([10,20,30,40,50])
#b=np.where(a>25)
#print(b)
#print(a[b])

##### question3 3 descending order
a=np.array([15,3,9,1,20])
#b=np.sort(a)
#print(b[::-1])
 ## or 
#print(np.sort(a)[::-1])

## question 4  
#a=np.array([1,2,3,4,5,6])
#print(a.reshape(2,3))


## question 5     #   using the set () and count() 
from collections import Counter
#a=[1,2,2,3,4,4,4,5]
#
#print(set(a))
#print(Counter(a))

# in numpy np.unique is the best 
#a=np.arraay([1,2,2,3,4,4,4,5])
#unique_value,counts=np.unique(a,return_counts=True)
#print(unique_value)
#print(counts)

# Array = [3, 7, 1, 9, 5], Check if 9 exists.

#a=np.array([3, 7, 1, 9, 5])
#target=9
#
#mil_gya=target in a
#print("mil_gya",mil_gya)

# Count frequency of each element in [1, 2, 2, 3, 3, 3, 4]
#a=np.array([1, 2, 2, 3, 3, 3, 4])
#kitni_barr_hai=Counter(a)
#print(f"{kitni_barr_hai} bar hai")


#Merge and sort two arrays
#🔹 A = [1, 5, 9], B = [2, 4, 6]

#a,b=np.array([1,5,9],[2,4,6])#❌ This gives an error
#merged=np.concatenate((a,b)).sort()# ❌ .sort() returns None!
#print(merged)

#a=np.array([1,5,9])
#b=np.array([2,4,6])
#b=np.concatenate((a,b))
#print(np.sort(b))
#
#
#unique_arr=np.unique(a)
#print(unique_arr)
#
#
### question 10
#a=np.array([10,50,30,20,40])
#b=np.sort(a)
#print(b[-2])

import numpy as np
#arr=np.array([10,70,30,20,90,60])
#k=int(input())
#k_largest =np.sort(arr)[-k:][::-1]
# isme humne sort kiya hai phle
# jese [10,20,30,60,70,90]
#last  (k) element mi jayenge [-k]
# jse k=3
#[60,70,90]
# [::-1] se descendignorder main ho jaynege
#[90,70,60]
#print(k_largest)

 ## ab ek alternative method 
 
#import heapq
#arr=[10,70,30,20,90,60]
#k=3
#k_largest=heapq.nlargest(k,arr)
#print(k_largest)


import random
#matrix=np.random.randint(1,100,(4,4))
#np.fill_diagonal(matrix,0)
#print(matrix)

#a=np.random.randint(low=0,high=100,size=20)
#print(a)

#✅ Q3. Maximum number of consecutive 1s in a binary array

#a=np.array([1,1,0,1,1,1,0,1])
#binary_str=''.join(a.astype(str))
#max_ones=max(len(x) for x in binary_str.split())
#print(max_ones)


 ### similar question on the consecutive element in array
#a=np.array([1,0,0,1,0,0,0,1]) 
#binary=''.join(a.astype(str)) #10010001
#max_0=max(len(x) for x in binary.split('1'))
#print(max_0)
#a=np.array([1,1,0,1,1,1,0,1]) 
#binary=''.join(a.astype(str))
#count_11=binary.count("11")
#print(count_11)
#
import numpy 

def arrays(arr):
    numpy_arr=numpy.array(arr,float)[::-1]
    return numpy_arr
    
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)