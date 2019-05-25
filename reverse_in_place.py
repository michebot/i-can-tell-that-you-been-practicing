def reverse_list_in_place(lst):

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

print(reverse_list_in_place([1, 2, 3,]))
print(reverse_list_in_place([1, 2, 3, 4,]))