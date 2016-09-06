def add_vectors(a, b):
    return a[0] + b[0], a[1] + b[1]


def subtract_vector(a, b):
    return a[0] - b[0], a[1] - b[1]


def vector_equality(a, b):
    return a[0] == b[0] and a[1] == b[1]


def direction_to_direction_vector(direction):

    if direction == 'up':
        return 0, -1
    elif direction == 'right':
        return 1, 0
    elif direction == 'down':
        return 0, 1
    elif direction == 'left':
        return -1, 0
    elif direction == 'none':
        return 0, 0
    else:
        raise Exception('not a valid direction!')
