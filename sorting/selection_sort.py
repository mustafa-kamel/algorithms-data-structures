import random


def find_smallest_item(unsorted_list: list) -> int:
    smallest_index = 0
    smallest = unsorted_list[smallest_index]
    for i in range(1, len(unsorted_list)):
        if unsorted_list[i] < smallest:
            smallest = unsorted_list[i]
            smallest_index = i

    return smallest_index


def selection_sort(unsorted_list: list) -> list:
    new_l = []
    while len(unsorted_list) > 0:
        index = find_smallest_item(unsorted_list)
        new_l.append(unsorted_list.pop(index))

    return new_l
