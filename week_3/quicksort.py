from typing import List


def swap(values: List[int], index_a: int, index_b: int) -> List[int]:
    values[index_a], values[index_b] = values[index_b], values[index_a]
    return values


def get_median_index(numbers: List[int]) -> int:
    first_index = 0
    last_index = len(numbers) - 1

    if len(numbers) % 2 == 0:
        middle_index = int((len(numbers) / 2) - 1)
    else:
        middle_index = int(len(numbers)/2)

    hashed = {
        numbers[first_index]: first_index,
        numbers[middle_index]: middle_index,
        numbers[last_index]: last_index
    }

    sorted_values = sorted(list(hashed.keys()))
    return hashed[sorted_values[1]]


def quicksort(numbers: List[int]):
    global count
    global strategy

    if len(numbers) < 2:
        return numbers

    if strategy == 'last':
        numbers = swap(numbers, 0, len(numbers)-1)
    elif strategy == 'median':
        median_index = get_median_index(numbers)
        numbers = swap(numbers, 0, median_index)

    count = count + len(numbers) - 1
    pivot_index = 0
    pivot_value = numbers[pivot_index]
    i = pivot_index + 1

    for j in range(pivot_index + 1, len(numbers)):
        if numbers[j] < pivot_value:
            numbers = swap(numbers, j, i)
            i = i + 1
    
    new_pivot_index = i-1
    numbers = swap(numbers, new_pivot_index, pivot_index)
    left = quicksort(numbers[0:new_pivot_index])
    right = quicksort(numbers[new_pivot_index+1:])
    return left + [pivot_value] + right

with open('data/numbers.txt', 'r') as f:
    numbers = f.read().splitlines()

count = 0
strategy = 'median' # | last

numbers = [int(n) for n in numbers]
numbers = quicksort(numbers)