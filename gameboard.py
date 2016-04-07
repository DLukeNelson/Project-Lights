

class GameBoard:
    def __init__(self):
        self.redTurn = True
        self.tiles = list()
        for i in range(12):
            for j in range(12):
                a = Tile()
                a.row = i
                a.col = j
                a.paths[(i-1, j)] = (i+1, j)
                a.paths[(i+1, j)] = (i-1, j)
                a.paths[(i, j-1)] = (i, j+1)
                a.paths[(i, j+1)] = (i, j-1)
                a.paths[(i+1, j+1)] = (i-1, j-1)
                a.paths[(i-1, j+1)] = (i+1, j-1)
                a.paths[(i+1, j-1)] = (i-1, j+1)
                a.paths[(i-1, j-1)] = (i+1, j+1)
                if i == 0 or i == 11:
                    a.paths[(i-1, j)] = None
                    a.paths[(i+1, j)] = None
                if j == 0 or j == 11:
                    a.paths[(i, j-1)] = None
                    a.paths[(i, j+1)] = None
                if i == 0 or i == 11 or j == 0 or j == 11:
                    a.paths[(i+1, j+1)] = None
                    a.paths[(i-1, j+1)] = None
                    a.paths[(i+1, j-1)] = None
                    a.paths[(i-1, j-1)] = None
                if j == 3 and i == 4:
                    for k in a.paths:
                        a.paths[k] = None
                    a.id = -1
                    a.img = 1
                elif j == 3 and i == 7:
                    for k in a.paths:
                        a.paths[k] = None
                    a.id = -1
                    a.img = 2
                if (i == 0 and j == 5) or (i == 1 and j == 3) or (i == 2 and j == 4) or (i == 11 and j == 5) or (i == 10 and j == 3) or (i == 9 and j == 4):
                    a.block(self)
                if i > 2 and i < 9 and j > 1 and j < 5:
                    a.used = True
                self.tiles.append(a)


    def LaserRed(self):
        for atile in range(144):
            self.tiles[atile].red = set()
        red = (4,3)
        redtile = (4,4)
        while redtile:
            rednext = self.tiles[ redtile[0]*12 + redtile[1] ].redlaser(red)
            red = redtile
            redtile = rednext

    def LaserBlue(self):
        for atile in range(144):
            self.tiles[atile].blue = set()
        blue = (7,3)
        bluetile = (7,4)
        while bluetile:
            bluenext = self.tiles[ bluetile[0]*12 + bluetile[1] ].bluelaser(blue)
            blue = bluetile
            bluetile = bluenext


class Tile:
    def __init__(self):
        self.img = 0
        self.id = 0
        self.paths = {}
        self.row = None
        self.col = None
        self.used = False
        self.red = set()
        self.blue = set()

    def mirror1(self, board):
        print(str((self.row, self.col)) + ' mirror1')
        if not self.used:
            if (board.redTurn and self.blue and not self.red) or (not board.redTurn and self.red and not self.blue):
                print('a')
                return
            for k in self.paths:
                self.paths[k] = None
            self.id = 1
            self.img = 5
            if self.row != 0 and self.col != 0:
                self.paths[(self.row-1, self.col)] = (self.row, self.col-1)
                self.paths[(self.row, self.col-1)] = (self.row-1, self.col)
            self.used = True
            board.redTurn = not board.redTurn

    def mirror2(self, board):
        print(str((self.row, self.col)) + ' mirror2')
        if not self.used:
            if (board.redTurn and self.blue and not self.red) or (not board.redTurn and self.red and not self.blue):
                print('a')
                return
            for k in self.paths:
                self.paths[k] = None
            self.id = 2
            self.img = 6
            if self.row != 0 and self.col != 11:
                self.paths[(self.row-1, self.col)] = (self.row, self.col+1)
                self.paths[(self.row, self.col+1)] = (self.row-1, self.col)
            self.used = True
            board.redTurn = not board.redTurn

    def mirror3(self, board):
        print(str((self.row, self.col)) + ' mirror3')
        if not self.used:
            if (board.redTurn and self.blue and not self.red) or (not board.redTurn and self.red and not self.blue):
                print('a')
                return
            for k in self.paths:
                self.paths[k] = None
            self.id = 3
            self.img = 7
            if self.row != 11 and self.col != 11:
                self.paths[(self.row+1, self.col)] = (self.row, self.col+1)
                self.paths[(self.row, self.col+1)] = (self.row+1, self.col)
            self.used = True
            board.redTurn = not board.redTurn

    def mirror4(self, board):
        print(str((self.row, self.col)) + ' mirror4')
        if not self.used:
            if (board.redTurn and self.blue and not self.red) or (not board.redTurn and self.red and not self.blue):
                print('a')
                return
            for k in self.paths:
                self.paths[k] = None
            self.id = 4
            self.img = 8
            if self.row != 11 and self.col != 0:
                self.paths[(self.row+1, self.col)] = (self.row, self.col-1)
                self.paths[(self.row, self.col-1)] = (self.row+1, self.col)
            self.used = True
            board.redTurn = not board.redTurn

    def lensX(self, board):
        print(str((self.row, self.col)) + ' lensX')
        if not self.used:
            if (board.redTurn and self.blue and not self.red) or (not board.redTurn and self.red and not self.blue):
                print('a')
                return
            for k in self.paths:
                self.paths[k] = None
            self.id = 5
            self.img = 3
            if self.row != 0 and self.col != 0 and self.col != 11:
                self.paths[(self.row, self.col+1)] = (self.row-1, self.col-1)
                self.paths[(self.row-1, self.col+1)] = (self.row, self.col-1)
            if self.row != 0 and self.row != 11 and self.col != 0:
                self.paths[(self.row-1, self.col)] = (self.row+1, self.col-1)
                self.paths[(self.row-1, self.col-1)] = (self.row+1, self.col)
            if self.row != 11 and self.col != 0 and self.col != 11:
                self.paths[(self.row, self.col-1)] = (self.row+1, self.col+1)
                self.paths[(self.row+1, self.col-1)] = (self.row, self.col+1)
            if self.row != 0 and self.row != 11 and self.col != 11:
                self.paths[(self.row+1, self.col)] = (self.row-1, self.col+1)
                self.paths[(self.row+1, self.col+1)] = (self.row-1, self.col)
            self.used = True
            board.redTurn = not board.redTurn

    def lensY(self, board):
        print(str((self.row, self.col)) + ' lensY')
        if not self.used:
            if (board.redTurn and self.blue and not self.red) or (not board.redTurn and self.red and not self.blue):
                print('a')
                return
            for k in self.paths:
                self.paths[k] = None
            self.id = 6
            self.img = 4
            if self.row != 11 and self.col != 0 and self.col != 11:
                self.paths[(self.row, self.col+1)] = (self.row+1, self.col-1)
                self.paths[(self.row+1, self.col+1)] = (self.row, self.col-1)
            if self.row != 0 and self.row != 11 and self.col != 0:
                self.paths[(self.row+1, self.col)] = (self.row-1, self.col-1)
                self.paths[(self.row+1, self.col-1)] = (self.row-1, self.col)
            if self.row != 0 and self.col != 0 and self.col != 11:
                self.paths[(self.row, self.col-1)] = (self.row-1, self.col+1)
                self.paths[(self.row-1, self.col-1)] = (self.row, self.col+1)
            if self.row != 0 and self.row != 11 and self.col != 11:
                self.paths[(self.row-1, self.col)] = (self.row+1, self.col+1)
                self.paths[(self.row-1, self.col+1)] = (self.row+1, self.col)
            self.used = True
            board.redTurn = not board.redTurn

    def block(self, board):
        if not self.used:
            if (board.redTurn and self.blue and not self.red) or (not board.redTurn and self.red and not self.blue):
                return
            for k in self.paths:
                self.paths[k] = None
            self.id = -1
            self.img = 9
            self.used = True
            board.redTurn = not board.redTurn

    def redlaser(self, inpair):
        out = self.paths[inpair]
        self.red.add(inpair)
        return out

    def bluelaser(self, inpair):
        out = self.paths[inpair]
        self.blue.add(inpair)
        return out

    def setimg(self):
        if self.id == 0:
            if (self.row, self.col-1) in self.red or (self.row, self.col+1) in self.red:
                if (self.row-1, self.col+1) in self.red or (self.row+1, self.col-1) in self.red:
                    if (self.row-1, self.col) in self.red or (self.row+1, self.col) in self.red:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 82
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 81
                        else:
                            self.img = 60
                    elif (self.row-1, self.col) in self.blue or (self.row+1, self.col) in self.blue:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 79
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 78
                        else:
                            self.img = 77
                    else:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 83
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 80
                        else:
                            self.img = 59
                elif (self.row-1, self.col+1) in self.blue or (self.row+1, self.col-1) in self.blue:
                    if (self.row-1, self.col) in self.red or (self.row+1, self.col) in self.red:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 71
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 70
                        else:
                            self.img = 69
                    elif (self.row-1, self.col) in self.blue or (self.row+1, self.col) in self.blue:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 67
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 66
                        else:
                            self.img = 97
                    else:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 72
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 68
                        else:
                            self.img = 65
                else:
                    if (self.row-1, self.col) in self.red or (self.row+1, self.col) in self.red:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 86
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 85
                        else:
                            self.img = 84
                    elif (self.row-1, self.col) in self.blue or (self.row+1, self.col) in self.blue:
                        if (self.row+1, self.col+1) in self.red or (self.row+1, self.col-1) in self.red:
                            self.img = 75
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 74
                        else:
                            self.img = 73
                    else:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 87
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 76
                        else:
                            self.img = 58
            elif (self.row, self.col-1) in self.blue or (self.row, self.col+1) in self.blue:
                if (self.row-1, self.col+1) in self.red or (self.row+1, self.col-1) in self.red:
                    if (self.row-1, self.col) in self.red or (self.row+1, self.col) in self.red:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 39
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 38
                        else:
                            self.img = 37
                    elif (self.row-1, self.col) in self.blue or (self.row+1, self.col) in self.blue:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 35
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 34
                        else:
                            self.img = 33
                    else:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 40
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 36
                        else:
                            self.img = 32
                elif (self.row-1, self.col+1) in self.blue or (self.row+1, self.col-1) in self.blue:
                    if (self.row-1, self.col) in self.red or (self.row+1, self.col) in self.red:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 26
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 25
                        else:
                            self.img = 24
                    elif (self.row-1, self.col) in self.blue or (self.row+1, self.col) in self.blue:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 22
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 21
                        else:
                            self.img = 20
                    else:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 27
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 23
                        else:
                            self.img = 19
                else:
                    if (self.row-1, self.col) in self.red or (self.row+1, self.col) in self.red:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 43
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 42
                        else:
                            self.img = 41
                    elif (self.row-1, self.col) in self.blue or (self.row+1, self.col) in self.blue:
                        if (self.row+1, self.col+1) in self.red or (self.row+1, self.col-1) in self.red:
                            self.img = 30
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 29
                        else:
                            self.img = 28
                    else:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 44
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 31
                        else:
                            self.img = 18
            else:
                if (self.row-1, self.col+1) in self.red or (self.row+1, self.col-1) in self.red:
                    if (self.row-1, self.col) in self.red or (self.row+1, self.col) in self.red:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 95
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 94
                        else:
                            self.img = 93
                    elif (self.row-1, self.col) in self.blue or (self.row+1, self.col) in self.blue:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 91
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 90
                        else:
                            self.img = 89
                    else:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 96
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 92
                        else:
                            self.img = 88
                elif (self.row-1, self.col+1) in self.blue or (self.row+1, self.col-1) in self.blue:
                    if (self.row-1, self.col) in self.red or (self.row+1, self.col) in self.red:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 51
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 50
                        else:
                            self.img = 49
                    elif (self.row-1, self.col) in self.blue or (self.row+1, self.col) in self.blue:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 47
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 46
                        else:
                            self.img = 54
                    else:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 52
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 48
                        else:
                            self.img = 45
                else:
                    if (self.row-1, self.col) in self.red or (self.row+1, self.col) in self.red:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 63
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 62
                        else:
                            self.img = 61
                    elif (self.row-1, self.col) in self.blue or (self.row+1, self.col) in self.blue:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 56
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 55
                        else:
                            self.img = 53
                    else:
                        if (self.row+1, self.col+1) in self.red or (self.row-1, self.col-1) in self.red:
                            self.img = 64
                        elif (self.row+1, self.col+1) in self.blue or (self.row-1, self.col-1) in self.blue:
                            self.img = 57
                        else:
                            self.img = 0
        elif self.id == 1:
            if (self.row, self.col-1) in self.red or (self.row-1, self.col) in self.red:
                self.img = 14
            elif (self.row, self.col-1) in self.blue or (self.row-1, self.col) in self.blue:
                self.img = 10
            else:
                self.img = 5
        elif self.id == 2:
            if (self.row, self.col+1) in self.red or (self.row-1, self.col) in self.red:
                self.img = 15
            elif (self.row, self.col+1) in self.blue or (self.row-1, self.col) in self.blue:
                self.img = 11
            else:
                self.img = 6
        elif self.id == 3:
            if (self.row, self.col+1) in self.red or (self.row+1, self.col) in self.red:
                self.img = 16
            elif (self.row, self.col+1) in self.blue or (self.row+1, self.col) in self.blue:
                self.img = 12
            else:
                self.img = 7
        elif self.id == 4:
            if (self.row, self.col-1) in self.red or (self.row+1, self.col) in self.red:
                self.img = 17
            elif (self.row, self.col-1) in self.blue or (self.row+1, self.col) in self.blue:
                self.img = 13
            else:
                self.img = 8
