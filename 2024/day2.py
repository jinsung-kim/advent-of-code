import re

file_path = 'input_files/day2.txt'

with open(file_path, 'r') as file:
	day2_puzzle_input = file.read()


def report_is_safe(report_levels):
	if len(report_levels) == 0:
		return False

	is_increasing = all(report_levels[i] > report_levels[i - 1] for i in range(1, len(report_levels)))
	is_decreasing = all(report_levels[i] < report_levels[i - 1] for i in range(1, len(report_levels)))

	if not (is_decreasing or is_increasing):
		return False

	for i in range(1, len(report_levels)):
		d = abs(report_levels[i] - report_levels[i - 1])

		if d < 1 or d > 3:
			return False

	return True


def part_one(puzzle_input):
	valid_reports = 0
	lines = puzzle_input.split('\n')

	for line in lines:
		report_levels = list(map(int, re.findall(r'\d+', line)))
		if report_is_safe(report_levels):
			valid_reports += 1

	return valid_reports


def part_two(puzzle_input):
	damper_valid_reports = 0
	lines = puzzle_input.split('\n')

	for line in lines:
		if report_is_safe(line):
			damper_valid_reports += 1
			continue

		report = list(map(int, re.findall(r'\d+', line)))
		for i in range(len(report)):
			t = report.copy()
			del t[i]
			if report_is_safe(t):
				damper_valid_reports += 1
				break

	return damper_valid_reports


# https://adventofcode.com/2024/day/2
def main():
	print('Part One:', part_one(day2_puzzle_input))  # 334
	print('Part Two:', part_two(day2_puzzle_input))  # 400


if __name__ == '__main__':
	main()
