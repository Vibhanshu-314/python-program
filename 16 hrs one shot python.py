#print("first program ")
#num = int(input("Enter the value of the number for its multiplication table: "))
#num_1 = int(input("Till what number do you want the table? "))
#
#for i in range(1, num_1 + 1):
#    print(f"{num} x {i} = {num * i}")
#print()
#
v="vibhanshu kumar"
#w=v.lower()
#print(w)
#
#print(v.upper())
#print(v.capitalize())
print(v.title())
#print()
#print(v.find("i"))
#print(v.find("u",3))

#user_input=input("enter the name in capitals letter: ")
#
#if user_input.isupper() and user_input.isalpha():
#    print("user_input is valid input")
#    
#
#else:
#    print("invalid input")
#a=66;
#print(chr(a))
# for printing aplhabet using their character ASCII code
#or a in range(65,91,1):
#   print(chr(a))
#   print()
#hum ek sentence same rkh rhe hai lekin noun jese words wkt ke sth change kr skt hai 
#user_input="hi {} ki haal hai  "
#print(user_input.format("divya"))
#print(user_input.format("radha"))
#print(user_input.format("nvya"))
#print(user_input.format("manvi"))

list=[1,2,3,[4,5,6]]
print(list[3])
print(list[3][1]) 
print(list[0: :3])
print(list[-1:2:-1])

##marks_list=[90,99,100,95,91]
#print(f"{marks_list[0]}\n{marks_list[3]}")
#for n in range(len(marks_list)):# range( )sirf int value leta hai list nahi
   # print(marks_list[n])
    
#marks_list.pop(1)   
#marks_list.append(90)
#print(marks_list)
#marks_list.insert(2,10)
#print(marks_list)

#purposse is to diffrentiate the odd and even number in different list
#l_even=[]
#l_odd=[]
#for n in range(1,101):
#    if (1<=n<101):
#        if (n % 2 == 0):
#            
#            l_even.append(n)
#        else:
#            l_odd.append(n)    
#    else:
#        print("enter the number b/w 1 to 100")
#print(l_even)
#print(l_odd)
#print("new day")  
#n=[m for m in range(1,101)]
#print(n) 
#n=[m for m in range(1,51) if m%2==0 ]    #list main hi looop use kia jisse asam ho ajye kamm or do conditioj use ho gyi for loop or if statement    of issme m for m   smme hi rhn chahiye wrna value store nhi hogi
#
#print(n)
#    
#v="vibhanshu"
#alpha=[n for n in v]
#print(alpha)
#print(alpha.count("h"))# count ka use krke hum pta lga skte hai kki list main kitne ek jeese item hai  or lekin hum jese h ko qoutes main likhna anivarye hai  
#
#l=["vashu","vashu","vibh","vibhanshu"]
#print(max(l))
#print(l.sort())
#name="vibhanshu"
#print(name[::-1])
#
#rint()
#
#ame=["chitwan","divya","navya","parth","rudra","sujal","sudhakar","vibh","yash"]
#oll_no=[3,4,15,16,20,26,28,32,33]
#or a,b in zip(name,roll_no):
#  print(a,b)
#  
#  
#rint()
#or h in range(len(name)):
#  print(name[h],roll_no[h])   
#n =input("enter the string")
#print(n.split())   # spllit( ) yha pe koi bhi string ko list mai co vert kr ra hai

#l=[]
#for i  in range(1,4):
#   n=input("enter the color name : ")
#   l.append(n)  
#print(l)    


          # # # # # # #    new  day ( stack )
          
#l=[]
#while True:
#   c=int(input('''
#      1 push elements
#      2 pop elements
#      3 peek elements
#      4 display elements
#      5 exit
#      :
#      '''))
#   if c==1:
#      n=input("enter the vslue to push in stack :")
#      l.append(n) 
#      print(l) 
#   elif c==2:
#       if len(l)==0:
#          print("stack is empty")     
#       else:
#        print(l.pop()) 
#   elif c==3:
#       print("last value is :",l[-1]) 
#   elif c==4:
#      print("stack : ",l)  
#   elif c==5:
#      break;        
#   else:
#      print("invalid input")
      
      
          ####### queue in python #####
#d={
#   "name":"python",
#   "fees": 8000,          
#  "duration_hrs":2
#   
#  }
#
#print(d["name"])
#print(d["fees"])

#for (a,b) in d.items():
#   print(a,b)
#   
#print(d.pop("name"))
#
#
#d=dict(name="python",fees=3000)
#print(d)
#
#d.update({"fees":10000})
#print(d)

#tupple=(4,2,3,1)
#for i in range(len(tupple)):
#   print(tupple[i])
#print(sum(tupple))   
#print(max(tupple))
#print(sorted(tupple))
#print(tupple.index(3))
#print(type(tupple))


#t=(8,7,6,5)
#l=[]
#for i in range(len(t)):
#   print(t[i])
#   l.append(t[i])
#print(l)   

       # # # ## # #  function ##########
 

# phle to def krenge using def  
#def square_data(a,b) : 
#   
#   print(pow(a,b))  
#
#square_data(2,2)
#
#
#print(square_data) 

### ab hum user input le rhe hai ###

#def square(a,b):
#   return pow(a,b)
#a=int(input("enter the value of a :"))
#b=int(input("enter the value of b :"))
#
#square(a,b)
#print(pow(a,b))
#or
#print(f"{a} raised to the power {b} is :{pow(a,b)}")


#import math
##x=12.8
##print(math.ceil(x))
## age ki value deta hai
#
## floor peeche ki vlau dega
#
#x=-20
#print(math.fabs(x))
## positive value deta hai
#
#print(math.factorial(3))
#
#l=[9,8,7,6,5,4,3,2,1]
#print(math.fsum(l))
##sum keke dedega list le members ki
#
#
#print(math.sqrt(81))
#



##############    random module ######

#import random
#print(random.randint(1,10))
#
#
#print(random.randrange(1,10))
#
#l=["bat","balls","wkts"]
#print(random.choice(l))


#####            python dates

#import datetime
#
#
#print(datetime.datetime.now())



#import random
#
#user_input=int(input("Enter Your Number :------>"))
#random_num=random.randint(1,100)
#print(random_num)
#if (user_input <random_num):
#   print("your guess is low")
#elif(user_input>random_num):
#   print("your guess is high")
#else:
#   print("correct guess")      
#


import json
# used in API   yeah ek text format mm hota hai
#d={
#   'course_name':'python', #dic format m hi hotA HAI
#   'fees':15000
#}
#f=json.dumps(d)
#print(f) 
## str type m output milega
#print(type(f))


#d='{"course_name":"python","fees":15000,"duration":"2 months"}'
#
#x=json.loads(d)
#print(type(x))
#for a in x:
#   print(a)
#