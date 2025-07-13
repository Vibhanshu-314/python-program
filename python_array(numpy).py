import numpy as np

#my_array = np.arange(8)
#
#print(my_array)
#print(type(my_array))
#
#my_array=np.arange(0,11,2)
#print(my_array)
#my_array = np.arange(1,10,2)
#print(my_array)
#my_array = np.arange(1,-10,-1)
#print(my_array)
#
### arrays from lists
#from_list=np.array([1, 2, 3, 4, 5],dtype=np.int8) # isse phle 54 bit ma store ho rha tha ab data type int m 8 bit m ho rha hai jiss hmara kaam efficiently ho jayega esa jaruri ni hia lekin hn space km lega
#print(from_list)
#print(type(from_list)) 
#print(type(from_list[0]))  # Check the type of the first element
#
#
## 2d array#
##from_list=np.array([[1, 2, 3],[4,5,6]],dtype=np.int8)
##print(from_list)
#
#
## using looop type to take self input 
#
#array_2d = np.array((np.arange(1,12,2),np.arange(0,11,2)))
#print(array_2d.reshape(4,3))
#print("2d shape array",array_2d)
#
#print(np.zeros((2,2)))
#print(np.ones((2,2)))
#print(np.empty((2,2)))
#print(np.empty((2,2,2)))
#
#print(np.eye(1))
#print()
#print(np.eye(2))
#print()
#print(np.eye(3))
#
#
#eye_array=np.eye(3)   # (3,k=1) ise diagonal uppr shift ho jayega
#eye_array[eye_array==0]=2
#
#
##[[1. 2. 2.]
## [2. 1. 2.]
## [2. 2. 1.]]
#
#eye_array[eye_array<2]=9
##eye_array[0]=3 #row 0 wale sare 3 ho jaywnge
#eye_array[:2]=3
#print(eye_array)
#eye_array[-1]=8
#print(eye_array)
#
#eye_array[:,0]=7
#print(eye_array)
#eye_array[:,-1]=6
#print(eye_array)
#eye_array[1:,:2]=4
#print(eye_array)
#print()
#print(np.sort(eye_array)) # row se sorted hoga
#print(np.sort(eye_array,axis=0)) # column se sorted hoga
#print(np.sort(eye_array,axis=None)) # pura array sort hoga

               ### operation on numpy array
#a=np.zeros((3,3))
#a[:]=2
#print(a)
#print(a.dtype)
#
#b=np.arange(1,10).reshape((3,3))
#print(b)
#
#c=np.arange(1,12,2).reshape((3,2))
#print(c)
#print()
#a=np.zeros((3,3))
#a[:]=2
#print(a.fill(8))
#a+=3# fill function is used to fill the array with a specific value
#print(a)
#
#       #### or
#a=np.full((3,3),8)+3
#print(a)     
#
#
### arithmtic operation
#print(a.sum())
#print(a.sum(axis=0))
#
#a=np.arange(1,10).reshape((3,3))
#print(a.argmax())
#print(a.min())
#peak_to_peak=a.max()-a.min()
#print(peak_to_peak)
#
#array_flat=a.reshape(a.size)
#print(array_flat)
#print(a.flatten())
#print(a.ravel())  # ravel is used to flatten the array
#print(a.T)  # transpose of the array      
#print(a.T.shape)  # shape of the transposed array
#print(a.T.reshape(a.size))  # reshaping the transposed array to a 1D array          
#print(a.T.flatten())  # flattening the transposed array
#print(a.T.ravel())  # raveling the transposed array
#print(a.T.ravel().shape)  # shape of the raveled transposed array  
   
   
   
   
   
   

      ######## basic program according to chatgpt ####
 ## create and initialize  a numpy array

array_np=np.array([1,3,4,5,6])
#print(array_np)
#
### printing the max and min element in the array
#print("max element in the array ;",array_np.max())
#
#print("min element in the array ;",array_np.min())
#
### printing the index of the max and min element in the array
#print("index of max element in the array ;",array_np.argmax())
#
### printing the index of the user defined element in the array 
#user_defined_element = int(input("Enter the element to find its index: "))
#if user_defined_element in array_np:
#    print(f"index of {user_defined_element} in the array ;", np.where(array_np == user_defined_element)[0][0])
#else:
#    print(f"{user_defined_element} is not in the array")
# ### or       
   
#print("reverse the array",array_np[-1::-1])
#print("sum of the elements in the array :",array_np.sum())  
#print("mean of the elements in the array :",array_np.mean()) 
#
#
#a_np=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#a_np.sort(axis=0)
#print("array sorted according to column",a_np )
#
#
## list se duplicate nikale
#arr=[1,2,2,3,4,4,5]
#no_duplicate=list(set(arr))
#print(no_duplicate)
#
## numpy se krenge 
#arr_np=np.array([1,2,2,3,4,4,5])
#no_duplicate_np=np.unique(arr_np)
#print(no_duplicate_np)
#
## using  lists
#arr_1=[1,2,3]
#arr_2=[4,5,6]
#print("merged list:",arr_1+arr_2)
#
##using numpy
#arr_1_np=np.array([1,2,3])
#arr_2_np=np.array([4,5,6])
#merged_np=np.concatenate((arr_1_np,arr_2_np))
#print("merged numpy array :",merged_np)


    ## checking the order is sorted or not
    
#arr_1=[1,2,3] 
#print(arr_1[1:])   
#print(arr_1[:-1])

#arr=np.array([[10,20,30],
#             [40,50,60],
#             [70,80,90]])
#print(arr[0]) # row 1
#print(arr[0,1]) # row 1 ka 2 element
#print(arr[:,0])   # column 1
#print(arr[:,1])   # column 2
#print(arr[:,1][1])  # column 2 ka 2nd element
# column 1 ka 2nd element

#arr_np=np.array([1,2,3,4,5])
#print(arr_np[0:1])
#print(arr_np[-1::-1])
#
#
#arr=np.array([[10,20,30],
#             [40,50,60],
#            [70,80,90]])
## accessing the row
#print(arr[1])
#print(arr[1,0])
#print(arr[:,1])
#print(arr[:,1][1])
#print(arr[:,::-1])
#   arr_np=np.array([1,2,3,4,5])
#   #greater_than_20=arr_np[arr_np>3]
#   #print(greater_than_20)
#   for i in arr_np:
#       print(f"{i}>2: ",i>2)


#class Calculator():
#    def __init__(self,numbers):
#        self.numbers=numbers
#    def add(self):
#        return sum(self.numbers)
#    def subtract(self):
#        result = self.numbers[0]
#        for num in self.numbers[1:]:
#            result-=num
#        return result   
#    def multiply(self):
#        result=1
#        for num in self.numbers:
#            result *= num 
#        return result
#    def divide(self):
#        result=self.number[0]
#        for num in self.number[1:]:
#            if num ==0:
#                return "error : cannot divide by 0"
#            result /=num
#        return result
#           
#user_input=input("enter the numbers seperated with space:")
#num_list=list(map(float,user_input.split())) 
#
#
#calc=Calculator(num_list)
#
#print("addition:",calc.add())
#print("substracted:",calc.subtract())
#print("multiplication:",calc.multiply())       
#print("division:",calc.divide())

a=[1,2,3,4,5]
print(a[-3:][::-1])