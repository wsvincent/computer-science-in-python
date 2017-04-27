def insertion_sort(input_list):
    """
    notes...

    Time Complexity: O(n^2) in the worst case
        - in worst case (list is sorted in descending order) "n" elements are checked and swapped for each selected element to get to the correct position

    Stable: Yes
        - logical ordering is maintained

    Memory: O(1)
        - sorts in place, original list re-used so no extra space

    Adaptivity: YES
        - if no swaps when adding an element to list, we can break out of comparing the rest of the elements

    Number of comparisons and swaps:
        - O(n^2) comparisons and O(n^2) swaps (more swaps than selection sort!)

    Notes:
        - low overhead and traditionally used with faster algrithms which follow a divide-and-conquer approach
        - why insertion sort over bubble sort?
            - bubble sort requires an additional pass over all elements to ensure the list is fully sorted
            - bubble sort must do "n" comparisons at every step. Insertion Sort can stop when the correct position in the sorted list is found
            - Bubble Sort performs poorly with modern hardware because the number of writes and swaps it performs results in cache misses so greater overhead than Insertion Sort
    """
    for i in range(len(input_list)):
        # start with "sorted list", look at next element, and count down
        # make sure not to include 0, b/c first element is always "sorted"
        for j in range(1, i + 1)[::-1]:
            if input_list[j] < input_list[j - 1]:
                input_list[j - 1], input_list[j] = input_list[j], input_list[j - 1]
            else:
                break

        return input_list
