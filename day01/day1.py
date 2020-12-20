
def solve_problem1(numbers):
    for i, number in enumerate(numbers):
        for other in numbers[i:]:
            if number + other == 2020:
                return number * other


def solve_problem2(numbers):
    for i, first in enumerate(numbers):
        for j, second in enumerate(numbers[i:]):
            for third in numbers[j:]:
                if first + second + third == 2020:
                    return first * second * third


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        numbers = list(map(int, file.readlines()))
        print('Problem 1:', solve_problem1(numbers))
        print('Problem 2:', solve_problem2(numbers))
