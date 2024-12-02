import re

file_path = 'input_files/day3.txt'
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
	gear_ratio_sum = 0
	lines = puzzle_input.split('\n')

	gear_regex = r'\*'
	gears = dict()

	for i, line in enumerate(lines):
		for m in re.finditer(gear_regex, line):
			j = m.start()
			gears[(i, j)] = []

	numbers_regex = r'\d+'
	for i, line in enumerate(lines):
		for m in re.finditer(numbers_regex, line):
			num_start, num_end = m.start(), m.end()
			for r in range(i - 1, i + 2):
				for c in range(num_start - 1, num_end + 1):
					if (r, c) in gears:
						gears[(r, c)].append(int(m.group()))

	for gear_engine_numbers in gears.values():
		if len(gear_engine_numbers) == 2:
			gear_ratio_sum += (gear_engine_numbers[0] * gear_engine_numbers[1])

	return gear_ratio_sum


# https://adventofcode.com/2023/day/3
def main():
	print('Part One:', part_one(day_3_puzzle_input))  # 550064
	print('Part Two:', part_two(day_3_puzzle_input))  # 85010461


if __name__ == '__main__':
	main()
