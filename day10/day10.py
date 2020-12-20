
def solve_problem1(adapters):
    diff1 = 0
    diff3 = 0
    for a, b in [adapters[i:i + 2] for i in range(len(adapters) - 1)]:
        diff = b - a
        if diff == 1:
            diff1 += 1
        elif diff == 3:
            diff3 += 1
    return diff1 * diff3


def solve_problem2(adapters):
    possibilities = get_possibilities(adapters)
    adapters_reversed = adapters[::-1]
    paths = {adapters_reversed[0]: 1}
    for adapter in adapters_reversed[1:]:
        paths[adapter] = sum([paths[poss] for poss in possibilities[adapter]])
    return paths[adapters[0]]


def get_possibilities(adapters):
    possibilities = {}
    for i, adapter in enumerate(adapters):
        possibilities[adapter] = []
        if i == len(adapters) - 1:
            return possibilities
        for other in adapters[i + 1:]:
            if other - adapter > 3:
                break
            possibilities[adapter].append(other)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        adapters = list(map(lambda line: int(line.strip()), file.readlines()))
        adapters.append(0)
        adapters.append(max(adapters) + 3)
        adapters = sorted(adapters)
        print('Problem 1:', solve_problem1(adapters))
        print('Problem 2:', solve_problem2(adapters))
