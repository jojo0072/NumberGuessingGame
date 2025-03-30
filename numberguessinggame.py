# Determine number 1-100, User Input, Check if divisible by five, three, two(odd), prime number, perfect square, fibonacci, higher, lower (changes)

import random

def main():
    num=random.randint(1, 100)
    print("Number Guessing Game\n")
    tips=[]
    tipsf(num, tips)      
    while True:
        user_input=input("Guess a number between 1 and 100: ")
        if not(user_input.isdigit()) or int(user_input) not in range(1, 100):
            print("Invalid Input")
            continue
        if int(user_input) != num:
            print("Wrong guess!")
            if higher_lower(num, user_input):
                tips.append("Guess higher!")
            else:
                tips.append("Guess lower!")                  
            choice=random.choice(tips)
            if choice != tips[-1]:
                tips.remove(choice)
            del tips[-1]          
            print("Tip:", choice)   
        else:
            print("You guessed the number correctly!\n")
            play_again()    
            
def tipsf(num,tips):                     
    tips.extend(div_mult(num))
     
    if prime(num):
        tips.append("It's a prime number!")
    else:
        tips.append("Not a prime number!")           
        
    if square(num):
       tips.append("Number is a perfect square!")
    else:
       tips.append("Not a perfect square!")  
    
    if fib(num):
       tips.append("Number is in the fibonacci sequence!")
    else:
       tips.append("Number is not part of the fibonacci sequence!")       
                 
    return tips  

def div_mult(num):
    random_list=set(list(random.randint(2, 9) for _ in range(4)))
    div_multl=[]
    for x in random_list:
        if num % x == 0:
            div_multl.append(f"Divisible by {str(x)}!")
        else:
            div_multl.append(f"Not a multiple of {str(x)}!")    
    return div_multl        
            
def higher_lower(num, user):
         return int(user) < num
                           
def prime(num):
         for x in range(2, num):
                if num % x == 0:
                    return False                                                                                   
                if num == num-1:
                    return True           
                    
def square(num):
          first=pow(num, 0,5)                           
          return pow(first, 2) == num

def fib(num):
    d= [0, 1]
    while d[-1] < 100:
        d.append(d[-1] + d[-2])        
        if num == d[-1]:
            return True    
    return False    

def play_again():
      again=input("Play again (y/n): \n").lower()
      if again !="y":
          exit()
      else:
          main()                                                                                                                                                                                                                                               
                                                            
main()            