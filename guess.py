import random
rand_= random.randint(1,2)
count = 3
for i in range(3):
    print(f"You have {count} attempts remaining\n")
    guess = int(input("Guess the number from 1 to 10\n"))
    
    if guess == rand_:
        print ("\nCongratulations!..you have guessed correctly\n")
        break
    else:
        count = count-1
        if count>0:
            print("\nIncorrect! Try again please\n")
        else:
            print("\nIncorrect! \nBetter luck next time\n")
        

        


