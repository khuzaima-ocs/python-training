from draw_hangman import draw_hanged_man
from game_states import GameStates
from random import choice

class Hangman:
    def __init__(self) -> None:
        self.turns_left = 0
        self.word = ""
        self.game_state = GameStates.NOT_STARTED
        self.guesses: list[str] = []
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

        self.print_game()

    def make_guess(self, guess):
        if self.game_state != GameStates.STARTED:
            print("Game has not started yet..")
            return
        
        if guess in self.guesses:
            print(f"'{guess}' already guessed..")
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
    