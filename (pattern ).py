
#i=int(input("Enter the number of rows you want in the pattern :"))
#for a in range(1,i+1):
#    for b in range(1,a+1):
#        print("*",end=" ")   
#    print()
#    # agli line main jane ke liye print() function use kiya hai
#   
#for a in range(1,i+1):
#    for b in range(1,a+1):
#        print(b,end=" ")   
#    print()
#    # agli line main jane ke liye print() function use kiya hai
#for a in range(i,0,-1):
# print("*"*a)
#    
#for a in range(i,0,-1):
#    for b in range(1,a+1):
#        print(b,end=" ")
#    print()    
#    

#n=("*")
#row=int(input("Enter the number of rows you want in the pattern :"))
#for i in range(1,row+1):
#    print(n*i)
#print(" ")    
#
#for i in range(row,0,-1):
#    print(n*i)
#print(" ")    
#
#for i in range(1,row+1):
#    space=row-i
#    star=i
#    print(" "*space+n*star)
#print(" ")
#    
#    
#for i in range(row,0,-1):
#    #space=row-i
#    #star=i
#    print(" "*(row-i)+n*i)  
#print(" ")     
#    
#for i in range(1,row+1):
#    space=row-i
#    star=2*i-1
#    print(" "*space+n*star) 
#print(" ")   
#    
#for i in range(row,0,-1):
#    space=row-i
#    star=(2*i)-1 
#    print(" "*space+star*n)      
#print(" ")
#for i in range(1,row+1):
#    for j in range(1,i+1):
#        print(j,end=" ")
#    print()  
#print() 
#for i in range(row,0,-1):
#    for  j in range(1,i+1):
#        print(j, end=" ")
#    print()        
#print( )    
#
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
  
  
    
   