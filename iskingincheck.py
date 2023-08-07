def king_is_in_check(chessboard : list[list[str]]) -> bool:
    row = ["a" for i in range(10)]
    for i in range(len(chessboard)):
        chessboard[i].append("a")
        chessboard[i].insert(0,"a")
    chessboard.append(row)
    chessboard.insert(0,row)    
    for i in range(len(chessboard)):
        if "♔" in chessboard[i]:
            x,y = i,chessboard[i].index("♔")#x and y values are inverted, but it does not matter at all(only in pawn case)
    
    #Check for pawn and knight
    if "♟" in chessboard[x-1][y-1]: return True
    elif "♟" in chessboard[x-1][y+1]: return True
    
    try:
        if "♞" in chessboard[x-1][y-2]: return True
    except IndexError:
        pass
    try:
        if "♞" in chessboard[x+1][y-2]: return True
    except IndexError:
        pass
    try:
        if "♞" in chessboard[x-2][y-1]: return True
    except IndexError:
        pass
    try:
        if "♞" in chessboard[x-2][y+1]: return True
    except IndexError:
        pass
    try:
        if "♞" in chessboard[x-1][y+2]: return True
    except IndexError:
        pass
    try:
        if "♞" in chessboard[x+1][y+2]: return True
    except IndexError:
        pass
    try:
        if "♞" in chessboard[x+2][y-1]: return True
    except IndexError:
        pass
    try:
        if "♞" in chessboard[x+2][y+1]: return True
    except IndexError:
        pass
    
    #Check for rook, and queen
    nx,ny = x,y
    while chessboard[nx][ny] not in '♟♞♝a':
        ny += 1
        if chessboard[nx][ny] in "♜♛": return True
    nx,ny = x,y
    while chessboard[nx][ny] not in '♟♞♝a':
        ny -= 1
        if chessboard[nx][ny] in "♜♛": return True
    nx,ny = x,y
    while chessboard[nx][ny] not in '♟♞♝a':
        nx += 1
        if chessboard[nx][ny] in "♜♛": return True
    nx,ny = x,y
    while chessboard[nx][ny] not in '♟♞♝a':
        nx -= 1
        if chessboard[nx][ny] in "♜♛": return True

    #Check for bishop and queen
    nx,ny = x,y
    while chessboard[nx][ny] not in '♟♞♜a':
        nx -= 1
        ny -= 1
        if chessboard[nx][ny] in "♝♛": return True
    nx,ny = x,y
    while chessboard[nx][ny] not in '♟♞♜a':
        nx -= 1
        ny += 1
        if chessboard[nx][ny] in "♝♛": return True
    nx,ny = x,y
    while chessboard[nx][ny] not in '♟♞♜a':
        nx += 1
        ny -= 1
        if chessboard[nx][ny] in "♝♛": return True
    nx,ny = x,y
    while chessboard[nx][ny] not in '♟♞♜a':
        nx += 1
        ny += 1
        if chessboard[nx][ny] in "♝♛": return True    
    
    chessboard = chessboard[1:-1]
    for i in range(len(chessboard)):
        chessboard[i].pop(0)
        chessboard[i].pop(-1)
    return False