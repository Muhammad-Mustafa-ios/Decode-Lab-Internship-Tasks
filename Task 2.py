import os  #importing module
def Input(items,expenses):   #Getting expenses input function
    
    x=0
    while True:
        name=(input("\nEnter Item name: "))
        items.append(name)
        money=int (input("\nEnter amount spend: "))
        expenses.append(money)
        print("1->Want to add more Expenses")
        print("2->Want to see your Expenses")
        option=int (input("\nOption:"))
        if option==1:
            x=x+1
            continue
        elif option==2:
            return items,expenses
            
        else:
            print ("Sorry,Invalid Option....! ")
            continue


def Display(items,expenses):    #Displaying function
    print("========= YOUR EXPENSES LIST =========\n")
    for x in range(len(items)):
        print(x+1,":",items[x],"---->",expenses[x])


def Calculation(expenses):   #Calculating Total funtion
      print("========= YOUR TOTAL EXPENSES  =========\n")
      total=0
      for x in range(len(expenses)):
          total=total+expenses[x]
      return total





#mainbody of program

items=[]          #Initializing lists
expenses=[]

while True:
 print("========= EXPENSES TRACKing SYSTEM =========\n")

 

 print("1-> For Entering Your Expenses ")
 print("2-> For Viewing Your Expenses ")
 print("3-> For Viewing Your Total Expenses ")
 print("4-> For Exiting Program ")

 get_option=(input("Option: "))   #Menu Drivens

 match get_option:   #Match cases for menu driven 
    case '1':
       
       Input(items,expenses)
       os.system("cls")    #Screen clear function
    case '2':                  #Displaying list of expenses
       os.system("cls")
       if len(items)<=0:
           print("No Expenses Yet,First Add Expenses!\n")
       else:
        Display(items,expenses)
        print("\n\n")

    case '3':              #Displaying Total
        if len(items)<=0:
           os.system("cls")
           print("No Expenses Yet,First Add Expenses!\n")
        else:
         os.system("cls")             
         print("========= EXPENSES TRACKing SYSTEM =========\n")
         Display(items,expenses)
         print("\n")
         print(Calculation(expenses))
         print("\n\n")
    case '4':                     #Closing program
        os.system("cls")
        print("========= EXPENSES TRACKing SYSTEM =========\n")
        print("GoodBye......!")
        break
    case _:   #Default case
        os.system("cls")
        print("Sorry,Invalid Option,Try Again....!\n")
        continue
        

