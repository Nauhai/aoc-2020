from copy import deepcopy


def solve(seats, neigh_func, tolerance):
    seats_length = len(seats)
    prev_seats = []
    while seats != prev_seats:
        prev_seats = deepcopy(seats)
        for i, seats_line in enumerate(prev_seats):
            line_length = len(seats_line)
            for j, seat in enumerate(seats_line):
                if seat not in 'L#':
                    continue
                neighbours = neigh_func(i, j, seats_length, line_length, prev_seats)

                if seat == 'L' and all(neigh != '#' for neigh in neighbours):
                    seats[i][j] = '#'

                if seat == '#' and len(list(filter(lambda neigh: neigh == '#', neighbours))) >= tolerance:
                    seats[i][j] = 'L'

    return count_occupied_seats(seats)


directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]


def get_neighbours(i, j, seats_length, line_length, seats):
    neighbours = []
    for i1, j1 in directions:
        if 0 <= i + i1 < seats_length and 0 <= j + j1 < line_length:
            neighbours.append(seats[i + i1][j + j1])
    return neighbours


def get_first_adjacents_seats(i, j, seats_length, line_length, seats):
    adjacents = []
    for i1, j1 in directions:
        ci, cj = i, j
        while 0 <= ci + i1 < seats_length and 0 <= cj + j1 < line_length:
            ci, cj = ci + i1, cj + j1
            if (seat := seats[ci][cj]) in 'L#':
                adjacents.append(seat)
                break
    return adjacents


def count_occupied_seats(seats):
    count = 0
    for line in seats:
        for seat in line:
            if seat == '#':
                count += 1
    return count


def solve_problem1(seats):
    return solve(seats, get_neighbours, 4)


def solve_problem2(seats):
    return solve(seats, get_first_adjacents_seats, 5)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        seats = list(map(lambda line: list(line.strip()), file.readlines()))
        print('Problem 1:', solve_problem1(deepcopy(seats)))
        print('Problem 2:', solve_problem2(deepcopy(seats)))
