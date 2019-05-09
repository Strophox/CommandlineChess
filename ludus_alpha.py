def chess_test():
    board = [
    ['wR','wN','wB','wQ','wK','wB','wN','wR'],
    ['wP','wP','wP','wP','wP','wP','wP','wP'],
    ['nA','nA','nA','nA','nA','nA','nA','nA'],
    ['nA','nA','nA','nA','nA','nA','nA','nA'],
    ['nA','nA','nA','nA','nA','nA','nA','nA'],
    ['nA','nA','nA','nA','nA','nA','nA','nA'],
    ['bP','bP','bP','bP','bP','bP','bP','bP'],
    ['bR','bN','bB','bQ','bK','bB','bN','bR'],
    ]
    playercolor = "w"
    a_to_n = dict(zip('ABCDEFGH', range(8))) #convert file notation to numbers
    def dev_display(board=board): #quick display
        col = {'w':'░', 'b':'█', 'n':' '}
        for i in board[::-1]:
            for j in i:
                print(col[j[0]]+(j[1] if j[1]!='A' else ' '), end=' ')
            print()
    while True:
        move_start, move_end, *rest = input("Make a valid move ¦ ").upper().split()+['A1', 'A1']
        if move_start == 'EXIT': break #!#
        try:
            s_file, s_rank = a_to_n[move_start[0]], int(move_start[1])-1
            e_file, e_rank = a_to_n[move_end[0]], int(move_end[1])-1
            s_color, s_type = board[s_rank][s_file][0], board[s_rank][s_file][1]
        except:
            continue
        rank_diff = e_rank - s_rank
        file_diff = e_file - s_file
        on_the_board = -1<s_file<8 and -1<s_rank<8 and -1<e_file<8 and -1<e_rank<8 #valid board positions
        not_same_square = not move_start==move_end #positions different
        own_figure = s_color==playercolor #own figure being moved
        not_blocked_own = s_color != board[e_rank][e_file][0] #now own piece on
        if s_type == 'R':
            move_in_domain = bool(rank_diff) ^ bool(file_diff) #move vertically or horizontally only
            path_available = True
            if rank_diff>0:
                for i in range(abs(rank_diff)):
                    path_available =
                    if not path_available:

            elif rank_diff<0:
            elif file_diff>0:
            elif file_diff<0:
                path_available =
        elif s_type = 'N':
            move_in_domain = (abs(rank_diff)==2 and abs(file_diff)==1) or (abs(rank_diff)==1 and abs(file_diff)==2 )
            path_available = True
        elif s_type = 'B':
            move_in_domain = rank_diff==file_diff
            path_available =
        elif s_type = 'Q':
            move_in_domain = (bool(rank_diff) ^ bool(file_diff)) or rank_diff==file_diff
            path_available =
        elif s_type = 'K':
            move_in_domain = file_diff<=1 and rank_diff<=1
            path_available = True
        elif s_type = 'P':
            move_in_domain = rank_diff=
            path_available =
        else: #no figure selected
            continue
        if on_the_board and not_same_square and own_figure and not_blocked_own and not_blocked_enemy
        #not in check afterwards
        #conversion?
        #en passant
        #castling?

        board[e_rank][e_file] = board[s_rank][s_file]
        board[s_rank][s_file] = 'nA'
        dev_display()

chess_test()
