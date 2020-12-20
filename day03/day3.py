import functools


def solve_problem1(plan, slope):
    x, y = 0, 0
    trees = 0
    breadth = len(plan[0])
    while y < len(plan):
        if plan[y][x % breadth] == '#':
            trees += 1
        x += slope[0]
        y += slope[1]
    return trees


def solve_problem2(plan, slopes):
    return functools.reduce(lambda a, b: a * b, map(lambda slope: solve_problem1(plan, slope), slopes), 1)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        plan = list(map(lambda line: line.strip(), file.readlines()))
        slopes = [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2)
        ]
        print('Problem 1:', solve_problem1(plan, (3, 1)))
        print('Problem 2:', solve_problem2(plan, slopes))
