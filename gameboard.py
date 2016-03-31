

class GameBoard:
    def __init__(self):
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
                    a.used = True
                    a.img = 1
                elif j == 3 and i == 7:
                    for k in a.paths:
                        a.paths[k] = None
                    a.used = True
                    a.img = 2
                self.tiles.append(a)

class Tile:
    def __init__(self):
        self.img = 0
        self.paths = {}
        self.row = None
        self.col = None
        self.used = False
        self.red = set()
        self.blue = set()

    def mirror1(self):
        if not self.used:
            for k in self.paths:
                self.paths[k] = None
            self.img = 5
            if self.row != 0 and self.col != 0:
                self.paths[(self.row-1, self.col)] = (self.row, self.col-1)
                self.paths[(self.row, self.col-1)] = (self.row-1, self.col)
            self.used = True

    def mirror2(self):
        if not self.used:
            for k in self.paths:
                self.paths[k] = None
            self.img = 6
            if self.row != 0 and self.col != 11:
                self.paths[(self.row-1, self.col)] = (self.row, self.col+1)
                self.paths[(self.row, self.col+1)] = (self.row-1, self.col)
            self.used = True

    def mirror3(self):
        if not self.used:
            for k in self.paths:
                self.paths[k] = None
            self.img = 7
            if self.row != 11 and self.col != 11:
                self.paths[(self.row+1, self.col)] = (self.row, self.col+1)
                self.paths[(self.row, self.col+1)] = (self.row+1, self.col)
            self.used = True

    def mirror4(self):
        if not self.used:
            for k in self.paths:
                self.paths[k] = None
            self.img = 8
            if self.row != 11 and self.col != 0:
                self.paths[(self.row+1, self.col)] = (self.row, self.col-1)
                self.paths[(self.row, self.col-1)] = (self.row+1, self.col)
            self.used = True

    def lensX(self):
        if not self.used:
            for k in self.paths:
                self.paths[k] = None
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
            if self.row != 0 and self.row != 11 and self.col != 0:
                self.paths[(self.row+1, self.col)] = (self.row-1, self.col+1)
                self.paths[(self.row+1, self.col+1)] = (self.row-1, self.col)
            self.used = True

    def lensY(self):
        if not self.used:
            for k in self.paths:
                self.paths[k] = None
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

    def block(self):
        if not self.used:
            for k in self.paths:
                self.paths[k] = None
            self.img = 9
            self.used = True

    def laser(self, inpair):
        print(self.paths[inpair] if self.paths[inpair] else 'Good')
        return self.paths[inpair]
