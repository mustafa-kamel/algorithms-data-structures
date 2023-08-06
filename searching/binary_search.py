from typing import Union


def binary_search(needle: int, haystack: Union[tuple, list, set]) -> Union[int, None]:
    low = 0
    high = len(haystack)
    i = 0
    while low < high:
        mid = (low + high) // 2
        print(f"Low: {low}, High: {high}, Mid: {mid}.")
        if haystack[mid] == needle:
            print(f"Found at index {mid} in {i} iterations.")
            return mid
        if haystack[mid] > needle:
            print("In smaller list.")
            high = mid
        else:
            print("In bigger list.")
            low = mid + 1
        i += 1

    print("Not found.")
    return None
