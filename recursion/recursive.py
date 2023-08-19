from typing import Union


def count_down(high: int) -> None:
    if high < 0:
        return
    print(high)
    count_down(high - 1)


def find_max_num_in_array(arr: list) -> int:
    if not arr:
        return 0
    return max(arr.pop(), find_max_num_in_array(arr))


def array_count(arr: list) -> int:
    count = 0
    if not arr:
        return 0
    arr.pop()
    count += 1
    return count + array_count(arr)


def array_sum(arr: list) -> int:
    if not arr:
        return 0
    return arr.pop() + array_sum(arr)


def binary_search(needle: int, haystack: Union[tuple, list, set]) -> Union[int, None]:
    if not haystack:
        return None
    mid_index = len(haystack) // 2
    mid = haystack[mid_index]
    if needle == mid:
        return mid_index
    elif needle < mid:
        haystack = haystack[0:mid_index]
    else:
        mid_index += 1
        haystack = haystack[mid_index:]

    return binary_search(needle, haystack)
