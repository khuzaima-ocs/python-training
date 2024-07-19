from tic_tac_toe import TicTacToe

if __name__ == "__main__":
    game = TicTacToe()

    print("""***** WELCOME TO TIC TAC TOE *****""")

    guide = """
1: Start
2: Quit
"""

    while True:

        print(guide)
        inp = int(input("Enter your choice: "))
        match inp:
            case 1:
                game.start()
                while True:
                    game.printBoard()
                    pos = int(input("Enter position: "))
                    game_status = game.turn(pos)
                    
                    if game_status == -1:
                        break

            case 2:
                print("Thanks for playing!")
                break

            case _:
                print("Invalid input!")