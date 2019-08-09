def flatten_list(lst):
    """
        Flattens a list of arbitrarily nested lists of integers and returns a flat list of integers.
    """

    flat_list = []

    for item in lst:
        if type(item) == list:
            flat_list += flatten_list(item)
        else:
            flat_list.append(item)

    return flat_list