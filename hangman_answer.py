
import random

words = list()
picked = list()

def graphic(state): #0-5 for printing the hangman graphic
    graphic = (
        """
        *No Man :)*
        """,
        """
           0
        
        
        """,
        """
           0
           |
        
        """,
        """
           0
          -|
        
        """,
        """
           0
          -|-
        
        """,
        """
           0
          -|-
          /
        """,
        """
           0
          -|-
          / \\
        """,
    )
    print(graphic[state])


def collect():
    hold = ""
    while True:
        hold = input("Enter word to be played with, and enter \"play\" to start the game:").lower() #getting words
        if(hold in words):
            print("No repeats!")
            continue
        if hold=='play':
            if len(words)==0:
                print("I'm sorry, but try again:")
                continue
            else:
                break
        words.append(hold)

def game():
    if len(words)>0:
        ind = random.randint(0,len(words)-1)
        word = words[ind] #target word
        words.pop(ind)
    else:
        print("You tried all the words though!")
        return
    print("Game started and picked a word!")
    wordlen = len(word)
    tries = 6 #the amount of chances the player gets
    right = list() #store user guesses
    correct = 0 #keeps track of how many characters the player got correct

    while tries>0 and correct < wordlen:
        print("Word: ") 
        for i in range(0, wordlen): #displaying the letters player got right so far
            if(word[i] in right):
                print(word[i],end=' ')
            else:
                print('_',end=' ')
        print("You have guessed the following: \n" ) #displaying what the user guessed already
        print(*right, sep = ", ")
        hold = ""
        while True: #make sure it is only 1 character and not already guessed
            hold = input("\n You have: " + str(tries) + " left. Enter a character to guess:").lower() #guessing part
            if len(hold)!=1:
                print('I am sorry, but only 1 character!')
            elif hold in right:
                print("You already guessed that!")
            else:
                break
        right.append(hold)
        if word.count(hold)>0: #got at least 1 character right
            correct+=word.count(hold)
            print("\n Nice Job! \n")
        else: #got no character(s) right
            tries-=1
            print("\n Rip \n")
        graphic(6-tries)
        print("\n\n\n")

    if correct==wordlen:
        print("\nCongrats, you won! The word was: " + word)
    else:
        print("\nSorry :( , but the word was: " + word)
    print("\n\n\n\n\n")

def playagain():
    hold=""
    while hold!='Y' and hold!='N':
        hold = input("Would you like to play again? Y/N:").upper()
        if hold!='Y' and hold!='N':
            print("Sory, has to either be \"Y\" or \"N\"")
    if hold=='N':
        return False
    else:
        return True

def reset():
    hold = ""
    while hold!='Y' and hold!='N':
        hold = input("Would you like to reset the game?:").upper()
        if hold!='Y' and hold!='N':
            print("Sory, has to either be \"Y\" or \"N\"")
    if hold=='Y':
        words.clear()
        print("Resetted game!")
        return True
    else:
        return False

#driver
finished = True
collect()
while finished :
    game()
    finished = playagain()
    if finished:
        if reset():
            collect()
        
        

print("\n\tOkay, thanks for playing then!\n")

    