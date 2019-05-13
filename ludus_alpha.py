# coding: utf-8
# Written by Lucas W. in Python 3.7.0
"""Initialisation"""
from time import time
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
languages = {
'english':{
'main':"\n What do you want to do? play/settings/exit > ",
'settings':"""
Type one of the following options to modify:
- 'invert': invert the colors of the board
- 'size': choose size of pieces and board
- 'flip': whether the board flips after each player's turn
- 'language': change interface language
""",
'white':'White', 'black':'Black', 'turn':"'s turn",
'inverted':" Inverted colors.",
'sizes':"The following sizes are available:", 'size_success':" Successfully changed size.\n", 'size_fail':" That size wasn't found!",
'flip_on':" The board will now flip after each player's turn.", 'flip_off':" The board stops flipping.",
'language':"Choose one of the following languages:", 'language_fail':"That language doesn't exist (yet?)", 'language_success':"Language successfully changed.",
'make_move':" Make a move ¦ ",
'conversion':" To what piece do you want to promote your pawn? (Queen/Rook/Bishop/Knight) >",
'invalid_move':"Invalid Move!",
},
'deutsch':{
'main':"\n Was wollen Sie machen? spielen/einstellungen/schliessen > ",
'settings':"""
Geben Sie eines der folgenden ein um es zu bearbeiten:
- 'umkehren': Kehren Sie die dargestellten Farben um
- 'grösse': Wählen Sie, wie gross die Figuren und das Brett sein sollen
- 'drehen': Ob das Brett nach jedem Zug sich entsprechend dreht
- 'sprache': Sprache ändern
""",
'white':'Weiss', 'black':'Schwarz', 'turn':" ist am Zug.",
'inverted':" Farben wurden umgekehrt",
'sizes':"Wählen Sie eine der folgenden Grössen:", 'size_success':" Die Grösse wurde erfolgreich aktualisiert\n", 'size_fail':" Die eingegebene Grösse existiert nicht!",
'flip_on':" Das Brett dreht sich nach jedem Zug dem entsprechenden Spieler.", 'flip_off':" Das Brett dreht sich nicht mehr.",
'language':"Die folgenden Sprachen stehen zur Verfügung:", 'language_fail':"Die gewünschte Sprache wurde nicht gefunden.", 'language_success':"Sprache erfolgreich geändert.",
'make_move':" Machen Sie einen Zug ¦ ",
'conversion':" In welche Figur wollen Sie Ihren Bauern umwandeln? (Dame/Turm/Läufer/Springer) >",
'invalid_move':"Ungültiger Zug!"
},
}
lang = languages['english']
styles = {
'3x3':{
'K':(
'-----',
'--X--',
'-X-X-',
'-XXX-',
'-----'
),
'Q':(
'-----',
'-X-X-',
'--X--',
'-XXX-',
'-----'
),
'R':(
'-----',
'-----',
'-X-X-',
'-XXX-',
'-----'
),
'B':(
'-----',
'--X--',
'-X-X-',
'--X--',
'-----'
),
'N':(
'-----',
'--XX-',
'-X-X-',
'---X-',
'-----'
),
'P':(
'-----',
'-----',
'--X--',
'-XXX-',
'-----'
),
'X':(
'-----',
'-----',
'-----',
'-----',
'-----'
)
},
'5x5':{
'K':(
'-------',
'---X---',
'-XX-XX-',
'-X-X-X-',
'-X-X-X-',
'--XXX--',
'-------',
),
'Q':(
'-------',
'---X---',
'-X-X-X-',
'-X-X-X-',
'-X-X-X-',
'--XXX--',
'-------',
),
'R':(
'-------',
'--X-X--',
'--XXX--',
'--XXX--',
'--XXX--',
'--XXX--',
'-------',
),
'B':(
'-------',
'---X---',
'--X-X--',
'--XXX--',
'---X---',
'-XX-XX-',
'-------',
),
'N':(
'-------',
'--XX-X-',
'-XXXX--',
'---XX--',
'--XX---',
'-XXXX--',
'-------',
),
'P':(
'-------',
'-------',
'---X---',
'--XXX--',
'---X---',
'--XXX--',
'-------',
),
'X':(
'-------',
'-------',
'-------',
'-------',
'-------',
'-------',
'-------',
)
},
'7x7':{
'K':(
'---------',
'----X----',
'--X-X-X--',
'-X-XXX-X-',
'-X--X--X-',
'--XXXXX--',
'---XXX---',
'--XXXXX--',
'---------',
),
'Q':(
'---------',
'---X-X---',
'-X-X-X-X-',
'-X-XXX-X-',
'--XX-XX--',
'--XXXXX--',
'---XXX---',
'--XXXXX--',
'---------',
),
'R':(
'---------',
'--X-X-X--',
'--XXXXX--',
'---XXX---',
'---XXX---',
'---XXX---',
'--XXXXX--',
'--XXXXX--',
'---------',
),
'B':(
'---------',
'---XXX---',
'---X-X---',
'--X---X--',
'--XX-XX--',
'----X----',
'--XX-XX--',
'-XX---XX-',
'---------',
),
'N':(
'---------',
'-----X---',
'---XXX---',
'--XXXXX--',
'--XX-XX--',
'----XXX--',
'---XXX---',
'--XXXXX--',
'---------',
),
'P':(
'---------',
'---------',
'----X----',
'---XXX---',
'---XXX---',
'----X----',
'---XXX---',
'--XXXXX--',
'---------',
),
'X':(
'---------',
'---------',
'---------',
'---------',
'---------',
'---------',
'---------',
'---------',
'---------',
)
},
'9x9':{
'K':(
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
),
'Q':(
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
),
'R':(
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
),
'B':(
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
),
'N':(
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
),
'P':(
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
),
'X':(
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
),
},
'9x9_alt':{
'K':(
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
),
'Q':(
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
),
'R':(
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
),
'B':(
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
),
'N':(
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
),
'P':(
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
),
'X':(
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
),
}
}
style = styles['5x5']
width = 8*len(style['K'])+2
col = {'w':'░', 'b':'█', 'd':'▓', 'l':'▒', 'x':' '} #white/black/dark/light/transparent(space)
flip = {0:1,1:-1}
history = []
turn = 0
s_rank, s_file, e_rank, e_file = 0, 0, 0, 0
a_to_n = dict(zip('abcdefgh', range(8))) #convert file letters to numbers
n_to_a = dict(zip(range(8), 'abcdefgh')) #convert numbers to file letters

"""Functions"""
def sign(x): # 1, -1 or 0 for positive/negative numbers and zero
    try:
        return int(x/abs(x))
    except:
        return 1
def display_board_single(board=board):
    Unicode = {'w':{'K':'♔', 'Q':'♕', 'R':'♖', 'B':'♗', 'N':'♘', 'P':'♙'}, 'b':{'K':'♚', 'Q':'♛', 'R':'♜', 'B':'♝', 'N':'♞', 'P':'♟'}, 'x':{'X':'-'}}
    #Ascii = {'w':{'K':'k', 'Q':'q', 'R':'r', 'B':'b', 'N':'n', 'P':'p'}, 'b':{'K':'K', 'Q':'Q', 'R':'R', 'B':'B', 'N':'N', 'P':'P'}, 'x':{'X':'.'}},
    for rank_num, rank in enumerate(board[::-flip[turn%2]]):
        print(str((8-rank_num if flip[turn%2]==1 else rank_num+1)), end='')
        for square_num, square in enumerate(rank[::flip[turn%2]]):
            print(Unicode[square[0]][square[1]].replace('-', {0:col['l'], 1:col['d']}[(rank_num+square_num)%2]), end='')
        print()
    print(' '+"abcdefgh"[::flip[turn%2]])
def display_board(board=board):
    for rank_num, rank in enumerate(board[::-flip[turn%2]]):
        for row_num, row in enumerate(style['K']):
            print(' '+str((8-rank_num if flip[turn%2]==1 else rank_num+1)) if row_num==int(len(style['K'])/2) else '  ', end='')
            for square_num, square in enumerate(rank[::flip[turn%2]]):
                print(style[square[1]][row_num].replace('X', col[square[0]]).replace('-', {0:col['l'], 1:col['d']}[(rank_num+square_num)%2]), end='')
                #print(style[square[1]][row_num].replace('l', col[{'w':'b','b':'w', 'x':'x'}[square[0]]]).replace('X', col[square[0]]).replace('-', {0:col['w'], 1:col['b']}[(rank_num+square_num)%2]), end='')
            print()
    print('  '+"{s2}A{s}B{s}C{s}D{s}E{s}F{s}G{s}H{s2}".format(s=(len(style['K'])-1)*' ', s2=int((len(style['K'])-1)/2)*' ')[::flip[turn%2]])

def check_query():#!!
    return True

def validate_move(s_rank, s_file, e_rank, e_file, playercol, history=history):
    s_color, s_type = board[s_rank][s_file][0], board[s_rank][s_file][1]
    e_color, e_type = board[e_rank][e_file][0], board[e_rank][e_file][1]
    rank_diff = e_rank - s_rank
    file_diff = e_file - s_file
    forward = {'w':1, 'b':-1}[playercol]
    own_figure = s_color==playercol #own figure being moved
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
        move_in_domain_pawn2 = (rank_diff, file_diff, s_rank) == (2*forward, 0, {'w':1, 'b':6}[playercol]) #two squares
        print(f"MOVE PAWN2 COND {(rank_diff, file_diff, s_rank)} VALUE {(2*forward, 0, {'w':1, 'b':6}[playercol])}")
        move_in_domain_pawn3 = (rank_diff, abs(file_diff)) == (forward, 1) and board[e_rank][e_file]!='xX' #diagonal
        if move_in_domain_pawn1 and e_rank == {'w':7,'b':0}[playercol]:
            special_move = 'conversion'
        elif (rank_diff, abs(file_diff)) == (forward, 1) and history[-1]==(n_to_a[e_file]+str(e_rank+1+forward), n_to_a[e_file]+str(e_rank+1-forward)) and board[e_rank-forward][e_file]=={'w':'bP', 'b':'wP'}[playercol]:
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

"""Main Loop"""
ui = 'none'
print("\n"+"CHESS (v.alpha)".center(width)+"""

 Welcome <user>!
 """)
while True:
    if ui in ['settings', 'einstellungen', 'iistellige']:
        print(lang['settings'])
    # Stopwatch/Time Limit
    # Piece Display
    if ui in ['invert', 'umkehren', 'umchereh']:
        col['w'], col['l'], col['d'], col['b'] = col['b'], col['d'], col['l'], col['w']
        print(lang['inverted'])
    if ui in ['size', 'grösse', 'grössi']:
        ui = input(f""" {lang['sizes']}
 {' / '.join([i for i in styles])} > """).lower()
        try:
            style = styles[ui]
            width = 8*len(style['K'])+2
            print(lang['size_success'])
        except:
            print(lang['size_fail'])
    if ui in ['flip', 'drehen', 'drehe']:
        if flip[1]==1:
            flip = {0:1,1:-1}
            print(lang['flip_on'])
        else:
            flip = {0:1,1:1}
            print(lang['flip_off'])
    if ui in ['language', 'sprache', 'sprach']:
        ui = input(f"""{lang['language']}
{' / '.join([i for i in languages])} > """).lower()
        try:
            lang = languages[ui]
            print(lang['language_success'])
        except:
            print(lang['language_fail'])
    if ui in ['', 'play', 'spielen', 'spiele']:
        exit=0#!!
        while True:
            display_board()
            playercol = {0:'w',1:'b'}[turn%2]
            print("\n"+f"{ {'w':lang['white'],'b':lang['black']}[playercol]}{lang['turn']}".center(width))
            while True:
                try:
                    move_start, move_end, move_force, *rest = input(lang['make_move']).lower().split()+[0,0,0]
                    if move_start=='exit': exit=1;break#!!
                    s_file, s_rank = a_to_n[move_start[0]], int(move_start[1])-1
                    e_file, e_rank = a_to_n[move_end[0]], int(move_end[1])-1
                    assert all([-1<i<8 for i in [s_file, s_rank, e_file, e_rank]])
                    #if flip[turn%2]==-1: s_file, s_rank, e_file, e_rank = 7-s_file, 7-s_rank, 7-e_file, 7-e_rank
                    print("\n",s_file,s_rank,e_file,e_rank)#!!
                    move_type = validate_move(s_rank, s_file, e_rank, e_file, playercol)
                    assert move_type!='invalid' or move_force=='force'
                    break
                except:
                    continue
            if exit:break#!!
            if move_type=='valid':
                board[e_rank][e_file] = board[s_rank][s_file]
                board[s_rank][s_file] = 'xX'
                history.append((move_start, move_end))
            elif move_type=='conversion':
                conversion_dict = {'queen':'Q','rook':'R','bishop':'B','knight':'N',
                'dame':'Q','turm':'R','läufer':'B','springer':'N',}
                while True:
                    ui = input(lang['conversion']).lower()
                    if ui not in conversion_dict: continue
                    break
                board[e_rank][e_file] = playercol+conversion_dict[ui]
                board[s_rank][s_file] = 'xX'
                #!! history.append((move_start, move_end))
            elif move_type=='en_passant':
                print("EN PASSANT!")#!!
                board[e_rank-{'w':1, 'b':-1}[playercol]][e_file] = 'xX'
                board[e_rank][e_file] = board[s_rank][s_file]
                board[s_rank][s_file] = 'xX'
                #!! history.append((move_start, move_end))
            elif move_type=='castling_kingside':#!!
                pass
                history.append(('O-O', '-'))
            elif move_type=='castling_queenside':#!!
                pass
                history.append(('O-O-O', '-'))
            elif move_force=='force': #Force any move
                board[e_rank][e_file] = board[s_rank][s_file]
                board[s_rank][s_file] = 'xX'
                history.append((move_start, move_end))
            elif move_type=='invalid':
                print(lang['invalid_move'].center(width))
            turn += 1
        #!! To-Do:
        # Check
        # Checkmate
        # Stalemate
        # Draw (insufficient material, 50-move rule)
        # 3-fold repetition
    if ui in ['hello', 'hallo', 'hallihallo', 'hey', 'hei', 'hoi']:
        print("Hi there :)")
    if ui in ['exit', 'schliessen', 'stop', 'stopp']:
        break
    ui = input(lang['main']).lower()

# Fischerandom - 960
# Undo
# (Simple AI)
# (Notation/Loading games)
