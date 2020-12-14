import functools


def solve_problem1(groups):
    return sum([len(set(functools.reduce(lambda a, b: a + ''.join(b), group, ''))) for group in groups])


def solve_problem2(groups):
    return sum([len(list(filter(lambda x: all(x in answer for answer in group[1:]), group[0]))) for group in groups])


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        groups = []
        group = []
        for line in map(lambda line: line.strip(), file.readlines()):
            if not line:
                groups.append(group)
                group = []
                continue
            group.append(line)
        groups.append(group)

        print('Problem 1:', solve_problem1(groups))
        print('Problem 2:', solve_problem2(groups))
