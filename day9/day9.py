
def solve_problem1(numbers, slice_length):
    for i in range(len(numbers) - slice_length):
        slc = numbers[i:i+slice_length]
        number = numbers[i+slice_length]
        if not is_valid(number, slc):
            return number


def is_valid(number, slc):
    for index, i in enumerate(slc):
        for j in slc[index+1:]:
            if number == i + j:
                return True
    return False


def solve_problem2(numbers, number):
    length = len(numbers)
    for i, num1 in enumerate(numbers):
        if num1 > number:
            continue
        for j in range(i+1, length):
            num2 = numbers[j]
            if num2 > number or num1 + num2 > number:
                continue
            slc = numbers[i:j+1]
            if sum(slc) == number:
                return min(slc) + max(slc)
    return None


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        numbers = list(map(lambda line: int(line.strip()), file.readlines()))
        number = solve_problem1(numbers, 25)
        print('Problem 1:', number)
        print('Problem 2:', solve_problem2(numbers, number))
