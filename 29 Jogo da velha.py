# Este exercício é único porque depende da saída de outros exercícios que precisam ser colocados juntos para fazer a
# solução final. O objetivo é praticar as funções e como elas funcionam juntas em programas maiores.
# Os 3 exercícios acima sugerem dividir seu jogo do jogo da velha em (pelo menos) 4 funções: Uma função para desenhar
# o tabuleiro do jogo (e a localização das peças) Uma função para verificar se há um vencedor no jogo Uma função para
# adicionar a entrada do usuário ao estado do jogo Uma função principal que chama as outras e joga o jogo

def draw_line(width, edge, filling):
	print(filling.join([edge] * (width + 1)))

def draw_board(width, height):
	draw_line(width, " ", "__")
	for i in range(height):
		draw_line(width, "|", "__")
	print("\n")

def display_winner(player):
	if player == 0:
		print("Tie")
	else:
		print("Player " + str(player) + " wins!")

def check_row_winner(row):
	"""
	Return the player number that wins for that row.
	If there is no winner, return 0.
	"""
	if row[0] == row[1] and row[1] == row[2]:
		return row[0]
	return 0

def get_col(game, col_number):
	return [game[x][col_number] for x in range(3)]

def get_row(game, row_number):
	return game[row_number]

def check_winner(game):
	game_slices = []
	for index in range(3):
		game_slices.append(get_row(game, index))
		game_slices.append(get_col(game, index))

	# check diagonals
	down_diagonal = [game[x][x] for x in range(3)]
	up_diagonal = [game[0][2], game[1][1], game[2][0]]
	game_slices.append(down_diagonal)
	game_slices.append(up_diagonal)

	for game_slice in game_slices:
		winner = check_row_winner(game_slice)
		if winner != 0:
			display_winner(winner)
			return winner

	display_winner(winner)
	return winner

def start_game():
	return [[0, 0, 0] for x in range(3)]

def display_game(game):
	d = {2: "O", 1: "X", 0: " "}
	game_string = []
	for row_num in range(3):
		new_row = []
		for col_num in range(3):
			new_row.append(d[game[row_num][col_num]])
		game_string.append(new_row)
	print(game_string)


def add_piece(game, player, row, column):
	"""
	game: game state
	player: player number
	row: 0-index row
	column: 0-index column
	"""
	game[row][column] = player
	return game

def convert_input_to_coordinate(user_input):
	return user_input - 1

def switch_player(player):
	if player == 1:
		return 2
	else:
		return 1


if __name__ == '__main__':
	game = start_game()
	display_game(game)
	player = 1


	def draw_line(width, edge, filling):
		print(filling.join([edge] * (width + 1)))


	def display_winner(player):
		if player == 0:
			print("Tie")
		else:
			print("Player " + str(player) + " wins!")


	def check_row_winner(row):
		"""
		Return the player number that wins for that row.
		If there is no winner, return 0.
		"""
		if row[0] == row[1] and row[1] == row[2]:
			return row[0]
		return 0


	def get_col(game, col_number):
		return [game[x][col_number] for x in range(3)]


	def get_row(game, row_number):
		return game[row_number]


	def check_winner(game):
		game_slices = []
		for index in range(3):
			game_slices.append(get_row(game, index))
			game_slices.append(get_col(game, index))

		# check diagonals
		down_diagonal = [game[x][x] for x in range(3)]
		up_diagonal = [game[0][2], game[1][1], game[2][0]]
		game_slices.append(down_diagonal)
		game_slices.append(up_diagonal)

		for game_slice in game_slices:
			winner = check_row_winner(game_slice)
			if winner != 0:
				return winner

		return winner


	def start_game():
		return [[0, 0, 0] for x in range(3)]


	def display_game(game):
		d = {2: "O", 1: "X", 0: "_"}
		draw_line(3, " ", "_")
		for row_num in range(3):
			new_row = []
			for col_num in range(3):
				new_row.append(d[game[row_num][col_num]])
			print("|" + "|".join(new_row) + "|")


	def add_piece(game, player, row, column):
		"""
		game: game state
		player: player number
		row: 0-index row
		column: 0-index column
		"""
		game[row][column] = player
		return game


	def check_space_empty(game, row, column):
		return game[row][column] == 0


	def convert_input_to_coordinate(user_input):
		return user_input - 1


	def switch_player(player):
		if player == 1:
			return 2
		else:
			return 1


	def moves_exist(game):
		for row_num in range(3):
			for col_num in range(3):
				if game[row_num][col_num] == 0:
					return True
		return False


	if __name__ == '__main__':
		game = start_game()
		display_game(game)
		player = 1
		winner = 0  # the winner is not yet defined

		# go on forever
		while winner == 0 and moves_exist(game):
			print("Currently player: " + str(player))
			available = False
			while not available:
				row = convert_input_to_coordinate(int(input("Which row? (start with 1) ")))
				column = convert_input_to_coordinate(int(input("Which column? (start with 1) ")))
				available = check_space_empty(game, row, column)
			game = add_piece(game, player, row, column)
			display_game(game)
			player = switch_player(player)
			winner = check_winner(game)
		display_winner(winner)
	# go on forever
	while True:
		print("Currently player: " + str(player))
		row = convert_input_to_coordinate(int(input("Which row? (start with 1) ")))
		column = convert_input_to_coordinate(int(input("Which column? (start with 1) ")))
		game = add_piece(game, player, row, column)
		display_game(game)
		player = switch_player(player)
		player = switch_player(player)

# Outra maneira
def draw_line(width, edge, filling):
	print(filling.join([edge] * (width + 1)))


def display_winner(player):
	if player == 0:
		print("Tie")
	else:
		print("Player " + str(player) + " wins!")

def check_row_winner(row):
	"""
	Return the player number that wins for that row.
	If there is no winner, return 0.
	"""
	if row[0] == row[1] and row[1] == row[2]:
		return row[0]
	return 0

def get_col(game, col_number):
	return [game[x][col_number] for x in range(3)]

def get_row(game, row_number):
	return game[row_number]

def check_winner(game):
	game_slices = []
	for index in range(3):
		game_slices.append(get_row(game, index))
		game_slices.append(get_col(game, index))

	# check diagonals
	down_diagonal = [game[x][x] for x in range(3)]
	up_diagonal = [game[0][2], game[1][1], game[2][0]]
	game_slices.append(down_diagonal)
	game_slices.append(up_diagonal)

	for game_slice in game_slices:
		winner = check_row_winner(game_slice)
		if winner != 0:
			return winner

	return winner

def start_game():
	return [[0, 0, 0] for x in range(3)]

def display_game(game):
	d = {2: "O", 1: "X", 0: "_"}
	draw_line(3, " ", "_")
	for row_num in range(3):
		new_row = []
		for col_num in range(3):
			new_row.append(d[game[row_num][col_num]])
		print("|" + "|".join(new_row) + "|")


def add_piece(game, player, row, column):
	"""
	game: game state
	player: player number
	row: 0-index row
	column: 0-index column
	"""
	game[row][column] = player
	return game

def check_space_empty(game, row, column):
	return game[row][column] == 0

def convert_input_to_coordinate(user_input):
	return user_input - 1

def switch_player(player):
	if player == 1:
		return 2
	else:
		return 1

def moves_exist(game):
	for row_num in range(3):
		for col_num in range(3):
			if game[row_num][col_num] == 0:
				return True
	return False

if __name__ == '__main__':
	game = start_game()
	display_game(game)
	player = 1
	winner = 0  # the winner is not yet defined

	# go on forever
	while winner == 0 and moves_exist(game):
		print("Currently player: " + str(player))
		available = False
		while not available:
			row = convert_input_to_coordinate(int(input("Which row? (start with 1) ")))
			column = convert_input_to_coordinate(int(input("Which column? (start with 1) ")))
			available = check_space_empty(game, row, column)
		game = add_piece(game, player, row, column)
		display_game(game)
		player = switch_player(player)
		winner = check_winner(game)
	display_winner(winner)