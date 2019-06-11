import unittest


def reverse(lst):

    # initializing pointers
    left_idx = 0
    right_idx = len(lst) - 1

    # condition for loop
    while left_idx < right_idx:
        # swapping characters

        # option 1
        # temp = lst[left_idx]
        # lst[left_idx] = lst[right_idx]
        # lst[right_idx] = temp

        # option 2
        lst[left_idx], lst[right_idx] = \
            lst[right_idx], lst[left_idx]

        # updating pointers to move towards middle
        left_idx += 1
        right_idx -= 1

    return lst

# print(reverse([1, 2, 3,]))
# print(reverse([1, 2, 3, 4,]))

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)