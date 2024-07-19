from random import choice

class TicTacToe:
    def __init__(self):
        self.start()

    def start(self):
        self.board = [f"{x}" for x in range(10)]
        self.player = choice(['X','O'])

    def printBoard(self):
        print ( "     |     |    ")
        print ("  "+self.board[1]+"  |  "+self.board[2]+"  |  "+self.board[3]+"  ")
        print ("     |     |")
        print ("-----|-----|----")
        print ( "     |     |    ")
        print ("  "+self.board[4]+"  |  "+self.board[5]+"  |  "+self.board[6]+"  ")
        print ("     |     |")
        print ("-----|-----|----")
        print ( "     |     |    ")
        print ("  "+self.board[7]+"  |  "+self.board[8]+"  |  "+self.board[9]+"  ")
        print ("     |     |")

        print(f"\nPlayer {self.player}'s turn")
        print("----------------------------")

    def change_player(self):
        self.player = 'X' if self.player == 'O' else 'O'

    def check_victory(self):
        # Checking Rows
        for i in [1,4,7]:
            if self.board[i] == self.board[i+1] == self.board[i+2] and self.board[i] == self.player:
                return True

        # Checking Cols
        for i in range(1, 4):
            if self.board[i] == self.board[i+3] == self.board[i+6] and self.board[i] == self.player:
                return True

        # Checking Main Diagonal
        if self.board[1] == self.board[5] == self.board[9] and self.board[1] == self.player:
            return True
        
        # Checking Cross Diagonal
        if self.board[3] == self.board[5] == self.board[7] and self.board[3] == self.player:
            return True

        return False

    def is_gameover(self):
        for i in range(1, 10):
            if self.board[i] == str(i):
                return False
            
        return True

    def turn(self, pos: int):
        if self.board[pos] == str(pos):
            self.board[pos] = self.player

            if self.check_victory():
                self.printBoard()
                print(f"Congratulation, {self.player} won the game!! 🎉")
                return -1
            
            if self.is_gameover():
                self.printBoard()
                print("Game over!!")
                return -1
            
            self.change_player()

        else:
            print("Already filled...")
