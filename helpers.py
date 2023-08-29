from random import randint


def generate_random_array(size: int, max: int) -> list[int]:
    return [randint(0, max) for _ in range(size)]


def generate_random_arrays(max: int, min_size: int, max_size: int, step: int) -> list[list[int]]:
    return [generate_random_array(max_size, max) for max_size in range(min_size, max_size, step)]


def generate_random_matrix(rows: int, cols: int, max: int) -> list[list[int]]:
    return [generate_random_array(cols, max) for _ in range(rows)]


def generate_random_matrices(max: int, min_size: int, max_size: int, step: int) -> list[list[list[int]]]:
    return [generate_random_matrix(max_size, max_size, max) for max_size in range(min_size, max_size, step)]


def is_sorted(arr: list[int]) -> bool:
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


def is_sorted_matrix(arr: list[list[int]]) -> bool:
    transpose(arr)
    for row in arr:
        if not is_sorted(row):
            transpose(arr)
            return False
    transpose(arr)
    return True


def transpose(arr: list[list[int]]) -> list[list[int]]:
    """Rotate a matrix 90 degrees clockwise"""

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    return arr


def print_matrix(arr: list[list[int]]):
    for row in arr:
        print(row)