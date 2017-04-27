def binary_search(list, item):
    """
    A very efficient search algorithm for ordered list.

    Instead of searching the list in sequence, binary_search compares the middle element in the list to our target item. If a match, the position in our list is returned. If not, we can take advantage of our ordered list to eliminate either the upper or lower half of the remaining items and continue.


    Time Complexity: O(log n) in worst case


    Notes:
        - hard to beat for ordered lists
        - sorting can be expensive
        - for small values, worth vs sequential search?
    """
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None
