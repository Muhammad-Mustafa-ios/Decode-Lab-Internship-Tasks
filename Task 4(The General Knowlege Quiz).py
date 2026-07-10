
import os  #Screen clearing module
import time   #Time module

def slow_print(text, delay=0.05):  #slow printing function
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def Input(question_list,answer_list):    #Taking questions from user
    value=int(input("-->> How many Questions do you want to enter: "))
    for x in range(value):
        question=input(f"\n* Enter your question {x+1}: ")
        question_list.append(question)
        answer=input(f"\n-> Enter its Answer: ").lower()   #Anwers from user
        answer_list.append(answer)
    return question_list,answer_list



def Quiz(question_list,answer_list):    #Asking from users
       score=0
       for x in range(len(question_list)): 
         print(f"{x+1}:{question_list[x]}")
         answer=input("* Answer: ").lower()
         if answer==answer_list[x]:
             slow_print("Correct Answer,great......!\n")
             score=score+10
         else:
             score=score-2   #scoring
             slow_print("Wrong Answer,Good Try.......!\n")
       
       return score





        

    

#Main Body


questions=[]
answers=[]
print("============ The GK Quiz ===============\n")
slow_print("First You have to Enter your Qustions in the system.\n")
questions,answers=Input(questions,answers)
os.system("cls")
print("============ The GK Quiz ===============\n")
slow_print("\nNow,Quiz is going to start.....................\n")
score=Quiz(questions,answers)
os.system("cls")
slow_print("============ The GK Quiz ===============\n")
slow_print("============ Score Board ===============\n")
print(f"Your Score: {score}")
 
     

