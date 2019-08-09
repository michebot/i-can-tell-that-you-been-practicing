def contains_all_items(list1, list2):
    
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
