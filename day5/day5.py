
def find_seat(seq, rngs = (range(128), range(8))):
    row, column = rngs

    if len(row) == 1 and len(column) == 1:
        return row[0] * 8 + column[0]

    char = seq[0]
    if char == 'F':
        row = row[:len(row)//2]
    elif char == 'B':
        row = row[len(row)//2:]
    elif char == 'R':
        column = column[len(column)//2:]
    elif char == 'L':
        column = column[:len(column)//2]

    return find_seat(seq[1:], (row, column))


def solve_problem1(seats):
    return max(seats)


def solve_problem2(seats, max_seat):
    for i in range(max_seat):
        if i not in seats and i-1 in seats and i+1 in seats:
            return i
    return None


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        seats = [find_seat(seat) for seat in list(map(lambda seat: seat.strip(), file.readlines()))]
        max_seat = solve_problem1(seats)
        print('Problem 1:', max_seat)
        print('Problem 2:', solve_problem2(seats, max_seat))
