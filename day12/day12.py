
degrees_orientations = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W'
}

orientations_degrees = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270
}


def solve_problem1(actions):
    orientation = 90

    ship_pos = {
        'N': 0,
        'E': 0,
        'S': 0,
        'W': 0
    }

    for action, value in actions:
        if action in ship_pos.keys():
            ship_pos[action] += value

        elif action == 'L':
            orientation -= value
        elif action == 'R':
            orientation += value
        elif action == 'F':
            ship_pos[degrees_orientations[orientation % 360]] += value

    return get_manhattan_distance(ship_pos)


def solve_problem2(actions):
    waypoint_pos = {
        'N': 1,
        'E': 10,
        'S': 0,
        'W': 0
    }

    ship_pos = {
        'N': 0,
        'E': 0,
        'S': 0,
        'W': 0
    }

    for action, value in actions:
        if action in waypoint_pos.keys():
            waypoint_pos[action] += value

        elif action in 'LR':
            new_pos = {
                'N': 0,
                'E': 0,
                'S': 0,
                'W': 0
            }
            for orientation, units in waypoint_pos.items():
                new_pos[orientation] = waypoint_pos[degrees_orientations[(orientations_degrees[orientation] + (value if action == 'L' else -value)) % 360]]
            waypoint_pos = new_pos

        elif action == 'F':
            for orientation in ship_pos.keys():
                ship_pos[orientation] += value * waypoint_pos[orientation]

    return get_manhattan_distance(ship_pos)


def get_manhattan_distance(ship_pos):
    return abs(ship_pos['N'] - ship_pos['S']) + abs(ship_pos['E'] - ship_pos['W'])


def action_mapper(action_input):
    action = action_input.strip()
    return action[0], int(action[1:])


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        actions = list(map(action_mapper, file.readlines()))
        print('Problem 1:', solve_problem1(actions))
        print('Problem 2:', solve_problem2(actions))
