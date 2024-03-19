from typing import List


def count_inversions(integers: List[int]):
    if len(integers) <= 1:
        return integers, 0
    
    divide_index = int(len(integers) / 2) 
    left_side, left_inverted = count_inversions(integers[:divide_index])  
    right_side, right_inverted = count_inversions(integers[divide_index:])
    to_merge_count = len(left_side) + len(right_side)
    inverted_count = (left_inverted + right_inverted)
    merged = []
    index_left, index_right = 0, 0

    while len(merged) < to_merge_count:
        left_remains = len(left_side) - index_left
        right_remains = len(right_side) - index_right

        if left_remains == 0:
            merged.extend(right_side[index_right:])
        elif right_remains == 0:
            merged.extend(left_side[index_left:])
        elif right_side[index_right] < left_side[index_left]:
            merged.append(right_side[index_right])
            inverted_count += left_remains
            index_right += 1
        else:
            merged.append(left_side[index_left])
            index_left += 1

    return merged, inverted_count


with open('data/numbers.txt', 'r') as f:
    numbers = f.read().splitlines()

integers = [int(n) for n in numbers]
print(count_inversions(integers))

