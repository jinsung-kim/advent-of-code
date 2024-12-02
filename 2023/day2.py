file_path = 'input_files/day2.txt'

r, g, b = 12, 13, 14

with open(file_path, 'r') as file:
	day_2_puzzle_input = file.read()


def parse_game():
	game_log = []
	game_lines = day_2_puzzle_input.split('\n')
	for game_line in game_lines:
		game_status = game_line.split(':')
		game_id, game_state = int(game_status[0].split(' ')[1]), game_status[1].strip('\n')

		game_log.append([])
		for game_round in game_state.split(';'):
			marbles = [m.strip() for m in game_round.split(',')]

			for color_count in marbles:
				t = color_count.split(' ')
				marble_count, color = int(t[0]), t[1]
				game_log[-1].append((marble_count, color))

	return game_log


def part_one(game_log):
	valid_id_sum = 0
	for (ind, game) in enumerate(game_log):
		valid_game = True
		game_id = ind + 1
		for i in range(len(game)):
			marble_count, color = game[i][0], game[i][1]
			if color == 'red' and marble_count > r:
				valid_game = False
			elif color == 'green' and marble_count > g:
				valid_game = False
			elif color == 'blue' and marble_count > b:
				valid_game = False

		if valid_game:
			valid_id_sum += game_id

	return valid_id_sum


def part_two(game_log):
	power_set = 0

	for game in game_log:
		game_min_marbles = [0, 0, 0]
		for i in range(len(game)):
			marble_count, color = game[i][0], game[i][1]

			if color == 'red':
				game_min_marbles[0] = max(game_min_marbles[0], marble_count)
			elif color == 'green':
				game_min_marbles[1] = max(game_min_marbles[1], marble_count)
			else:
				game_min_marbles[2] = max(game_min_marbles[2], marble_count)

		power_set += (game_min_marbles[0] * game_min_marbles[1] * game_min_marbles[2])

	return power_set


# https://adventofcode.com/2023/day/2
def main():
	game_log = parse_game()

	print('Part One:', part_one(game_log))  # 2105
	print('Part Two:', part_two(game_log))  # 72422


if __name__ == '__main__':
	main()
