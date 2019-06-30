def lines(a, b):
    """Return lines in both a and b"""
    # Split strings into lists
    list1 = a.split('\n')
    list2 = b.split('\n')

    # Remove duplicates from both lists and find the common elements
    list_of_common_elements = list(set(list1) & set(list2))
    return list_of_common_elements


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    return []


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    return []
