class Game:
    def __init__(self, id):
        self.p1Moved = False
        self.p2Moved = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

    def getPlayerMoves(self, p):
        #p between 0 and 1
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Moved = True
        else:
            self.p2Moved = True

    def connected(self):
        return self.ready

    def bothMoved(self):
        return self.p1Moved and self.p2Moved

    def winner(self):
        #only have to compare first letter of move
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        return winner

    def resetMoves(self):
        self.p1Moved = False
        self.p2Moved = False
