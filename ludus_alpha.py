# coding: utf-8
# Written by Lucas W. in Python 3.7.0
"""Initialisation"""
from time import time
from threading import Timer
from copy import deepcopy
name = "Terminal Chess (alpha) (by Lucas W. 2019)"
board_template = [ #standard setup
['wR','wN','wB','wQ','wK','wB','wN','wR'],
['wP','wP','wP','wP','wP','wP','wP','wP'],
['xX','xX','xX','xX','xX','xX','xX','xX'],
['xX','xX','xX','xX','xX','xX','xX','xX'],
['xX','xX','xX','xX','xX','xX','xX','xX'],
['xX','xX','xX','xX','xX','xX','xX','xX'],
['bP','bP','bP','bP','bP','bP','bP','bP'],
['bR','bN','bB','bQ','bK','bB','bN','bR'],
]
board_temp = [ #temporary setup
['xX','xX','xX','xX','wK','wB','xX','xX'],
['xX','xX','xX','xX','xX','xX','xX','xX'],
['xX','xX','xX','xX','xX','xX','xX','xX'],
['xX','xX','xX','xX','xX','xX','xX','xX'],
['xX','xX','xX','xX','xX','xX','xX','xX'],
['xX','xX','xX','xX','xX','xX','xX','xX'],
['xX','xX','xX','xX','xX','xX','xX','xX'],
['xX','xX','bB','xX','bK','xX','xX','xX'],
]
board = deepcopy(board_temp)
languages = { #UI language
'english':{
'welcome':" Welcome <user>!",
'main':"\n What do you want to do? play/settings/quit > ",
'settings':"""
Type one of the following options to modify:
- 'invert': invert the colors of the board
- 'size': choose size of pieces and board
- 'flip': whether the board flips after each player's turn
- 'language': change interface language
- 'time': change time limit per player""",
'play':"""
 How to play:
 - Type '<start> <end>' to make a move (e.g. 'e2 e4')
 - Type 'resign' to resign
 - Type 'draw' to propose a draw
 - The game can be paused using 'pause'
 Enjoy playing!""",
'w':'White', 'b':'Black', 'turn':"'s turn", 'check':" is in check.",
'draw_query':' {} proposes a draw. Does {} agree? (yes/no) > ', 'resign':"{} resigns. {} wins the game.", 'pause':"The game has been paused.", 'draw':"The game is drawn.",
'draw_material':"Neither player has sufficient material to mate the other.", 'draw_threefold':"Threefold repetition has occured.", 'draw_50moverule_piece':"No piece has been taken for 50 moves.", 'draw_50moverule_pawn':"No pawn has been moved for 50 moves.",
'inverted':" Inverted colors.",
'sizes':" The following sizes are available:", 'size_success':" Successfully changed size.\n", 'size_fail':" That size wasn't found!",
'flip_on':" The board will now flip after each player's turn.", 'flip_off':" The board stops flipping.",
'language':" Choose one of the following languages:", 'language_fail':" That language doesn't exist.", 'language_success':" Language successfully changed.",
'time_query':" How much time (sec.) should one player have? (0 for infinite, current: {}) > ", 'time_success':" Time per player was set to {}s.", 'time_fail':" Time was not updated.",
'time_up':"{} ran out of time. {} wins the game.", 'time_left':"{} has {:.1f} seconds left on his clock.",
'make_move':" Make a move ¦ ",
'conversion':" To what piece do you want to promote your pawn? (Queen/Rook/Bishop/Knight) >",
'invalid_move':"Invalid Move!",
},
'deutsch':{
'welcome':" Willkommen!",
'main':"\n Was wollen Sie machen? spielen/einstellungen/schliessen > ",
'settings':"""
Geben Sie eines der folgenden ein um es zu bearbeiten:
- 'umkehren': Kehren Sie die dargestellten Farben um
- 'grösse': Wählen Sie, wie gross die Figuren und das Brett sein sollen
- 'drehen': Ob das Brett nach jedem Zug sich entsprechend dreht
- 'sprache': Sprache ändern
- 'zeit': Zeitlimit pro Spieler einstellen""",
'play':"""
 Wie man spielt:
 - Schreiben Sie '<start> <end>' um zu ziehen (z.B. 'e2 e4')
 - 'aufgeben' um aufzugeben
 - 'remis' um ihrem Gegner ein Remis anzubieten
 - Mittels 'pause' kann das spiel pausiert werden
 Viel Spass beim Spielen!""",
'w':'Weiss', 'b':'Schwarz', 'turn':" ist am Zug.", 'check':" steht im Schach.",
'draw_query':' {} schlägt ein Remis vor. Akzeptiert {}? (ja/nein) > ', 'resign':"{} gibt auf. {} gewinnt die Partie.", 'pause':"Die Partie wurde pausiert.", 'draw':"Die Partie endet in einem Remis.",
'draw_material':"Keiner der beiden Spieler hat genug Material, um zu gewinnen.", 'draw_threefold':"Dieselbe Position hat sich dreimal wiederholt.", 'draw_50moverule_piece':"Es wurde keine Figur während 50 Zügen geschlagen.", 'draw_50moverule_pawn':"Es wurde kein Bauer während 50 Zügen bewegt.",
'inverted':" Farben wurden umgekehrt",
'sizes':" Wählen Sie eine der folgenden Grössen:", 'size_success':" Die Grösse wurde erfolgreich aktualisiert\n", 'size_fail':" Die eingegebene Grösse existiert nicht!",
'flip_on':" Das Brett dreht sich nach jedem Zug dem entsprechenden Spieler.", 'flip_off':" Das Brett dreht sich nicht mehr.",
'language':" Die folgenden Sprachen stehen zur Verfügung:", 'language_fail':" Die gewünschte Sprache wurde nicht gefunden.", 'language_success':" Sprache erfolgreich geändert.",
'time_query':" Wieviel Zeit (Sek.) sollte jeder Spieler haben? (0 für Unendlich, bisher: {}) > ", 'time_success':" Zeitlimit wurde auf {}s pro Spieler gesetzt.", 'time_fail':" Zeitlimit wurde nicht geändert.",
'time_up':"{} hat das Zeitlimit erreicht. {} gewinnt die Partie.", 'time_left':"{} hat {:.1f} Sekunden übrig.",
'make_move':" Machen Sie einen Zug ¦ ",
'conversion':" In welche Figur wollen Sie Ihren Bauern umwandeln? (Dame/Turm/Läufer/Springer) >",
'invalid_move':"Ungültiger Zug!"
},
}
lang = languages['english'] #lang used
styles = { #board styles
'2x2':{
'K':(
'----',
'-XX-',
'-XX-',
'----'
),
'Q':(
'----',
'-X--',
'-XX-',
'----'
),
'R':(
'----',
'-X--',
'-X--',
'----'
),
'B':(
'----',
'-X--',
'--X-',
'----'
),
'N':(
'----',
'-XX-',
'--X-',
'----'
),
'P':(
'----',
'----',
'-X--',
'----'
),
'X':(
'----',
'----',
'----',
'----'
),
},
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
'-X-X-',
'-XXX-',
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
'3x3 bauhaus':{
'K':(
'-----',
'-XXX-',
'-XXX-',
'-XXX-',
'-----'
),
'Q':(
'-----',
'--X--',
'-XXX-',
'-XXX-',
'-----'
),
'R':(
'-----',
'-X-X-',
'-XXX-',
'-XXX-',
'-----'
),
'B':(
'-----',
'-X-X-',
'--X--',
'-X-X-',
'-----'
),
'N':(
'-----',
'-XX--',
'-XXX-',
'--XX-',
'-----'
),
'P':(
'-----',
'-----',
'-XX--',
'-XX--',
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
'-XXXXX-',
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
'---XX-X--',
'--XXXX---',
'-XXXXXX--',
'--X--XX--',
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
'7x7 double':{
'K':(
'------------------',
'--------XX--------',
'---XXX--XX--XXX---',
'--XX--XXXXXX--XX--',
'--XX----XX----XX--',
'---XXXXXXXXXXXX---',
'-----XXXXXXXX-----',
'---XXXXXXXXXXXX---',
'------------------',
),
'Q':(
'------------------',
'------X----X------',
'-XX---XX--XX---XX-',
'--XX--XXXXXX--XX--',
'---XXXXX--XXXXX---',
'----XXXXXXXXXX----',
'-----XXXXXXXX-----',
'---XXXXXXXXXXXX---',
'------------------',
),
'R':(
'------------------',
'----XX--XX--XX----',
'----XXXXXXXXXX----',
'-----XXXXXXXX-----',
'------XXXXXX------',
'-----XXXXXXXX-----',
'----XXXXXXXXXX----',
'----XXXXXXXXXX----',
'------------------',
),
'B':(
'------------------',
'-------XXXX-------',
'-----XXX--XXX-----',
'----XX------XX----',
'-----XXX--XXX-----',
'-------XXXX-------',
'-----XXX--XXX-----',
'--XXXX------XXXX--',
'------------------',
),
'N':(
'------------------',
'-------XXXX-XX----',
'----XXXXX-XXX-----',
'--XXXXXXXXXXXX----',
'---XXX---XXXXX----',
'-------XXXXXX-----',
'-----XXXXXXX------',
'----XXXXXXXXXX----',
'------------------',
),
'P':(
'------------------',
'------------------',
'--------XX--------',
'-------XXXX-------',
'------XXXXXX------',
'-------XXXX-------',
'------XXXXXX------',
'----XXXXXXXXXX----',
'------------------',
),
'X':(
'------------------',
'------------------',
'------------------',
'------------------',
'------------------',
'------------------',
'------------------',
'------------------',
'------------------',
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
}
style = styles['5x5'] #style used
width = 8*len(style['K'])+2 #board width
col = {'w':'░', 'b':'█', 'd':'▓', 'l':'▒', 'x':' '} #white/black/dark/light/transparent(space)
flip = {0:1,1:-1} #flip after each turn
history = [] #recorded moves
board_history = [] #recorded positions
turn = 0 #turn number
time_s = 0 #standard time
times = {'w':time_s, 'b':time_s} #individual times
time_up = False
piece_taken = 0 #how many moves since <>
pawn_moved = 0 #how many moves since <>
s_rank, s_file, e_rank, e_file = 0, 0, 0, 0 #start rank/file, end rank/file
a_to_n = dict(zip('abcdefgh', range(8))) #convert file letters to numbers
n_to_a = dict(zip(range(8), 'abcdefgh')) #convert numbers to file letters

"""Functions"""
def sign(x): #1, -1 or 0 for positive/negative numbers and zero
    try:
        return int(x/abs(x))
    except:
        return 1
def display_board_single(board): #smallest display of chess board in terminal
    Unicode = {'w':{'K':'♔', 'Q':'♕', 'R':'♖', 'B':'♗', 'N':'♘', 'P':'♙'}, 'b':{'K':'♚', 'Q':'♛', 'R':'♜', 'B':'♝', 'N':'♞', 'P':'♟'}, 'x':{'X':'-'}}
    Ascii = {'w':{'K':'k', 'Q':'q', 'R':'r', 'B':'b', 'N':'n', 'P':'p'}, 'b':{'K':'K', 'Q':'Q', 'R':'R', 'B':'B', 'N':'N', 'P':'P'}, 'x':{'X':'-'}}
    style_used = Ascii
    for rank_num, rank in enumerate(board[::-flip[turn%2]]):
        print(str((8-rank_num if flip[turn%2]==1 else rank_num+1)), end=' ')
        for square_num, square in enumerate(rank[::flip[turn%2]]):
            print(style_used[square[0]][square[1]].replace('-', {0:col['l'], 1:col['d']}[(rank_num+square_num)%2] ), end='')
        print()
    print('\n  '+"abcdefgh"[::flip[turn%2]])
def display_board(board): # displays board in terminal
    print()
    for rank_num, rank in enumerate(board[::-flip[turn%2]]):
        for row_num, row in enumerate(style['K']):
            print(' '+str((8-rank_num if flip[turn%2]==1 else rank_num+1)) if row_num==int(len(style['K'])/2) else '  ', end='')
            print(''.join([style[square[1]][row_num].replace('X', col[square[0]]).replace('-', {0:col['l'], 1:col['d']}[(rank_num+square_num)%2])  for square_num, square in enumerate(rank[::flip[turn%2]])]))
            #for square_num, square in enumerate(rank[::flip[turn%2]]): #old version of the previous line
            #    print(style[square[1]][row_num].replace('X', col[square[0]]).replace('-', {0:col['l'], 1:col['d']}[(rank_num+square_num)%2]), end='')
            #print()
    print('  '+"{s2}A{s}B{s}C{s}D{s}E{s}F{s}G{s}H{s2}".format(s=(len(style['K'][0])-1)*' ', s2=int((len(style['K'][0])-1)/2)*' ')[::flip[turn%2]])
def reset(): #reset game (board, time, other statistics)
    global board, board_history, history, times, piece_taken, pawn_moved, turn
    board = deepcopy(board_template)
    board_history = []
    history = []
    time_up = False
    times = {'w':time_s, 'b':time_s}
    piece_taken = 0
    pawn_moved = 0
    turn = 0
def time_up_toggle(): #change global time_up
    print("Time is up.")
    global time_up
    time_up = True
def find_piece(color, board, piece_type, depth=1): #finds the king of a specific player on the board
    for rank_num, rank in enumerate(board):
        for file_num, square in enumerate(rank):
            if square==color+'K':
                depth -= 1
                if not depth:
                    return rank_num, file_num
    return (-1,-1)
def not_attacked(playercol, rank, file, board): #checks, whether a certain square is attacked by a certain color
    enemy_color = {'w':'b','b':'w'}[playercol]
    forward = {'w':-1, 'b':1}[enemy_color]
    for x,y in ((1,0), (-1,0), (0,1), (0,-1)): #attacked by queen/rook?
        steps = 1
        while -1<rank+steps*x<8 and -1<file+steps*y<8:
            if board[rank+steps*x][file+steps*y] in [enemy_color+'Q', enemy_color+'R']:
                return False
            if board[rank+steps*x][file+steps*y] != 'xX':
                break
            steps += 1
    for x,y in ((1,1), (-1,1), (1,-1), (-1,-1)): #attacked by queen/bishop?
        steps = 1
        while -1<rank+steps*x<8 and -1<file+steps*y<8:
            if board[rank+steps*x][file+steps*y] in [enemy_color+'Q', enemy_color+'B']:
                return False
            if board[rank+steps*x][file+steps*y] != 'xX':
                break
            steps += 1
    for x,y in ((1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)): #attacked by knight?
        if -1<rank+x<8 and -1<file+y<8:
            if board[rank+x][file+y]==enemy_color+'N':
                return False
    for sidestep in (1,-1): #attacked by pawn?
        if -1<rank+forward<8 and -1<file+sidestep<8:
            if board[rank+forward][file+sidestep]==enemy_color+'P':
                return False
    for x,y in [(x,y) for x in (0,1,-1) for y in (0,1,-1)]: #attacked by king?
        if not -1<rank+x<8 or not -1<file+y<8:
            continue
        if board[rank+x][file+y]==enemy_color+'K':
            return False
    return True
def validate_move(s_rank, s_file, e_rank, e_file, playercol, history=history): #checks, whether a given move is legal
    s_piece = board[s_rank][s_file]
    e_piece = board[e_rank][e_file]
    rank_diff = e_rank - s_rank
    file_diff = e_file - s_file
    forward = {'w':1, 'b':-1}[playercol]
    own_figure = s_piece[0]==playercol #own figure being moved
    not_occupied_own = s_piece[0] != e_piece[0] #end square not of the same color (also keeps piece from staying on same square)
    move_in_domain = True
    path_available = True
    special_move = ''
    if s_piece[1]=='R': #Rook/Turm
        move_in_domain = bool(rank_diff) ^ bool(file_diff) #move vertically or horizontally only
        if rank_diff!=0: #moved along a file
            for i in range(1, abs(rank_diff)):
                path_available = board[s_rank+sign(rank_diff)*i][s_file]=="xX"
                if not path_available: break
        elif file_diff!=0: #moved along a rank
            for i in range(1, abs(file_diff)):
                path_available = board[s_rank][s_file+sign(file_diff)*i]=="xX"
                if not path_available: break
    elif s_piece[1]=='N': #Knight/Springer
        move_in_domain = (abs(rank_diff), abs(file_diff))==(1,2) or (abs(rank_diff), abs(file_diff))==(2,1) #L-shape
    elif s_piece[1]=='B': #Bishop/Läufer
        move_in_domain = abs(rank_diff)==abs(file_diff) #on a diagonal
        for i in range(1, abs(rank_diff)):
            path_available = board[s_rank+sign(rank_diff)*i][s_file+sign(file_diff)*i]=="xX" #diagonal not blocked
            if not path_available: break
    elif s_piece[1]=='Q': #Queen/Dame
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
    elif s_piece[1]=='K': #King/König
        move_in_domain_castling = (rank_diff, abs(file_diff))==(0,2)
        squares_free = board[e_rank][e_file]=='xX' and board[e_rank][s_file+int(file_diff/2)]=='xX'
        squares_not_attacked = not_attacked(playercol, e_rank, e_file, board) and not_attacked(playercol, e_rank, s_file+int(file_diff/2), board)
        king_unmoved = False
        if (s_rank, s_file)=={'w':(0,4), 'b':(7,4)}[playercol]:
            king_unmoved = True
            for move in history:
                if move[0]=={'w':'e1', 'b':'e8'}[playercol]:
                    king_unmoved = False
                    break
        rook_unmoved = False
        if file_diff>0 and board[s_rank][7]==playercol+'R':
                rook_unmoved = True
                for move in history:
                    if move[0]=={'w':'h1', 'b':'h8'}[playercol]:
                        rook_unmoved = False
                        break
                if rook_unmoved:
                    special_move = 'castling_kingside'
        if file_diff<0 and board[s_rank][0]==playercol+'R':
                rook_unmoved = True
                for move in history:
                    if move[0]=={'w':'a1', 'b':'a8'}[playercol]:
                        rook_unmoved = False
                        break
                if rook_unmoved:
                    special_move = 'castling_queenside'
        move_in_domain_king1 = abs(file_diff)<=1 and abs(rank_diff)<=1 #one square in every direction
        if move_in_domain_king1:
            special_move = ''
        move_in_domain_king2 = all([move_in_domain_castling, squares_free, squares_not_attacked, king_unmoved, rook_unmoved])#castling
        move_in_domain = any([move_in_domain_king1, move_in_domain_king2])
    elif s_piece[1]=='P': #Pawn/Bauer
        move_in_domain_pawn1 = (rank_diff, file_diff) == (forward, 0) #one square
        move_in_domain_pawn2 = (rank_diff, file_diff, s_rank) == (2*forward, 0, {'w':1, 'b':6}[playercol]) #two squares
        move_in_domain_pawn3 = (rank_diff, abs(file_diff)) == (forward, 1) and board[e_rank][e_file]!='xX' #diagonal
        if move_in_domain_pawn1 and e_rank == {'w':7,'b':0}[playercol]:
            special_move = 'conversion'
        elif (rank_diff, abs(file_diff)) == (forward, 1) and history[-1]==(n_to_a[e_file]+str(e_rank+1+forward), n_to_a[e_file]+str(e_rank+1-forward)) and board[e_rank-forward][e_file]=={'w':'bP', 'b':'wP'}[playercol]:
            special_move = 'en_passant'
        move_in_domain = any([move_in_domain_pawn1, move_in_domain_pawn2, move_in_domain_pawn3, special_move])
        if any([move_in_domain_pawn1, move_in_domain_pawn2]):
            path_available = board[e_rank][e_file]=='xX'

    new_board = deepcopy(board)
    new_board[e_rank][e_file] = s_piece
    new_board[s_rank][s_file] = 'xX'
    if special_move=='en_passant':
        new_board[e_rank-forward][e_file] = 'xX'
    king_rank, king_file = find_piece(playercol, new_board, 'K')
    not_in_check = not_attacked(playercol, king_rank, king_file, new_board)
    print("own_figure, not_occupied_own, move_in_domain, path_available, not_in_check:\n",[own_figure, not_occupied_own, move_in_domain, path_available, not_in_check])
    if all([own_figure, not_occupied_own, move_in_domain, path_available, not_in_check]):
        return special_move if special_move else 'valid'
    else:
        return 'invalid'
def can_make_move(playercol, board):#!!
    pass

"""Main Loop"""
ui = 'none'
print("\n", name.center(width), "\n", (len(name)*"-").center(width), "\n")
while True:
    if ui in ['settings', 'e', 'einstellungen']: #settings
        print(lang['settings'])
    elif ui in ['invert', 'i', 'umkehren']: #color inversion
        col['w'], col['l'], col['d'], col['b'] = col['b'], col['d'], col['l'], col['w']
        print(lang['inverted'])
    elif ui in ['size', 's', 'grösse']: #size options
        try:
            style = styles[input(f" {lang['sizes']}\n {' / '.join([i for i in styles])} > ").lower()]
            width = 8*len(style['K'])+2
            print(lang['size_success'])
        except:
            print(lang['size_fail'])
    elif ui in ['flip', 'f', 'drehen']: #flip toggle
        if flip[1]==1:
            flip = {0:1,1:-1}
            print(lang['flip_on'])
        else:
            flip = {0:1,1:1}
            print(lang['flip_off'])
    elif ui in ['language', 'l', 'sprache']: #language preferences
        try:
            lang = languages[input(f"{lang['language']}\n {' / '.join([i for i in languages])} > ").lower()]
            print(lang['language_success'])
        except:
            print(lang['language_fail'])
    elif ui in ['time', 't', 'zeit']: #time configuration
        try:
            time_s = abs(int(input(lang['time_query'].format(time_s))))
            print(lang['time_success'].format(time_s))
            times = {'w':time_s, 'b':time_s}
        except:
            print(lang['time_fail'])
    elif ui in ['', 'play', 'p', 'spielen']: #actual chess game
        print(lang['play'])
        exit_game = ''
        while True: #playerturns
            playercol = {0:'w',1:'b'}[turn%2] #whose turn it is
            display_board(board) #main display
            print("\n"+f"{lang[playercol]}{lang['turn']}".center(width))
            if time_s: #how much time is left, starting timer
                print(lang['time_left'].format(lang[playercol], times[playercol]).center(width))
                time_start = time()
                time_limit = Timer(times[playercol], time_up_toggle)
                time_limit.start()
            king_rank, king_file = find_piece(playercol, board, 'K')
            if not not_attacked(playercol, *find_piece(playercol, board, 'K'), board): #Whether a player is in check
                print("\n"+f"{lang[playercol]}{lang['check']}".center(width))
            while True: #loops until a valid move is entered by the user
                #try:
                    move_start, move_end, move_force, *rest = input(lang['make_move']).lower().split()+[0,0,0]
                    if time_up:
                        break
                    if move_start in ['resign','aufgeben']: #resigning
                        exit_game ='resign'
                        break
                    elif move_start in ['draw', 'remis'] and input(lang['draw_query'].format(lang[playercol], lang[{'w':'b','b':'w'}[playercol]])).lower() in ['yes', 'ja']: #agreed draw
                        exit_game = 'draw'
                        break
                    elif move_start in ['pause']: #pausing game
                        exit_game = 'pause'
                        break
                    s_file, s_rank = a_to_n[move_start[0]], int(move_start[1])-1
                    e_file, e_rank = a_to_n[move_end[0]], int(move_end[1])-1
                    assert all([-1<i<8 for i in [s_file, s_rank, e_file, e_rank]]) #on the board
                    move_type = validate_move(s_rank, s_file, e_rank, e_file, playercol) #valid move?
                    assert move_type!='invalid' or move_force=='force'
                    break
                #except:
                    continue
            if time_s: #subtract time from player clock
                time_limit.cancel()
                times[playercol] -= time() - time_start #update player time
            if time_up: #win on time
                print("\n\n",lang['time_up'].format(lang[playercol], lang[{'w':'b','b':'w'}[playercol]]).center(width))
                reset()
                break
            if exit_game=='resign': #resign
                print(lang['resign'].format(lang[playercol], lang[{'w':'b','b':'w'}[playercol]]).center(width))
                reset()
                break
            elif exit_game=='draw': #agreed draw
                print(lang['draw'].center(width))
                reset()
                break
            elif exit_game=='pause': #game paused
                print(lang['pause'].center(width))
                break
            if board[e_rank][e_file] != 'xX': #piece taken?
                piece_taken = 0
            else:
                piece_taken += 1
            if board[s_rank][s_file][1] == 'P': #pawn moved?
                pawn_moved = 0
            else:
                pawn_moved += 1
            if move_type=='valid': #normal move found
                board[e_rank][e_file] = board[s_rank][s_file]
                board[s_rank][s_file] = 'xX'
            elif move_type=='conversion': #pawn promotion
                conversion_dict = {'queen':'Q','rook':'R','bishop':'B','knight':'N',
                'dame':'Q','turm':'R','läufer':'B','springer':'N',}
                while True:
                    ui = input(lang['conversion']).lower()
                    if ui not in conversion_dict: continue
                    break
                board[e_rank][e_file] = playercol+conversion_dict[ui]
                board[s_rank][s_file] = 'xX'
            elif move_type=='en_passant': #en passant
                board[e_rank-{'w':1, 'b':-1}[playercol]][e_file] = 'xX'
                board[e_rank][e_file] = board[s_rank][s_file]
                board[s_rank][s_file] = 'xX'
            elif move_type=='castling_kingside': #kingside castling
                board[e_rank][e_file] = board[s_rank][s_file]
                board[s_rank][s_file] = 'xX'
                board[s_rank][s_file+1] = playercol+'R'
                board[e_rank][7] = 'xX'
            elif move_type=='castling_queenside': #queenside castling
                board[e_rank][e_file] = board[s_rank][s_file]
                board[s_rank][s_file] = 'xX'
                board[s_rank][s_file-1] = playercol+'R'
                board[e_rank][0] = 'xX'
            elif move_force=='force': #???
                board[e_rank][e_file] = board[s_rank][s_file]
                board[s_rank][s_file] = 'xX'
            history.append((move_start, move_end)) #add move to history
            board_history.append(tuple(tuple(rank) for rank in board)) #add board to board history
            if board_history.count(board_history[-1])>2: #draw by threefold repetition - DISCLAIMER: WILL NOT TAKE INTO ACCOUNT THE POSSIBILITIES OF 'en passant' OR 'castling' !!
                print(lang['draw_threefold'].center(width))
                print(lang['draw'].center(width))
                reset()
                break
            elif pawn_moved>=50 or piece_taken>=50: #draw by 50-move rule
                print(lang['draw_50moverule'+('_pawn' if pawn_moved>=50 else '_piece')].center(width))#!!
                print(lang['draw'].center(width))
                reset()
                break
            material = []
            for rank in board:
                for square in rank:
                    if square!='xX' and square[1]!='K':
                        material.append(square)
            insufficient_material = [(),('bB'),('wB'), ('bN'), ('wN')]
            if tuple(material) in insufficient_material: #draw by insufficient material
                print(lang['draw_material'].center(width))
                print(lang['draw'].center(width))
                reset()
                break
            if tuple(material) in [('bB','wB'), ('wB','bB')]: #draw by insufficient material (2 bishops on the same color)
                B1_rank, B1_file = find_piece(material[0][0], board, 'B')
                B2_rank, B2_file = find_piece(material[1][0], board, 'B')
                if ((B1_rank+B1_file)%2)==((B2_rank+B2_file)%2):
                    print(lang['draw_material'].center(width))
                    print(lang['draw'].center(width))
                    reset()
                    break
            turn += 1
    elif ui in ['quit', 'q', 'exit', 'schliessen']: #close script
        break
    ui = input(lang['main']).lower() #main menu user input
#Dekoratives
    # Piece/Point Display
#Praktisches
    # Checkmate
    # Draw: Stalemate (Patt)
#Mögliche Zukunftspläne
    # Fischerandom/960 chess
    # Undo
    # (Simple AI)
    # (Notation/Loading games)
