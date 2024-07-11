from enum import Enum, auto
from random import choice
from draw_hangman import draw_hanged_man

class GameStates(Enum):
    NOT_STARTED = auto()
    STARTED = auto()
    COMPLETED = auto()

class Hangman:
    def __init__(self) -> None:
        self.turns_left = 0
        self.word = ""
        self.game_state = GameStates.NOT_STARTED
        self.guesses = []
        self.total_turns = 6
        self.words = []
        with open('words.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                self.words.append(line[:-1])    


    def start(self):
        if self.game_state == GameStates.STARTED:
            print("Game already started!!")
            return 
        
        self.guesses = []
        self.turns_left = self.total_turns
        self.game_state = GameStates.STARTED
        self.word = choice(self.words)
        print(self.word)

        self.print_game()

    def make_guess(self, guess):
        if self.game_state != GameStates.STARTED:
            print("Game has not started yet..")
            return
        
        if guess in self.guesses:
            print(f"'{letter}' already guessed..")
            return

        self.guesses.append(guess)
        index = self.word.find(guess)

        if index == -1:
            self.turns_left -= 1
            draw_hanged_man(self.total_turns - self.turns_left)
            print("Wrong guess..")
            if self.turns_left == 0:
                self.game_state = GameStates.COMPLETED
                print("You lost 😔")
                print(f"The word was {self.word}")

                print(f"\nYou guesses were {self.guesses}")
                return
        else:
            print("Correct guess..")
            
        self.print_game()

        if self.check_victory():
            self.game_state = GameStates.COMPLETED
            print("You won 🎉")

    def check_victory(self):
        for letter in self.word:
            if letter not in self.guesses:
                return False
    
        return True

    def print_game(self):
        
        for letter in self.word:
            if letter in self.guesses:
                print(f"{letter}", end=" ")
            else:
                print("-", end=" ")

        print(f"\nGuesses left: {self.turns_left}")
        print()

    def print_letters_remaining(self):
        print("Remaining letters are : [", end="")
        letters = list("abcdefghijklmnopqrstuvwxyz")

        for letter in letters:
            if letter not in self.guesses:
                print(f"{letter}, ", end="")
            
        print("]")
        

game = Hangman()

guide = """
1: Start/Restart Game
2: Make a guess
3: Exit"""

print("Welcome to HANGMAN GAME")

while True:
    if game.game_state == GameStates.STARTED:
        inp = 2
    else:
        print(guide)
        inp = int(input("\nEnter your choice: "))
    match inp:
        case 1:
            game.start()

        case 2:
            letter = input("Enter your guess (1 to check remaining letters) : ")
            if letter == "1":
                game.print_letters_remaining()
                continue
            elif len(letter) != 1:
                print("Invalid input..")
                continue
            
            game.make_guess(letter.lower())

        case 3:
            print("Thanks for Playing\n")
            break

        case _:
            print("Invalid input..")