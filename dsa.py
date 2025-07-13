#import time
#
#start_time=time.time()
#
#sum=0
#for i in range(1,100):
#    sum+=i
#    print(sum)
#    
#end_time=time.time()
#execution_time=end_time-start_time
#print(f"{execution_time:.6f}sec")    
# 
# 
# 
# 
#l=[1,2,3,4,5]
#for i in l:
#    for j in l:
#     print('({},{})'.format(i,j)) 
     
#import sys
#l=[]
#for i in range(10):
#    l.append(i)
#    print(i,sys.getsizeof(l))


    
    
# is kam ko or ache se krne ke liye hum numpy array ka use bhi krste hai
#import numpy as np
#arr=np.zeros(5,dtype=int)
#
#print("array",arr)
#print("size of the array in bytes is :",arr.nbytes)
#\
    
import ctypes

class Meraalist:
    
    def __init__(self): # isse onject bnane pe yeh direct cll hoga 
        self.size=1 # abhi ki total  capacity  1 hai
        self.n=0 # abhi number of elements in array is 0
        # create the c type array with size=self.size
        
        self.A=self.__make_array(self.size)
    
    def __len__(self):
        return self.n 
    def append(self,element):
        if self.n==self.capacity:
         self._resize(2*self.capacity)
         self.A[self.n] = element
        self.n += 1
    def _resize(self, new_cap):
        B = self._make_array(new_cap)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = new_cap

    def __make_array(self,capacity):
        
        return (capacity*ctypes.py_object)()        