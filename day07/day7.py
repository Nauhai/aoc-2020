
def solve_problem1(bags):
    return len(list(filter(lambda bag: contains_shiny(bag, bags), bags.values())))


def contains_shiny(bag, bags):
    if len(bag) == 0:
        return False
    
    for sub_bag in bag:
        if sub_bag[1] == 'shiny gold' or contains_shiny(bags[sub_bag[1]], bags):
            return True
    return False


def solve_problem2(bags):
    return count_bags(bags['shiny gold'], bags)


def count_bags(root, bags):
    total = 0
    queue = [root]
    while len(queue) > 0:
        n = len(queue)
        while(n > 0):
            sub_bags = queue.pop()
            for bag in sub_bags:
                total += bag[0]
                queue.append(bags[bag[1]] * bag[0])
            n -= 1
    return total


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        bags = {}
        for line in map(lambda line: line.strip(), file.readlines()):
            name, content = line.split(' bags contain ')
            content = content[:-1]
            sub_bags = []
            if content != 'no other bags':
                for bag in content.split(', '):
                    amount, bname = bag.split(' ', 1)
                    sub_bags.append((int(amount), ' '.join(bname.split(' ')[:-1])))
            bags[name] = sub_bags
        
        print('Problem 1:', solve_problem1(bags))
        print('Problem 2:', solve_problem2(bags))
