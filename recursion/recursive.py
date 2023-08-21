from typing import Union


def count_down(high: int) -> None:
    if high < 0:
        return
    print(high)
    count_down(high - 1)


def find_max_num_in_array(arr: list) -> int:
    if not arr:
        return 0
    return max(arr[0], find_max_num_in_array(arr[1:]))


def array_count(arr: list) -> int:
    if not arr:
        return 0
    return 1 + array_count(arr[1:])


def array_sum(arr: list) -> int:
    if not arr:
        return 0
    return arr[0] + array_sum(arr[1:])


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
