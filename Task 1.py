import os #module import

def Input():   #For getting Tasks

    os.system("cls")
    print("=========== TO-DO-LIST ===========\n")
    listtasks=[]
    btn='y'
    x=0
    while btn=='y':
     task=input(str(f"\nEnter your task {x+1}: "))
     listtasks.append(task)
     print("Choice one option:\n")
     print("y-> For new Task ")
     print("n-> For Exiting ")
     option=input (("\nOption: "))
     if option=='y':
       x=x+1
       btn='y'
       
     elif option=='n':
         btn='n'
         os.system("cls")
         return listtasks
        
         
         
         

def Display(listtasks):    #For Displaying Tasks
    os.system("cls")
    print("--------- Your Tasks ----------\n")
    for x in range(len(listtasks)):
        print(f"{x+1}:{listtasks[x]}")
    
        

def Done(listtasks):    #For Updating Tasks that are Done
    os.system("cls")
    print("--------- Updating Tasks ----------\n")
    while True:
      value=int (input("Enter the number of task you have done: "))
   
      if (value-1) in range(len(listtasks)):
       listtasks[value-1]=listtasks[value-1]+" --Done"
       return listtasks
       
      else:
        print("Invalid number of Task")
        
        continue
    
#mainbody of program

while True:
 print("=========== TO-DO-LIST ===========\n")
 

 print("1-> For Entering Your Tasks ")
 print("2-> For Viewing Your Tasks ")
 print("3-> For Updating Tasks ")
 print("4-> For Exiting Program ")

 get_option=int(input("Option: "))

 match get_option:   #Match cases for menu driven 
    case 1:
       
       tasks=Input()
       os.system("cls")    #Screen clear function
    case 2:
       if len(tasks)<=0:
           print("No Tasks Yet....!")
       else:
        Display(tasks)
        print("\n\n")

    case 3:
        if len(tasks)<=0:
           print("No Tasks Yet....!")
        else:
         Done(tasks)
         print("\n")
         Display(tasks)
         print("\n\n")
    case 4:
        os.system("cls")
        print("=========== TO-DO-LIST ===========\n")
        print("GoodBye......!")
        break
       






