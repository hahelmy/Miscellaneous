import random as r

words =[]

try:
    f=open("wordlist.txt")
except FileNotFoundError:
    print("File not found. Add a 'wordlist.txt' file with one word per line.")
    exit()
else:
   words = f.read().split('\n') # Create a list of words from file
   word = r.choice(words) # Choose a random word from words
   

guesses =[] # Attempted letters
guess =[] # The current progress

attempts = 10 # The number of attempts before the game is over

for _ in word: print(f"_", end=" ")
print("\n")

while True:
    guesses.append(input("Enter your guess: "))
    print("")
    for c in word:
        if c in guesses:
            print(f"{c}", end=" ") # print the correctly guessed letter
            guess.append(c)        # update the current progress
        else:
            print(f"_", end=" ")   # print a placeholder for the yet to be guessed letter
            guess.append("_")      # update the current progress
            
    if not '_' in guess: # if no uknown letters ramaing the game has been won
        print(f"\n\nGood job.. You guessed '{word}' with {attempts} attempt(s) to spare.\n")
        break
    else:
        guess=[]
    attempts -=1
    print(f"\n\nYou have {attempts} attempts left.\n")
    
    if attempts <= 0: # game is lost if no attempts remain and the word was not guessed
       print(f"Game over.. The word was '{word}'") 
       break      

