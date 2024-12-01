import re
file_path = 'day1.txt'

word_to_digit = {
	"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
	"six": "6", "seven": "7", "eight": "8", "nine": "9"
}


# https://adventofcode.com/2023/day/1
def main():
	calibration_sum = 0
	with open(file_path, 'r') as file:
		for line in file:
			digits = re.findall(r'\d', line)

			if len(digits) == 1:
				calibration_sum += int(digits[0] * 2)
			elif len(digits) >= 2:
				calibration_sum += int(digits[0] + digits[-1])

		# Part One.
		print(calibration_sum)  # 53334

	real_calibration_sum = 0
	with open(file_path, 'r') as file:
		for line in file:
			matches = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
			digits = [word_to_digit.get(match, match) for match in matches]

			if len(digits) == 1:
				real_calibration_sum += int(digits[0] * 2)
			elif len(digits) >= 2:
				real_calibration_sum += int(digits[0] + digits[-1])

		# Part Two.
		print(real_calibration_sum)  # 52834


if __name__ == '__main__':
	main()
