#  class and object

#class DemoClass:
#       a=10
#       
#       def sum(self):
#              print(20+10)
#              
#demoobject=DemoClass()
#print(demoobject.a) 
#demoobject.sum();


# method and constructor

#class DemoClass:
#       a=10
#       def __init__(self):
#              print("this is constr")
#       def showvalue(self):
#              print(self.a)
#              c=self.a*self.a
#              print(c)
#       def showvalue1(self,a,c):
#              print("welcome to vs code") 
#              print(a+c)      
#obj=DemoClass()
#obj.showvalue()              
#obj.showvalue1(1,2)


# inheritance ###
#single inheritance
#class A:
#       def displayA(self):
#              print("welcome to method of class A")
#class B(A):
#       def displayB(self):
#              print("welcome to method of class B")
#              
#obj=B()
#obj.displayA()
#obj.displayB()                          
#
#    multiple inheritance
#class A:
#       def displayA(self):
#              print("welcome to method of class A")
#class B:
#       def displayB(self):
#              print("welcome to method of class B")
#class C(A,B):
#       def displayC(self):
#              print("welcome to the method of class c")
#                  
#obj=C()
#obj.displayA()
#obj.displayB()    
#obj.displayC()                      


## getter and setter#

#class Student:
#       def __init__(self): # this is constr
#              self.__name="" # private attribute  (__name is prvt attribute makes it difficut to access from outside)
#       def getname(self): # to retrive the name 
#              return self.__name 
#       def setname(self,name): # to assign the name
#              self.__name=name
#obj=Student()
#obj.setname("testing")   
#name=obj.getname()
#print(name)                         
      
       #### encapsulation ####
#class BankAccount:
#       def __init__(self,balance):#       constructor          
#              self.balance=balance #                    
#       def deposit(self,amount):#
#              if amount>0:
#                     self.balance+=amount
#                     print(f"deposited {amount}")
#       def withdraw(self,amount):
#              if 0<amount<=self.balance:
#                     self.balance-=amount
#                     print(f"withdrawn {amount}")
#       def get_balance(self):
#              return self.balance  
#account=BankAccount(1000)  #  
#account.deposit(500)
#account.withdraw(200)
#print(f"current balance is :{account.get_balance()}")  # current balance is 1300                      
        
        
        ## polymorphism #
#l=[1,2,3,4,5  ]
#print(len(l))
#s="vibh" 
#print(len(s)) # polymorphism is the ability to use a single interface to represent different data types or classes.

#class Vk:
#       def displayinfo(self,name =""):
#              print("my name is :"+name)
#              
#obj=Vk()
#obj.displayinfo()
#obj.displayinfo("vibhu") # method overloading is a feature that allows a class to have multiple methods with the same name but different parameters.
#obj.displayinfo("vibhu kumar") # method overloading is not supported in python, but we can achieve it by using default parameters or variable-length arguments.
  
  # now we are using the super() function to call the parent class method in the child class.
                                          
#class Parent:
#       def display(self):
#              print("i am parent class")
#
#class Child(Parent):
#       def display(self):
#              super().display()
#       print("i am child class")   
#             
#             
#obj=Child() 
#obj.display()  # this will call the child class method         

     #   mething overloading

#class Area:
#       def find_area(self,a=0,b=0):
#              if a!=0 and b!=0:
#                     return a*b
#              elif a!=0:
#                     return a*a
#              else:
#                     return 0
#obj=Area()
#print(obj.find_area(5,20))
#print(obj.find_area(2))
#print(obj.find_area())            
  
  
  
n,m=map(int,input().split())
if n % 2 == 1 and m == n * 3:
# top part
 for i in range(n//2):
     pattern='.|.'*(2*i+1)
     print(pattern.center(m,'-'))
     
 # middle part
 print('WELCOME'.center(m,'-'))
 
 # bottom part
 for i in range(n//2-1,-1,-1):
     pattern='.|.'*(2*i+1)
     print(pattern.center(m,'-'))     
else:
    print("n must be odd and m must be 3 times n")
  
  
    
             
                                                                    