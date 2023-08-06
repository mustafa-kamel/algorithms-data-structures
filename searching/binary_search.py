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


def test_binary_search():
    lookup = 2
    search_list = list(range(1, 9999))
    index = binary_search(lookup, search_list)
    if index and search_list[index] == lookup:
        print(f"Found {lookup} at index {index} ({search_list[index]})")
    else:
        print("Item not found.")


test_binary_search()


def test_beginning_needle():
    lookup = 1
    search_list = list(range(1, 10000))
    index = binary_search(lookup, search_list)
    assert index == 0


test_beginning_needle()
