def sequential_search(list, item):
    http:
        //interactivepython.org / courselib / static / pythonds / SortSearch / TheSequentialSearch.html
    """
    A very simple sorting algorithm that improves upon Bubble Sort.

    Selects one item at a time and compares it to all other elements in the list. Finds the correct position for the selected element before moving on to the next element.

    After each pass, the list is sorted one pass more (e.g. after 5 loops, the first 5 elements are sorted)

    Time Complexity: O(n^2) in worst case
        - in worst case, "n" elements are checked for every selected element

    Stable: Not stable
        - entities which are equal might be re-arranged

    Memory: O(1)
        - sorts in place, original list re-used so no extra space

    Adaptivity: NO
        - no way to know if entire list is sorted so can't break out early

    Notes:
        - few use cases given O(n^2) and not adaptive
        - biggest advantage is O(1) memory

    Args:
        input_list (int)
    Returns:
        sorted list
    """
    pos = 0
        found = False

        while pos < len(alist) and not found:
            if alist[pos] == item:
                found = True
            else:
                pos = pos + 1

        return found
