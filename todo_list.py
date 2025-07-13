tasks=[]
def add_task():
    task=input(" enter a task :")
    tasks.append(task)
    print("task added successfully!  ")
    
def view_task():
     if not tasks:
         print("bde bhai khai hai mamla!")
     else:
        print("yeh hai thari todo_list :")
        for i , task in enumerate(tasks,1) :#  i number ke liye
                # task task string ke liye  # 1 mtlb starting from 1 
            print(f"{i}.{task}")        

def delete_task():
        view_task()
        try:
            number =int(input(" bte kaunse number wala task delete krna hai : :")) 
            if 1<=number<=len(tasks):
              removed=tasks.pop(number-1)
              print(f"deleted task :{removed}")
            else:
                    print("invalid number.")     
        except ValueError:
                print("plzzz    koi dhnka number dal")   
                
                
# abb bari hai main function ki 

while True:
        print('''
              -------- bta bhai kya kam krna hai------
              1. Add tasks.
              2. view tasks.
              3. delete tasks.
              4. exit 
              ''')    
        
        choice=input("enter kr ab koi valid number :")
        
        # ab wohi if-else ki bhsdd
        
        if choice=="1":
                add_task() 
        elif choice=="2":
                view_task()
        elif choice=="3":
                delete_task() 
        elif choice=="4":
                print("bhaut bhaut abhar apka ane ke liye we are glad ...")
                break
        else:
                print("abhi btaya tha ki dhnka number dal lekin nhai! ")                                        
                  
     
    
        
                         