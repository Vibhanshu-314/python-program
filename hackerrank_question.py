#thickness=int(input())
#c='H'
#i=0
#while i<thickness:
#    left=(c*i).rjust(thickness)
#    right=(c*i).ljust(thickness)
#    print(left+c+right)
#    #print(left)
#    i+=1
#    
#i=0
#while i<thickness  

#for i in range(9 // 2 - 1, -1, -1):
#    x="*"
#    print(x*(2*i+1))

#n,m=map(int,input().split())
#if n % 2 == 1 and m == n * 3:
## top part
# for i in range(n//2):
#     pattern='.|.'*(2*i+1)
#     print(pattern.center(m,'-'))
#     
# # middle part
# print('WELCOME'.center(m,'-'))
# 
# # bottom part
# for i in range(n//2-1,-1,-1):
#     pattern='.|.'*(2*i+1)
#     print(pattern.center(m,'-'))     
#else:
#    print("n must be odd and m must be 3 times n")
#  
#from itertools import product 
#def itertool(a,b):
#    ans=list(product(a,b))
#
#    return ans
#
#
#
#if __name__ == "__main__":
#     a=list(map(int,input("enter a:").split()))
#     b=list(map(int,input("enter b:").split()))
#     
#     result=itertool(a,b) 
#     print("cartesian product",result)
#      

#from collections import Counter
#
#x=int(input())
#shoe_sizes=list(map(int,input().split()))
#
#inventory=Counter(shoe_sizes)
#n=int(input())
#earning=0
#for _ in range(n):
#    size,price=map(int,input().split())
#    if inventory(size)>0:
#        earning+=price
#        inventury-=1
#print(earning)





# set hai topic

n=int(input())
arr=[]
sum=0
for i in range(n):
    x=int(input())
    arr.append(x)

unique_value=set(arr)
total=sum(unique_value)

avg=total/len(unique_value)

print(avg)
    