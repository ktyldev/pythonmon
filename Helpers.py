class Helpers:

    @staticmethod
    def add_vectors(a, b):
        return a[0] + b[0], a[1] + b[1]

    @staticmethod
    def vector_equality(a, b):
        return a[0] == b[0] and a[1] == b[1]