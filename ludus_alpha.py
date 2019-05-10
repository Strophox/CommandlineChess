# coding: utf-8
# Written by Lucas W. in Python 3.7.0

def chess_test():
    """Initialisation"""
    board = [
    ['wR','wN','wB','wQ','wK','wB','wN','wR'],
    ['wP','wP','wP','wP','wP','wP','wP','wP'],
    ['xX','xX','xX','xX','xX','xX','xX','xX'],
    ['xX','xX','xX','xX','xX','xX','xX','xX'],
    ['xX','xX','xX','xX','xX','xX','xX','xX'],
    ['xX','xX','xX','xX','xX','xX','xX','xX'],
    ['bP','bP','bP','bP','bP','bP','bP','bP'],
    ['bR','bN','bB','bQ','bK','bB','bN','bR'],
    ]
    Three_by_Three = {
    'K':[
    '-----',
    '--X--',
    '-X-X-',
    '-XXX-',
    '-----'
    ],
    'Q':[
    '-----',
    '-X-X-',
    '--X--',
    '-XXX-',
    '-----'
    ],
    'R':[
    '-----',
    '-----',
    '-X-X-',
    '-XXX-',
    '-----'
    ],
    'B':[
    '-----',
    '--X--',
    '-X-X-',
    '--X--',
    '-----'
    ],
    'N':[
    '-----',
    '--XX-',
    '-X-X-',
    '---X-',
    '-----'
    ],
    'P':[
    '-----',
    '-----',
    '--X--',
    '-XXX-',
    '-----'
    ],
    'X':[
    '-----',
    '-----',
    '-----',
    '-----',
    '-----'
    ]
    }
    Five_by_Five = {
    'K':[
    '-------',
    '-XX-XX-',
    '-X-X-X-',
    '--XXX--',
    '-------',
    '-XXXXX-',
    '-------',
    ],
    'Q':[
    '-------',
    '-X-X-X-',
    '--X-X--',
    '-XXXXX-',
    '-------',
    '-XXXXX-',
    '-------',
    ],
    'R':[
    '-------',
    '--X-X--',
    '--XXX--',
    '--XXX--',
    '-------',
    '-XXXXX-',
    '-------',
    ],
    'B':[
    '-------',
    '---X---',
    '--X-X--',
    '---X---',
    '-------',
    '-XXXXX-',
    '-------',
    ],
    'N':[
    '-------',
    '---XX--',
    '--X-X--',
    '----X--',
    '-------',
    '-XXXXX-',
    '-------',
    ],
    'P':[
    '-------',
    '-------',
    '---X---',
    '--XXX--',
    '-------',
    '-XXXXX-',
    '-------',
    ],
    'X':[
    '-------',
    '-------',
    '-------',
    '-------',
    '-------',
    '-------',
    '-------',
    ]
    }
    Seven_by_Seven = {
    'K':[
    '---------',
    '--X-X-X--',
    '-X-XXX-X-',
    '-X--X--X-',
    '-X--X--X-',
    '--XXXXX--',
    '---XXX---',
    '--XXXXX--',
    '---------',
    ],
    'Q':[
    '---------',
    '---X-X---',
    '-X-X-X-X-',
    '-X-XXX-X-',
    '--XX-XX--',
    '--XXXXX--',
    '---XXX---',
    '--XXXXX--',
    '---------',
    ],
    'R':[
    '---------',
    '--X-X-X--',
    '--XXXXX--',
    '---XXX---',
    '---XXX---',
    '---XXX---',
    '--XXXXX--',
    '--XXXXX--',
    '---------',
    ],
    'B':[
    '---------',
    '----X----',
    '---X-X---',
    '--X---X--',
    '--XX-XX--',
    '----X----',
    '---X-X---',
    '-XX---XX-',
    '---------',
    ],
    'N':[
    '---------',
    '-----X---',
    '---XXX---',
    '--XXXXX--',
    '--XX-XX--',
    '----XXX--',
    '---XXX---',
    '--XXXXX--',
    '---------',
    ],
    'P':[
    '---------',
    '---------',
    '----X----',
    '---XXX---',
    '---XXX---',
    '----X----',
    '---XXX---',
    '--XXXXX--',
    '---------',
    ],
    'X':[
    '---------',
    '---------',
    '---------',
    '---------',
    '---------',
    '---------',
    '---------',
    '---------',
    '---------',
    ]
    }
    Nine_by_Nine_alt = {
    'K':[
    '-----------',
    '---X-X-X---',
    '--X-XXX-X--',
    '--X--X--X--',
    '---XXXXX---',
    '----XXX----',
    '----XXX----',
    '---XXXXX---',
    '---XXXXX---',
    '--XXXXXXX--',
    '-----------',
    ],
    'Q':[
    '-----------',
    '---X-X-X---',
    '----XXX----',
    '---XXXXX---',
    '----XXX----',
    '----XXX----',
    '----XXX----',
    '---XXXXX---',
    '---XXXXX---',
    '--XXXXXXX--',
    '-----------',
    ],
    'R':[
    '-----------',
    '-----------',
    '---X-X-X---',
    '---XXXXX---',
    '---XXXXX---',
    '----XXX----',
    '----XXX----',
    '---XXXXX---',
    '---XXXXX---',
    '---XXXXX---',
    '-----------',
    ],
    'B':[
    '-----------',
    '-----X-----',
    '----X-X----',
    '----X-X----',
    '----XXX----',
    '-----X-----',
    '----XXX----',
    '----XXX----',
    '---XXXXX---',
    '---XXXXX---',
    '-----------',
    ],
    'N':[
    '-----------',
    '------X----',
    '----XXXX---',
    '---XXXXXX--',
    '--XXX-XXX--',
    '---X--XXX--',
    '-----XXX---',
    '----XXX----',
    '---XXXXX---',
    '---XXXXX---',
    '-----------',
    ],
    'P':[
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----X-----',
    '----XXX----',
    '----XXX----',
    '-----X-----',
    '----XXX----',
    '---XXXXX---',
    '-----------',
    ],
    'X':[
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    ],
    }
    Nine_by_Nine = {
    'K':[
    '-----------',
    '-----X-----',
    '---X-X-X---',
    '--X-XXX-X--',
    '--X--X--X--',
    '--X--X--X--',
    '---XXXXX---',
    '----XXX----',
    '---XXXXX---',
    '--XXXXXXX--',
    '-----------',
    ],
    'Q':[
    '-----------',
    '----X-X----',
    '--X-X-X-X--',
    '--X-X-X-X--',
    '--X-XXX-X--',
    '--XXX-XXX--',
    '--X-XXX-X--',
    '---XXXXX---',
    '---XXXXX---',
    '--XXXXXXX--',
    '-----------',
    ],
    'R':[
    '-----------',
    '-----------',
    '---X-X-X---',
    '---XXXXX---',
    '---XXXXX---',
    '----XXX----',
    '----XXX----',
    '---XXXXX---',
    '---XXXXX---',
    '--XXXXXXX--',
    '-----------',
    ],
    'B':[
    '-----------',
    '-----X-----',
    '----XXX----',
    '---XX-XX---',
    '---X---X---',
    '---XX-XX---',
    '----XXX----',
    '----XXX----',
    '--XX-X-XX--',
    '-XX-----XX-',
    '-----------',
    ],
    'N':[
    '-----------',
    '-----XX-X--',
    '----X-XX---',
    '---XXXXXX--',
    '--XXX-XXX--',
    '---X--XXX--',
    '-----XXX---',
    '----XXX----',
    '---XXXXX---',
    '---XXXXX---',
    '-----------',
    ],
    'P':[
    '-----------',
    '-----------',
    '-----------',
    '-----X-----',
    '----XXX----',
    '----XXX----',
    '-----X-----',
    '----XXX----',
    '----XXX----',
    '---XXXXX---',
    '-----------',
    ],
    'X':[
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    '-----------',
    ],
    }
    styles = {
    'Letters':{'w':{'K':'k', 'Q':'q', 'R':'r', 'B':'b', 'N':'n', 'P':'p'}, 'b':{'K':'K', 'Q':'Q', 'R':'R', 'B':'B', 'N':'N', 'P':'P'}, 'x':{'X':'.'}},
    'Unicode':{'w':{'K':'♔', 'Q':'♕', 'R':'♖', 'B':'♗', 'N':'♘', 'P':'♙'}, 'b':{'K':'♚', 'Q':'♛', 'R':'♜', 'B':'♝', 'N':'♞', 'P':'♟'}, 'x':{'X':'-'}},
    '3x3':Three_by_Three,
    '5x5':Five_by_Five,
    '7x7':Seven_by_Seven,
    '9x9_alt':Nine_by_Nine_alt,
    '9x9':Nine_by_Nine
    }
    style_used = styles['3x3']
    col = {'w':'░', 'b':'█', 'd':'▓', 'l':'▒', 'x':' '} #white/black/dark/light/transparent(space)
    history = []
    turn = 0
    s_rank, s_file, e_rank, e_file = 0, 0, 0, 0
    a_to_n = dict(zip('abcdefgh', range(8))) #convert file letters to numbers
    n_to_a = dict(zip(range(8), 'abcdefgh')) #convert numbers to file letters

    """Functions"""
    def sign(x):
        try:
            return int(x/abs(x))
        except:
            return 1

    def dev_display(board=board): #quick display
        for num, rank in enumerate(board[::-1]):
            print(str(8-num), end=' ')
            for square in rank:
                print(col[square[0]]+(square[1] if square[1]!='X' else '-'), end=' ')
            print()
        print("  a  b  c  d  e  f  g  h")

    def single_display(style=styles['Unicode'], board=board):
        for rank_num, rank in enumerate(board[::-1]):
            print(str(8-rank_num), end='')
            for square_num, square in enumerate(rank):
                print(style[square[0]][square[1]].replace('-', {0:col['l'], 1:col['d']}[(rank_num+square_num)%2]), end='')
            print()
        print(" abcdefgh")

    def display(style=style_used, board=board):
        for rank_num, rank in enumerate(board[::-1]):
            for row_num, row in enumerate(style['K']):
                print(str(8-rank_num) if row_num==int(len(style['K'])/2) else ' ', end='')
                for square_num, square in enumerate(rank):
                    print(style[square[1]][row_num].replace('X', col[square[0]]).replace('-', {0:col['l'], 1:col['d']}[(rank_num+square_num)%2]), end='')
                print()
        print(" {s2}A{s}B{s}C{s}D{s}E{s}F{s}G{s}H".format(s=(len(style['K'])-1)*' ', s2=int((len(style['K'])-1)/2)*' '))

    def check_query():#!!
        return True

    def validate_move(s_rank, s_file, e_rank, e_file, playercolor, history=history):
        s_color, s_type = board[s_rank][s_file][0], board[s_rank][s_file][1]
        e_color, e_type = board[e_rank][e_file][0], board[e_rank][e_file][1]
        rank_diff = e_rank - s_rank
        file_diff = e_file - s_file
        forward = {'w':1, 'b':-1}[playercolor]
        own_figure = s_color==playercolor #own figure being moved
        not_blocked_own = s_color != e_color #end square not of the same color (also keeps piece from staying on same square)
        move_in_domain = True
        path_available = True
        special_move = ''
        print(" FORWARD:", forward, " COLOR, TYPE:",s_color, s_type, "\n RANK, FILE DIFFERENCE:", rank_diff, file_diff, "\n OWN FIGURE:", own_figure, "\n NOT BLOCKED BY OWN:", not_blocked_own) #!!

        if s_type=='R': #Rook/Turm
            print("ROOK")#!!
            move_in_domain = bool(rank_diff) ^ bool(file_diff) #move vertically or horizontally only
            if rank_diff!=0: #moved along a file
                for i in range(1, abs(rank_diff)):
                    path_available = board[s_rank+sign(rank_diff)*i][s_file]=="xX"
                    if not path_available: break
            elif file_diff!=0: #moved along a rank
                for i in range(1, abs(file_diff)):
                    path_available = board[s_rank][s_file+sign(file_diff)*i]=="xX"
                    if not path_available: break
            else: print("ERROR R")

        elif s_type=='N': #Knight/Springer
            print("KNIGHT")#!!
            move_in_domain = (abs(rank_diff), abs(file_diff))==(1,2) or (abs(rank_diff), abs(file_diff))==(2,1) #L-shape

        elif s_type=='B': #Bishop/Läufer
            print("BISHOP")#!!
            move_in_domain = abs(rank_diff)==abs(file_diff) #on a diagonal
            for i in range(1, abs(rank_diff)):
                path_available = board[s_rank+sign(rank_diff)*i][s_file+sign(file_diff)*i]=="xX" #diagonal not blocked
                if not path_available: break

        elif s_type=='Q': #Queen/Dame
            print("QUEEN")#!!
            move_in_domain = bool(rank_diff)^bool(file_diff) or abs(rank_diff)==abs(file_diff) #along rank, file or diagonal
            if bool(rank_diff)^bool(file_diff) and rank_diff!=0: #along a file
                for i in range(1, abs(rank_diff)):
                    path_available = board[s_rank+sign(rank_diff)*i][s_file]=="xX"
                    if not path_available: break
            elif bool(rank_diff)^bool(file_diff) and file_diff!=0: #along a rank
                for i in range(1, abs(file_diff)):
                    path_available = board[s_rank][s_file+sign(file_diff)*i]=="xX"
                    if not path_available: break
            elif abs(rank_diff)==abs(file_diff): #on a diagonal
                for i in range(1, abs(rank_diff)):
                    path_available = board[s_rank+sign(rank_diff)*i][s_file+sign(file_diff)*i]=="xX"
                    if not path_available: break
            else: print("ERROR Q")#!!

        elif s_type=='K': #King/König
            print("KING")#!!
            move_in_domain_king1 = file_diff<=1 and rank_diff<=1 #one square in every direction
            move_in_domain_king2 = True#!!
            move_in_domain_king = any([move_in_domain_king1, move_in_domain_king2])

        elif s_type=='P': #Pawn/Bauer
            print("PAWN")#!!
            move_in_domain_pawn1 = (rank_diff, file_diff) == (forward, 0) #one square
            move_in_domain_pawn2 = (rank_diff, file_diff, s_rank) == (2*forward, 0, {'w':1, 'b':6}[playercolor]) #two squares
            print(f"MOVE PAWN2 COND {(rank_diff, file_diff, s_rank)} VALUE {(2*forward, 0, {'w':1, 'b':6}[playercolor])}")
            move_in_domain_pawn3 = (rank_diff, abs(file_diff)) == (forward, 1) and board[e_rank][e_file]!='xX' #diagonal
            if move_in_domain_pawn1 and e_rank == {'w':7,'b':0}[playercolor]:
                special_move = 'conversion'
            elif (rank_diff, abs(file_diff)) == (forward, 1) and history[-1]==(n_to_a[e_file]+str(e_rank+1+forward), n_to_a[e_file]+str(e_rank+1-forward)) and board[e_rank-forward][e_file]=={'w':'bP', 'b':'wP'}[playercolor]:
                special_move = 'en_passant'
            print(" PAWN CHECK 1/2/3:", move_in_domain_pawn1, move_in_domain_pawn2, move_in_domain_pawn3, "EN PASSANT CHECK:", (n_to_a[e_file]+str(e_rank+1+forward), n_to_a[e_file]+str(e_rank+1-forward)) )#!!
            move_in_domain = any([move_in_domain_pawn1, move_in_domain_pawn2, move_in_domain_pawn3, special_move])
            if any([move_in_domain_pawn1, move_in_domain_pawn2]):
                path_available = board[e_rank][e_file]=='xX'

        else: #No figure
            print("ERROR X")#!!
        print(" MOVE IN DOMAIN:",move_in_domain,"\n PATH AVAILABLE:",path_available)
        not_in_check = check_query()#!!

        if all([own_figure, not_blocked_own, move_in_domain, path_available, not_in_check]):
            print("SUCCESS")#!!
            if special_move:
                return special_move
            else:
                return 'valid'
        else:
            print("FAIL")#!!
            return 'invalid'
        #!! not in check afterwards
        #!! castling?

    """Main Loop"""
    exit=0#!!
    print("\n --- CHESS TEST START --- \n\n")
    #single_display(styles['Unicode'])
    while True:
        display()
        playercolor = {0:'w',1:'b'}[turn%2]
        print(f"\n{(4*len(style_used))*' '}--- "+{'w':"White",'b':"Black"}[playercolor], end="'s turn ---\n")
        while True:
            try:
                move_start, move_end, *rest = input("Make a valid move ¦ ").lower().split()+[0,0]
                if move_start=='exit': exit=1;break#!!
                s_file, s_rank = a_to_n[move_start[0]], int(move_start[1])-1
                e_file, e_rank = a_to_n[move_end[0]], int(move_end[1])-1
                assert all([-1<i<8 for i in [s_file, s_rank, e_file, e_rank]])
                print("\n",s_file,s_rank,e_file,e_rank)#!!
                move_type = validate_move(s_rank, s_file, e_rank, e_file, playercolor)
                assert move_type!='invalid'
                break
            except:
                continue
        if exit:break#!!
        if move_type=='valid':
            board[e_rank][e_file] = board[s_rank][s_file]
            board[s_rank][s_file] = 'xX'
            history.append((move_start, move_end))
        elif move_type=='conversion':
            while True:
                conversion_type = input("To what piece do you want to promote your pawn? (Queen/Rook/Bishop/Knight) ").lower()
                if conversion_type not in ['queen', 'rook', 'bishop', 'knight']: continue
                break
            board[e_rank][e_file] = playercolor+{'queen':'Q', 'rook':'R', 'bishop':'B', 'knight':'N'}[conversion_type]
            board[s_rank][s_file] = 'xX'
            #!! history.append((move_start, move_end))
        elif move_type=='en_passant':
            print("EN PASSANT!")#!!
            board[e_rank-{'w':1, 'b':-1}[playercolor]][e_file] = 'xX'
            board[e_rank][e_file] = board[s_rank][s_file]
            board[s_rank][s_file] = 'xX'
            #!! history.append((move_start, move_end))
        elif move_type=='castling_kingside':#!!
            pass
            history.append(('O-O', '-'))
        elif move_type=='castling_queenside':#!!
            pass
            history.append(('O-O-O', '-'))
        else:
            print("ERROR MOVE_TYPE")#!!
        turn += 1


chess_test()
