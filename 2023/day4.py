import re

file_path = 'input_files/day4.txt'

with open(file_path, 'r') as file:
	day4_puzzle_input = file.read()


def parse_scratcher(puzzle_input):
	scratchers = []
	numbers_regex = r'\d+'
	lines = puzzle_input.split('\n')

	for line in lines:
		line_state = line.split(':')

		if len(line_state) > 1:
			game_state = line.split(':')[1].strip()

			t = game_state.split('|')
			winning_numbers_str = t[0]
			card_numbers_str = t[1]
			winning_numbers = [int(n) for n in re.findall(numbers_regex, winning_numbers_str)]
			card_numbers = [int(n) for n in re.findall(numbers_regex, card_numbers_str)]

			scratchers.append((winning_numbers, card_numbers))

	return scratchers


def part_one(puzzle_input):
	points = 0

	for card in parse_scratcher(puzzle_input):
		overlap = len(set(card[0]) & set(card[1]))

		if overlap >= 1:
			points += pow(2, overlap - 1)

	return points


def part_two(puzzle_input):
	cards = [1] * (len(puzzle_input.split('\n')) - 1)
	print(len(cards))

	for i, card in enumerate(parse_scratcher(puzzle_input)):
		overlap = set(card[0]) & set(card[1])
		for j in range(len(overlap)):
			cards[i + j + 1] += cards[i]

	return sum(cards)


# https://adventofcode.com/2023/day/4
def main():
	print('Part One:', part_one(day4_puzzle_input))
	print('Part Two:', part_two(day4_puzzle_input))


if __name__ == '__main__':
	main()
