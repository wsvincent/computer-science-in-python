def shell_sort(input_list):
    """
    Shell Short improves on Insertion Sort by breaking the original list into sub-lists made of elements separated by an 'increment'. These sub-lists are then sorted by Insertion Sort.

    If increment is 2, then sublist is 2, 4, 6, etc.

    Each sub-list is then sorted using insertion sort.

    Increment is slowly reduced until it's 1.

    The advantage is you are eventually applying insertion sort to a nearly sorted list, which is very efficient.

    Complexity: between O(n) and O(n^2)

    Memory: O(1) extra space, since sort in place

    Notes:
        - getting the exact complexity of Shell Sort is difficult b/c it depends on the increment value chosen
        - it is also not clear what the best increment value is
        - bottom line: complexity is better than insertion sort as the final iteration with increment = 1 works with a nearly sorted list
        - example of adaptive algorithm since based on Insertion Sort
