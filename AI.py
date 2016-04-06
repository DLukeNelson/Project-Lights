from gameboard import*

score = {(0, 0):38,
(0, 1):39,
(0, 2):10,
(0, 3):11,
(0, 4):10,
(0, 5):0,
(0, 6):7,
(0, 7):37,
(0, 8):36,
(0, 9):55,
(0, 10):54,
(0, 11):53,
(1, 0):29,
(1, 1):40,
(1, 2):11,
(1, 3):0,
(1, 4):21,
(1, 5):10,
(1, 6):39,
(1, 7):8,
(1, 8):37,
(1, 9):56,
(1, 10):55,
(1, 11):24,
(2, 0):10,
(2, 1):31,
(2, 2):12,
(2, 3):33,
(2, 4):0,
(2, 5):41,
(2, 6):10,
(2, 7):9,
(2, 8):8,
(2, 9):57,
(2, 10):26,
(2, 11):25,
(3, 0):11,
(3, 1):12,
(3, 2):13,
(3, 3):14,
(3, 4):13,
(3, 5):12,
(3, 6):11,
(3, 7):10,
(3, 8):9,
(3, 9):8,
(3, 10):7,
(3, 11):6,
(4, 0):42,
(4, 1):43,
(4, 2):14,
(4, 3):999999,
(4, 4):14,
(4, 5):13,
(4, 6):12,
(4, 7):11,
(4, 8):10,
(4, 9):9,
(4, 10):8,
(4, 11):7,
(5, 0):11,
(5, 1):12,
(5, 2):13,
(5, 3):14,
(5, 4):13,
(5, 5):12,
(5, 6):11,
(5, 7):10,
(5, 8):9,
(5, 9):8,
(5, 10):7,
(5, 11):6,
(6, 0):10,
(6, 1):31,
(6, 2):12,
(6, 3):13,
(6, 4):12,
(6, 5):31,
(6, 6):10,
(6, 7):9,
(6, 8):8,
(6, 9):7,
(6, 10):6,
(6, 11):5,
(7, 0):29,
(7, 1):10,
(7, 2):11,
(7, 3):0,
(7, 4):11,
(7, 5):10,
(7, 6):9,
(7, 7):8,
(7, 8):7,
(7, 9):6,
(7, 10):5,
(7, 11):4,
(8, 0):8,
(8, 1):9,
(8, 2):10,
(8, 3):11,
(8, 4):10,
(8, 5):9,
(8, 6):8,
(8, 7):7,
(8, 8):36,
(8, 9):40,
(8, 10):39,
(8, 11):38,
(9, 0):7,
(9, 1):8,
(9, 2):9,
(9, 3):10,
(9, 4):9,
(9, 5):8,
(9, 6):7,
(9, 7):6,
(9, 8):5,
(9, 9):34,
(9, 10):38,
(9, 11):37,
(10, 0):6,
(10, 1):7,
(10, 2):8,
(10, 3):9,
(10, 4):8,
(10, 5):7,
(10, 6):6,
(10, 7):5,
(10, 8):4,
(10, 9):3,
(10, 10):32,
(10, 11):31,
(11, 0):25,
(11, 1):36,
(11, 2):7,
(11, 3):8,
(11, 4):7,
(11, 5):6,
(11, 6):5,
(11, 7):4,
(11, 8):3,
(11, 9):2,
(11, 10):1,
(11, 11):0}






def blueAI(board):
    tileset = set()
    for atile in board.tiles:
        if not atile.used and atile.blue:
            tileset.add(atile)


    bestmove = None
    for atile in tileset:
        moves = set()
        moves.add( atile.mirror1 )
        moves.add( atile.mirror2 )
        moves.add( atile.mirror3 )
        moves.add( atile.mirror4 )
        moves.add( atile.lensX )
        moves.add( atile.lensY )
        print('New Set')

        for move in moves:
            if bestmove == None:
                bestmove = (evaluation(board, move), move)
            else:
                attempt = (evaluation(board, move), move)
                if attempt[0] > bestmove[0]:
                    bestmove = attempt
            # undo the move we just tested
            atile.used = False
            atile.id = 0
            atile.img = 0
            atile.paths[(atile.row-1, atile.col)] = (atile.row+1, atile.col)
            atile.paths[(atile.row+1, atile.col)] = (atile.row-1, atile.col)
            atile.paths[(atile.row, atile.col-1)] = (atile.row, atile.col+1)
            atile.paths[(atile.row, atile.col+1)] = (atile.row, atile.col-1)
            atile.paths[(atile.row+1, atile.col+1)] = (atile.row-1, atile.col-1)
            atile.paths[(atile.row-1, atile.col+1)] = (atile.row+1, atile.col-1)
            atile.paths[(atile.row+1, atile.col-1)] = (atile.row-1, atile.col+1)
            atile.paths[(atile.row-1, atile.col-1)] = (atile.row+1, atile.col+1)
            if atile.row == 0 or atile.row == 11:
                atile.paths[(atile.row-1, atile.col)] = None
                atile.paths[(atile.row+1, atile.col)] = None
            if atile.col == 0 or atile.col == 11:
                atile.paths[(atile.row, atile.col-1)] = None
                atile.paths[(atile.row, atile.col+1)] = None
            if atile.row == 0 or atile.row == 11 or atile.col == 0 or atile.col == 11:
                atile.paths[(atile.row+1, atile.col+1)] = None
                atile.paths[(atile.row-1, atile.col+1)] = None
                atile.paths[(atile.row+1, atile.col-1)] = None
                atile.paths[(atile.row-1, atile.col-1)] = None
            board.LaserRed()
            board.LaserBlue()
    print('Best Move is:')
    print(bestmove)
    bestmove[1](board)






def evaluation(board, move):
    move(board)
    board.LaserRed()
    board.LaserBlue()
    points = 0
    for atile in board.tiles:
        if atile.blue:
            points += score[(atile.row, atile.col)]
    print(points)
    return points
