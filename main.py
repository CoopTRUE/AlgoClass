from helpers import generate_random_arrays, generate_random_matrices, is_sorted, is_sorted_matrix, transpose
from tqdm import trange, tqdm
from time import sleep, perf_counter_ns
import matplotlib.pyplot as plt


def insertion_sort(arr: list[int]):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1


def selection_sort(arr: list[int]):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]


def bubble_sort(arr: list[int]):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def quick_sort(arr: list[int]):
    # I'll admit that this code is taken from chatgpt, I just needed a quick sorting algo for reference
    def _quicksort(arr: list[int], low: int, high: int):
        if low < high:
            pivot = arr[low]
            left = low + 1
            right = high
            done = False
            while not done:
                while left <= right and arr[left] <= pivot:
                    left = left + 1
                while arr[right] >= pivot and right >= left:
                    right = right - 1
                if right < left:
                    done = True
                else:
                    arr[left], arr[right] = arr[right], arr[left]
            arr[low], arr[right] = arr[right], arr[low]

            _quicksort(arr, low, right - 1)
            _quicksort(arr, right + 1, high)

    _quicksort(arr, 0, len(arr) - 1)


def column_sort(arr: list[list[int]]):
    """Sort a matrix by columns and use transpose to sort by rows"""
    transpose(arr)
    for row in arr:
        insertion_sort(row)
    transpose(arr)


def main():
    # arr = generate_random_array(10_000, 10000)
    # avg_ips = insertion_sort(arr)
    # assert is_sorted(arr), 'Array is not sorted'
    # sleep(0.5)
    # print("Insertion sort: {:.2f} items per second".format(avg_ips))
    avg_speed = []
    total_arr = generate_random_arrays(100_000, 100, 3000, 100)
    for arr in tqdm(total_arr, desc='Insertion sort testing'):
        perf = perf_counter_ns()
        insertion_sort(arr)
        perf = perf_counter_ns() - perf
        assert is_sorted(arr), 'Array is not sorted'
        # items per second
        avg_speed.append(len(arr) / perf * 1e9)
    plt.plot(list(map(len, total_arr)), avg_speed, marker='o', label='Insertion sort')

    avg_speed = []
    total_arr = generate_random_arrays(100_000, 100, 3000, 100)
    for arr in tqdm(total_arr, desc='Selection sort testing'):
        perf = perf_counter_ns()
        selection_sort(arr)
        perf = perf_counter_ns() - perf
        assert is_sorted(arr), 'Array is not sorted'
        # items per second
        avg_speed.append(len(arr) / perf * 1e9)
    plt.plot(list(map(len, total_arr)), avg_speed, marker='x', label='Selection sort')

    avg_speed = []
    total_arr = generate_random_matrices(100_000, 10, 100, 10)
    for arr in tqdm(total_arr, desc='Column sort testing'):
        perf = perf_counter_ns()
        column_sort(arr)
        perf = perf_counter_ns() - perf
        assert is_sorted_matrix(arr), 'Matrix is not sorted'
        # items per second
        avg_speed.append(len(arr) / perf * 1e9)
    plt.plot(list(map(len, total_arr)), avg_speed, marker='^', label='Column sort')

    avg_speed = []
    total_arr = generate_random_arrays(100_000, 100, 3000, 100)
    for arr in tqdm(total_arr, desc='Bubble sort testing'):
        perf = perf_counter_ns()
        bubble_sort(arr)
        perf = perf_counter_ns() - perf
        assert is_sorted(arr), 'Array is not sorted'
        # items per second
        avg_speed.append(len(arr) / perf * 1e9)
    plt.plot(list(map(len, total_arr)), avg_speed, marker='v', label='Bubble sort')

    avg_speed = []
    total_arr = generate_random_arrays(100_000, 100, 3000, 100)
    for arr in tqdm(total_arr, desc='Quick sort testing'):
        perf = perf_counter_ns()
        quick_sort(arr)
        perf = perf_counter_ns() - perf
        assert is_sorted(arr), 'Array is not sorted'
        # items per second
        avg_speed.append(len(arr) / perf * 1e9)
    plt.plot(list(map(len, total_arr)), avg_speed, marker='s', label='Quick sort')

    plt.legend()
    plt.xlabel('Array length')
    plt.ylabel('Items per second')
    plt.title('Average Iterations Per Second vs Array Size')
    plt.ticklabel_format(style='plain', axis='both', useOffset=False)
    plt.show()

    #
    # arr = generate_random_array(10_000, 100000)
    # avg_ips = selection_sort(arr)
    # assert is_sorted(arr), 'Array is not sorted'
    # sleep(0.5)
    # print("Insertion sort: {:.2f} items per second".format(avg_ips))
    #
    # arr = generate_random_matrix(1000, 1000, 100000)
    # avg_ips = column_sort(arr)
    # assert is_sorted_matrix(arr), 'Matrix is not sorted'
    # sleep(0.5)
    # print("Column sort: {:.2f} items per second".format(avg_ips))


if __name__ == '__main__':
    main()
