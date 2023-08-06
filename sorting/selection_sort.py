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


def test_sorted_list():
    sorted_list = [1, 2, 3, 4, 8, 54]
    print("----------------------------")
    print("")
    print("test_sorted_list")
    sorted_list2 = selection_sort(sorted_list.copy())
    if sorted_list == sorted(sorted_list2):
        print("success")
    else:
        print("failed")
        print(sorted_list, "!=", sorted_list2)
    print("")


def test_unsorted_list1():
    unsorted_list = [5, 8, 3, 2, 9, 1, 4, 7, 55]
    print("----------------------------")
    print("")
    print("test_unsorted_list1")
    sorted_list = selection_sort(unsorted_list.copy())
    if sorted_list == sorted(unsorted_list):
        print("success")
    else:
        print("failed")
        print(sorted_list, "!=", sorted(unsorted_list))
    print("")


def test_unsorted_list2():
    unsorted_list = [6, 8, 4, 99, 11, 0, 3, 2, 14]
    sorted_list = selection_sort(unsorted_list.copy())
    print("----------------------------")
    print("")
    print("test_unsorted_list2")
    if sorted_list == sorted(unsorted_list):
        print("success")
    else:
        print("failed")
        print(sorted_list, "!=", sorted(unsorted_list))
    print("")


def test_unsorted_list3():
    unsorted_list = [random.randint(i, i * 999) for i in range(1, 999)]
    sorted_list = selection_sort(unsorted_list.copy())
    print("----------------------------")
    print("")
    print("test_unsorted_list3")
    if sorted_list == sorted(unsorted_list):
        print("success")
    else:
        print("failed")
        print(sorted_list, "!=", sorted(sorted_list))
    print("")


test_sorted_list()
test_unsorted_list1()
test_unsorted_list2()
test_unsorted_list3()
