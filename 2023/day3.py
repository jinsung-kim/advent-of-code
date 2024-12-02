import re

file_path = 'day3.txt'
# https://adventofcode.com/2023/day/3

with open(file_path, 'r') as file:
	day_3_puzzle_input = file.read()


def part_one(puzzle_input: str):
	schematic_sum = 0
	lines = puzzle_input.split('\n')

	symbol_regex = r'[^.\d]'
	symbol_adjacent = set()
	for i, line in enumerate(lines):
		for m in re.finditer(symbol_regex, line):
			j = m.start()
			symbol_adjacent |= {(r, c) for r in range(i - 1, i + 2) for c in range(j - 1, j + 2)}

	numbers_regex = r'\d+'
	for i, line in enumerate(lines):
		for m in re.finditer(numbers_regex, line):
			if any((i, j) in symbol_adjacent for j in range(*m.span())):
				schematic_sum += int(m.group())

	return schematic_sum


def part_two(puzzle_input: str):
	pass


# https://adventofcode.com/2023/day/3
def main():
	print('Part One:', part_one(day_3_puzzle_input))  # 550064


if __name__ == '__main__':
	main()
