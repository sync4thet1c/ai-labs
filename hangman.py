import random
import time

#initial steps to invite in the game:
print("\nWelcome to Hangman game\n")
name = input("Enter your name: ")
print("Hello " + name + " !")

def main():
    global count, display, word, already_guessed,length
    words_to_guess = ['january', 'border','monday', 'year', 'programmer', 'authentic', 'lungs', 'planets', 'children']
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = "_"*length
    already_guessed = []
    
def hangman():
    global count, display, word,already_guessed
    limit = 5
    guess = input("This is the Hangman Word.Enter your guess: " + display + "\n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip())>= 2 or guess <= "9":
        print("Invalid input, Try a letter\n")
        hangman()
        
    elif guess in word:
        already_guessed.extend([word])
        index = word.find(guess)
        word = word[:index] + "_" + word[index+1:]
        display = display[:index] + guess + display[index+1:]
        print(display + "\n")
        
    elif guess in already_guessed:
        print("Try another letter\n")
        
    else:
        count += 1
        
        if count == 1:
            print("   _______\n"
                  "|     |\n"
                  "|     \n"
                  "|     \n"
                  "|     \n"
                  "|     \n"
                  "|     \n"
                  "|     \n")
            print("Wrong Guess. " + str(limit-count) + "guesses remaining\n")
            
        elif count == 2:
            print("   _______\n"
                  "|     |\n"
                  "|     |\n"
                  "|     \n"
                  "|     \n"
                  "|     \n"
                  "|     \n"
                  "|     \n")
            print("Wrong Guess. " + str(limit-count) + "guesses remaining\n")
            
        elif count == 3:
            print("   _______\n"
                  "|     |\n"
                  "|     |\n"
                  "|     O\n"
                  "|     \n"
                  "|     \n"
                  "|     \n"
                  "|     \n")
            
        elif count == 5:
            print("   _______\n"
                  "|     |\n"
                  "|     |\n"
                  "|     |\n"
                  "|     O\n"
                  "|    /|\ \n"
                  "|     |\n"
                  "|     \n")
            print("Wrong Guess. " + str(limit-count) + "guesses remaining\n")
            print("Wrong Guess. " + str(limit-count) + "guesses remaining\n")
            
        elif count == 4:
            print("   _______\n"
                  "|     |\n"
                  "|     |\n"
                  "|     O\n"
                  "|    /|\ \n"
                  "|     |\n"
                  "|     \n"
                  "|     \n")
            print("Wrong Guess. " + str(limit-count) + "guesses remaining\n")
            
        elif count == 5:
            print("   _______\n"
                  "|     |\n"
                  "|     |\n"
                  "|     |\n"
                  "|     O\n"
                  "|    /|\ \n"
                  "|     |\n"
                  "|    / \ \n")
            print("Wrong guess. You are hanged!\n")
            # print(already_guessed)
            print("The word was: "," ".join(already_guessed)[:length])
                       
    if word == "_" * length:
        print("Congratulations" + name + "! You have guessed the word correctly!")
    
    elif count != limit:
        hangman()
    
main()
hangman()   