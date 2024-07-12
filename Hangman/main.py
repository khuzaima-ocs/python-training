from game_states import GameStates
from hangman import Hangman

if __name__ == "__main__":      
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