import random     #random module
import string      #string module
import os     #screen clearing module
def random_password():     #main function to generate a strong password
 print("--- Enter a strong password.....\n")
 while True:
  password=input("* Password: ")
  if len(password)>=8:
    random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    os.system("cls")
    print("=========== Strong Password Generator ==================\n") 
    print(f"* Your Password:{password}")
    print(f"* Suggested Password:{random_password}\n")
    break
  else:
      print("--- password must have atleast 8 characters.\n")

 


#main body
print("=========== Strong Password Generator ==================\n")     
random_password()