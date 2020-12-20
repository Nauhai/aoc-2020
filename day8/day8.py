
def execute_program(operations):
    acc = 0
    cursor = 0
    cursor_values = []
    while cursor not in cursor_values:
        cursor_values.append(cursor)
        operation, value = operations[cursor]
        cursor += value if operation == 'jmp' else 1
        if operation == 'acc':
            acc += value
        if cursor >= len(operations):
            return acc, cursor, True
    return acc, cursor, False


def immutable_replace(old_list, i, elem):
    new_list = list(old_list)
    new_list[i] = elem
    return new_list


def solve_problem1(operations):
    return execute_program(operations)[0]


def solve_problem2(operations):
    ops = ['nop', 'jmp']
    for i, (operation, value) in enumerate(operations):
        if operation in ops:
            acc, cursor, finished = execute_program(immutable_replace(operations, i, (ops[ops.index(operation) - 1], value)))
            if finished:
                return acc


def operation_mapper(operation_input):
    operation, value = operation_input.strip().split(' ')
    return operation, int(value)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        operations = list(map(operation_mapper, file.readlines()))
        print('Problem 1:', solve_problem1(operations))
        print('Problem 2:', solve_problem2(operations))
