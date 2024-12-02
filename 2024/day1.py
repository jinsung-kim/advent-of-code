from collections import Counter

file_path = 'input_files/day1.txt'

with open(file_path, 'r') as file:
    day_1_puzzle_input = file.read()


def part_one():
    location_ids = []
    lines = day_1_puzzle_input.split('\n')

    for line in lines:
        location_ids.extend(map(int, line.split()))

    employee_list_l = [location_ids[i] for i in range(0, len(location_ids), 2)]
    employee_list_r = [location_ids[i] for i in range(1, len(location_ids), 2)]

    assert len(employee_list_l) == len(employee_list_r)

    employee_list_l.sort()
    employee_list_r.sort()

    d = 0

    for i in range(len(employee_list_l)):
        d += abs(employee_list_l[i] - employee_list_r[i])

    return d, employee_list_l, employee_list_r  # Used for part two.


def part_two(employee_list_l, employee_list_r):
    sim_score = 0
    c = Counter(employee_list_r)

    for location_id in employee_list_l:
        sim_score += (c[location_id] * location_id)

    return sim_score


# https://adventofcode.com/2024/day/1
def main():
    ans = part_one()
    print('Part One:', ans[0])  # 2375403
    employee_list_l, employee_list_r = ans[1], ans[2]
    print('Part Two:', part_two(employee_list_l, employee_list_r))  # 23082277


if __name__ == '__main__':
    main()
