def add_vectors(a, b):
    return int(a[0] + b[0]), int(a[1] + b[1])


def subtract_vector(a, b):
    return int(a[0] - b[0]), int(a[1] - b[1])


def multiply_vector(vector, n):
    return int(vector[0] * n), int(vector[1] * n)


def divide_vector(vector, n):
    return int(vector[0] // n), int(vector[0] // n)


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


def colour_from_tile_type(tile_type):
    if tile_type == 'collision':
        return 255, 0 ,0
    elif tile_type == 'surf':
        return 0, 255, 0
    else:
        return None
