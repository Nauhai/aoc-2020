from abc import *

class Password(ABC):
    def __init__(self, password_input):
        policy, password = password_input.split(': ')
        rang, letter = policy.split(' ')
        mi, ma = map(int, rang.split('-'))

        self.policy = (mi, ma, letter)
        self.password = password

        super().__init__()

    @abstractmethod
    def is_valid(self):
        pass

class Password1(Password):
    def is_valid(self):
        return len(list(filter(lambda char: char == self.policy[2], self.password))) in range(self.policy[0], self.policy[1] + 1)

class Password2(Password):
    def is_valid(self):
        first, second, char = self.policy[0] - 1, self.policy[1] - 1, self.policy[2]
        return (self.password[first] == char and self.password[second] != char) or (self.password[first] != char and self.password[second] == char)



def solve_problem1(passwords):
    return len(list(filter(lambda password: password.is_valid(), map(lambda password: Password1(password), passwords))))

def solve_problem2(passwords):
    return len(list(filter(lambda password: password.is_valid(), map(lambda password: Password2(password), passwords))))


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        passwords = list(map(lambda password: password.strip(), file.readlines()))
        print('Problem1:', solve_problem1(passwords))
        print('Problem2:', solve_problem2(passwords))
