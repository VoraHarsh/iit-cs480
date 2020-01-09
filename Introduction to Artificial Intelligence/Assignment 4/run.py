from games import *

ttt = TicTacToe()
board = {}
moves = []

print("Enter the first row.")

# This Code will take Input from user as a list
# For example the User should give the Input as X - O with spaces betweewn all the three elements 
# All the Inputs must be Capital Letter

a = list(input().split(" "))

a1 = a[0]
a2 = a[1]
a3 = a[2]

if a1!='-':
	board.update({(1,1) : a1})
else: moves.append((1,1))

if a2!='-':
	board.update({(1,2) : a2})
else: moves.append((1,2))

if a3!='-':
	board.update({(1,3) : a3})
else: moves.append((1,3))


print("Enter the second row.")

# This Code will take Input from user as a list
# For example the User should give the Input as X - O with spaces betweewn all the three elements
# All the Inputs must be Capital Letter

b = list(input().split(" "))
b1 = b[0] 
b2 = b[1]
b3 = b[2]

if b1!='-':
	board.update({(2,1) : b1})
else: moves.append((2,1))

if b2!='-':
	board.update({(2,2) : b2})
else: moves.append((2,2))

if b3!='-':
	board.update({(2,3) : b3})
else: moves.append((2,3))


print("Enter the third row.")

# This Code will take Input from user as a list
# For example the User should give the Input as - - - with spaces betweewn all the three elements
# All the Inputs must be Capital Letter

c = list(input().split(" "))
c1 = c[0]
c2 = c[1]
c3 = c[2]

if c1!='-':
	board.update({(3,1) : c1})
else: moves.append((3,1))

if c2!='-':
	board.update({(3,2) : c2})
else: moves.append((3,2))

if c3!='-':
	board.update({(3,3) : c3})
else: moves.append((3,3))

#This code will check no. of X and O on the board and accordingly assign the value to "to_move" variable

if len(board)%2==0:
    to_move = 'X'
else:
    to_move = 'O'
    

# This code will create a gamestate for Tic-Tac-Toe

my_state = GameState(
to_move = to_move,
utility = '0',
board = board,
moves = moves
)

print("Whose turn is it now?")

#This code is checking the total number of steps already played on the board. After Computing it will print X or O depending on whose chance is to play.

if len(my_state.board)%2==0:
	print("X")
else:
	print("O")

print("How many states did the minimax algorithm evaluate?")

# This code will call the minimax_decision method from games.py file and will return the total number of states evaluated.

total_states = minimax_decision(my_state, ttt)
print(total_states[1])


print("How many states did the alpha-beta pruning algorithm evaluate?")


# This code will call the alphabeta_search method from games.py file and will return the total number of states evaluated.

alphabeta_states = alphabeta_search(my_state,ttt)
print(alphabeta_states[1])

print("What is the value of the current state from the perspective of X?")

# This code will call the cur_per method from games.py file and will return 1 or 0 or -1 from the perspective of X.

y= ttt.cur_per(my_state,alphabeta_player)
print(y)

print("Assuming both X and O play optimally, does X have a guaranteed win? Is it a tie? Is it a guaranteed loss for X?")

# This code is just using the variable y from above to print whether "X will Win" or "X will Lose" or "It is a tie"

if y == 1:
	print("X will win")
elif y == -1:
	print("X will lose")
else:
	print("It is a tie")

print("Assuming both X and O would play optimally, how would they play till the game ends?")

# This will return the initial state and states after that, by playing otimally till the end.

ttt.play_game(my_state,alphabeta_player,alphabeta_player)


