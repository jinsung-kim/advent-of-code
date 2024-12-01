from collections import Counter

file_path = 'day1.txt'


def main():
    location_ids = []

    with open(file_path, 'r') as file:
        for line in file:
            location_ids.extend(map(int, line.split()))

    employee_list_1 = [location_ids[i] for i in range(0, len(location_ids), 2)]
    employee_list_2 = [location_ids[i] for i in range(1, len(location_ids), 2)]

    assert len(employee_list_1) == len(employee_list_2)

    employee_list_1.sort()
    employee_list_2.sort()

    d = 0

    # Part One.
    for i in range(len(employee_list_1)):
        d += abs(employee_list_1[i] - employee_list_2[i])

    print(d)

    # Part Two.
    sim_score = 0
    c = Counter(employee_list_2)

    for location_id in employee_list_1:
        sim_score += (c[location_id] * location_id)

    print(sim_score)


if __name__ == '__main__':
    main()
