def make_board():
	return [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]
	
def print_board(board):
	for i in range(len(board)):
		print('| ', end='')
		for j in range(len(board)):
			print(board[i][j], end=' ')
		print('|')
			


def clear(board):
	for i in range(len(board)):
		return [['_']*len(board)]*len(board)
		
def make_move(who, row, col, board):
	board[row][col] = who
	
	
def hasWon(who, board):
	if board[0][0]==board[0][1]==board[0][2]==who or \
			board[1][0]==board[1][1]==board[1][2]==who or \
			board[2][0]==board[2][1]==board[2][2]==who:
		return True
		
	if board[0][0]==board[1][0]==board[2][0]==who or \
			board[0][1]==board[1][1]==board[2][1]==who or \
			board[0][2]==board[1][2]==board[2][2]==who:
		return True
		
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] == who or \
	board[0][2] == board[1][1] == board[2][0] and board[2][0] == who:
		return True
	
	return False

				 
def gameOver(board):
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] != '_':
				return False
	return True
				
def game():
	board = make_board()
	print_board(board)
	while True:
		who = input('Enter who: ')
		row = int(input('Row: '))
		col = int(input('Col: '))
		make_move(who, row, col, board)
		print_board(board)
		if gameOver(board):
			break
		if hasWon(who, board) == True:
			print('The winner is: ', who)
			break
			
		
		
print(game())