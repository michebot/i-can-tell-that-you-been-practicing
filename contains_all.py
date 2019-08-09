import collections
import pytest


# Implement the contains_all function
# The contains_all function accepts arguments list1 and list2
# It should return True if all elements in list1 are included in list2, otherwise return False
def contains_all(list1, list2):
    
    if type(list1) == int:
        list1 = [list1]
    if type(list2) == int:
        list2 = [list2]
    elif list1 == [] or list2 == []:
        return True
    elif list1 == list2:
        return True

    list1_dict = dict()
    list2_dict = dict()
    
    for item in list1:
        list1_dict[item] = list1_dict.get(item, 0) + 1
    for item in list2:
        list2_dict[item] = list2_dict.get(item, 0) + 1
        
    for item in list1_dict:
        if item not in list2_dict:
            return False
        elif item in list2_dict:
            if list1_dict[item] > list2_dict[item]:
                return False
    return True
            
    


def run_test(list1, list2, expected_result):
    result = contains_all(list1, list2)
    assert expected_result == result


# With perfect input


def test_it_should_return_true_for_an_empty_set_of_list1():
    list1 = []
    list2 = ['a', 'b', 'c']
    run_test(list1, list2, True)


def test_it_should_return_true_if_all_list1_are_in_list2():
    list1 = ['a']
    list2 = ['a']
    run_test(list1, list2, True)


def test_it_should_return_false_if_not_all_list1_are_in_list2():
    list1 = ['a']
    list2 = ['b']
    run_test(list1, list2, False)


def test_it_should_return_true_if_list1_are_in_a_different_order_but_are_all_present_in_list2():
    list1 = ['a', 'b', 'c']
    list2 = ['b', 'a', 'c']
    run_test(list1, list2, True)


def test_it_should_return_false_if_list2_does_not_have_all_values_from_the_input():
    list1 = ['a', 'b', 'c']
    list2 = ['a', 'b']
    run_test(list1, list2, False)


def test_it_should_return_true_if_list2_contains_extra_values():
    list1 = ['a', 'b', 'c']
    list2 = ['b', 'q', 'r', 'n', 'a', 'c']
    run_test(list1, list2, True)


def test_it_should_return_false_if_list2_is_missing_one_element():
    list1 = ['a', 'b', 'c']
    list2 = ['q', 'r', 'n', 'a', 'c']
    run_test(list1, list2, False)


def test_it_should_return_false_if_not_all_individual_list1_are_represented_in_list2():
    list1 = ['a', 'a', 'b', 'c']
    list2 = ['b', 'q', 'r', 'n', 'a', 'c']
    run_test(list1, list2, False)


def test_it_should_return_true_if_list2_contains_more_of_the_same_element():
    list1 = ['a', 'a', 'b', 'c']
    list2 = ['b', 'a', 'a', 'a', 'c']
    run_test(list1, list2, True)


# With incorrect user input


def test_it_should_return_true_for_a_null_set():
    list1 = None
    list2 = []
    run_test(list1, list2, True)


def test_it_should_return_true_if_list2_is_null_but_list1_are_empty():
    list1 = []
    list2 = None
    run_test(list1, list2, True)


def test_it_should_return_true_if_they_are_both_null():
    list1 = None
    list2 = None
    run_test(list1, list2, True)


def test_it_should_handle_values_as_if_they_were_lists():
    list1 = 0
    list2 = 0
    run_test(list1, list2, True)
    
    list1 = 0
    list2 = [0]
    run_test(list1, list2, True)

    list1 = 1
    run_test(list1, list2, False)


pytest.main()
