import random
import keyboard
import sys

class Board:

    def __init__(self, size = 10, bombCount = 10):
        self.size = size
        self.bombCount = bombCount
        self.board = [["[X]" for _ in range(self.size)] for _ in range(self.size)]
        self.data = {
            "dug": [],
            "bombs": []
        }
        self.setup()
    
    def getUnavailableSlots(self):
        return self.data["dug"]
    
    def isBomb(self, x, y):
        return (x,y) in self.data["bombs"]
    
    def setup(self):
        bombs = 0
        while (bombs <= self.bombCount):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if (x,y) in self.data["bombs"]:
                continue
            self.data["bombs"].append((x,y))
            bombs += 1
    
    def getSurroundingData(self, x, y):
        n = 0
        for r in range(max(0, x - 1), min(self.size, x + 2)):
            for c in range(max(0, y - 1), min(self.size, y + 2)):
                if (r == x and c == y):
                    continue
                if ((r, c) in self.data["bombs"]):
                    n += 1
        return n
    
    def dig(self, x, y):
        if (x,y) in self.getUnavailableSlots():
            print("This spot was already dug out please type in another splot's location")
        else:
            self.data["dug"].append((x,y))
            for r in range(max(0, x - 1), min(self.size, x + 2)):
                for c in range(max(0, y - 1), min(self.size, y + 2)):            
                    if r == x and c == y:
                        continue
                    if (r,c) in self.getUnavailableSlots():
                        continue
                    self.board[r][c] = "[" + str(self.getSurroundingData(r, c)) + "]"
    
    def dug(self):
        return len(self.data["dug"])
    
    def __str__(self):
        string = ""
        for x in range(self.size):
            for y in range(self.size):
                if (x,y) in self.getUnavailableSlots():
                    string += "[ ]"
                else:
                    string += str(self.board[x][y])
            string += "\n"
        
        return string
    

def startGame(size, bombs):
    board = Board(10,10)
    while (board.dug() < board.size ** 2 - board.bombCount):
        print(board)
        location = input("Please type in the coordinates you wish to dig in. (Example: \"1,1\")").strip().split(",")
        if len(location) < 2 or len(location) > 2:
            print("Please type in a valid value!")
            continue
        else:
            x = int(location[0]) - 1
            y = int(location[-1]) - 1
            if board.isBomb(x, y):
                print("GAME OVER!")
                print("Press a key to restart the game or press \'Esc\' to exit")
                if keyboard.is_pressed('esc'):
                    sys.exit()
                else:
                    startGame(size, bombs)
                break
            else:
                board.dig(x, y)
                continue
    print("Congratulations!!! You have won :D")
    print("Press a key to restart the game or press \'Esc\' to exit")
    if keyboard.is_pressed('esc'):
        sys.exit()
    else:
        startGame(size, bombs)

size = input("Please specify the size of the board.")
while not size.isdigit():
    size = input("Please specify the size of the board.")

bombCount = input("Please specify how many bombs you would like in the board")
while not bombCount.isdigit():
    bombCount = input("Please specify how many bombs you would like in the board")

startGame(size, bombCount) #Start the game :D
