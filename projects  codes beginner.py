            ########### number guessing game #########



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



          ########## rock paper scissor game ##########
          
#import random
#l=["rock","paper","scissor"]   
#
#
#while True:
#    uc=input('''
#             game start......
#             yes
#             no
#             exit
#             
#             
#             
#             
#        ''')
#    if uc=="yes":
#        for i in range(1,4):
#         choice=input("enter your choice :")
#         comp=random.choice(l)
#         print(comp)
#         
#         if choice==comp:
#             print("tie")
#             
#         elif (choice=="rock" and comp=="scissor")  or (choice=="paper" and comp=="rock") or (choice=="scissor" and comp=="paper"):
#             print("u win")
#         else:
#             print("u lose")     
#             
#    else:
#        print("")        
        
        ####### rock paper scissor game ####
    
#import random
#l=["rock","paper","scissor"]
#
#
#while True:
#    uc=int(input('''
# GAME STARTS ..........
# 1 -----> YES
# 2------> NO |EXIT
#'''))
#    if uc==1:
#       user_win=0
#       comp_win=0
#       for a in range(1,6):
#            user=int(input("enter your input :"))
#            
#            
#            if user==1:
#                uchoice="rock"
#            elif user==2:
#                uchoice="paper"
#            elif user==3:
#                uchoice="scissor"
#            else:
#                print("invalid")
#                continue   
#            print(uchoice) 
#            computer=random.choice(l)
#            print(computer)
#        
#            if uchoice==computer:
#                print("its a tie.")
#            elif (uchoice=="rock" and computer=="scissor") or (uchoice=="paper" and computer=="rock")or (uchoice=="scissor"and computer=="rock"):
#                print("you win this round")
#                user_win += 1
#            else:
#                print("you lose this round")
#                comp_win += 1
#       print("\n------final score----")         
#       print("you win :",user_win,"rounds")
#       print("comp win :",comp_win,"rounds")
#       if user_win > comp_win :
#           print("you win")
#       elif user_win < comp_win :
#           print("comp win ")
#       else:
#           print("its a tie")       
#           
#    elif uc ==2:
#        print("exiting the game")   
#        break
#    else:
#        print("invalid input")             
#                
#                
#                
#                
#                
#                
#                
#                
#                
#                
#                        
#             
#
#import random
#l = ["rock", "paper", "scissor"]
#
#while True:
#    uc = int(input('''
# GAME STARTS ..........
# 1 -----> YES
# 2 -----> NO | EXIT
#    '''))
#
#    if uc == 1:
#        user_win = 0
#        comp_win = 0
#
#        for a in range(1, 6):
#            print("\nRound", a)
#            print("1: Rock, 2: Paper, 3: Scissor")
#            user = int(input("Enter your input (1/2/3): "))
#
#            if user == 1:
#                uchoice = "rock"
#            elif user == 2:
#                uchoice = "paper"
#            elif user == 3:
#                uchoice = "scissor"
#            else:
#                print("Invalid input! Try again.")
#                continue
#
#            print("You chose:", uchoice)
#            computer = random.choice(l)
#            print("Computer chose:", computer)
#
#            if uchoice == computer:
#                print("It's a tie.")
#            elif (uchoice == "rock" and computer == "scissor") or \
#                 (uchoice == "paper" and computer == "rock") or \
#                 (uchoice == "scissor" and computer == "paper"):
#                print("You win this round!")
#                user_win += 1
#            else:
#                print("Computer wins this round!")
#                comp_win += 1
#
#        # Final results
#        print("\n--- Final Score ---")
#        print("You won:", user_win, "rounds")
#        print("Computer won:", comp_win, "rounds")
#
#        if user_win > comp_win:
#            print("🎉 You win the game!")
#        elif user_win < comp_win:
#            print("💻 Computer wins the game!")
#        else:
#            print("🤝 It's a draw!")
#
#    elif uc == 2:
#        print("Exiting the game. Bye!")
#        break
#    else:
#        print("Invalid input. Please enter 1 or 2.")

                 #    ######  # dice roll game #####

#import random 
#
#while True:
#    play=input("roll the dice ? (yes/no)")
#    if play =="no":
#        print("game over!")
#        break
#    user_win=0
#    comp_win=0
#    for a in range(1,4):
#     user_roll=random.randint(1,6)
#     comp_roll=random.randint(1,6)
#    
#     print("you rolled :",user_roll)
#     print("comp rolled :",comp_roll)
#    
#     if user_roll<comp_roll:
#        print("comp wins")
#        comp_win+=1
#     elif user_roll>comp_roll:
#         print("you win")  
#         user_win+=1
#     else:
#         print("its a tie") 
#         continue  
#    print("------final result-----")
#    print(user_win)
#    print(comp_win)
#    
#    if user_win>comp_win:
#        print("you won the game")  
#    elif user_win<comp_win:
#        print("comp won the game") 
#    else:
#        print("its a tie")        
             
            #    


#tasks=[]
#def add_task():
#    task=input(" enter a task :")
#    tasks.append(task)
#    print("task added successfully!  ")
#    
#def view_task():
#     if not tasks:
#         print("bde bhai khai hai mamla!")
#     else:
#        print("yeh hai thari todo_list :")
#        for i , task in enumerate(tasks,1) :#  i number ke liye
#                # task task string ke liye  # 1 mtlb starting from 1 
#            print(f"{i}.{task}")        
#
#def delete_task():
#        view_task()
#        try:
#            number =int(input(" bte kaunse number wala task delete krna hai : :")) 
#            if 1<=number<=len(tasks):
#              removed=tasks.pop(number-1)
#              print(f"deleted task :{removed}")
#            else:
#                    print("invalid number.")     
#        except ValueError:
#                print("plzzz    koi dhnka number dal")   
#                
#                
## abb bari hai main function ki 
#
#while True:
#        print('''
#              -------- bta bhai kya kam krna hai------
#              1. Add tasks.
#              2. view tasks.
#              3. delete tasks.
#              4. exit 
#              ''')    
#        
#        choice=input("enter kr ab koi valid number :")
#        
#        # ab wohi if-else ki bhsdd
#        
#        if choice=="1":
#                add_task() 
#        elif choice=="2":
#                view_task()
#        elif choice=="3":
#                delete_task() 
#        elif choice=="4":
#                print("bhaut bhaut abhar apka ane ke liye we are glad ...")
#                break
#        else:
#                print("abhi btaya tha ki dhnka number dal lekin nhai! ")                                        
#                  
     
    
        
                         