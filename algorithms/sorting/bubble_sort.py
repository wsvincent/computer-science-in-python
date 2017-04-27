def bubble_sort(input_list):
    """
    Often the most inefficient sorting method except edge case of a "short bubble".

    Each iteration, every element is compared with its neighbor and swapped if not in the correct order.

    The smallest elements 'bubble' to the beginning of the list.

    Time Complexity: O(n^2) in worst case
        - in worst case (list is sorted in descending order) "n" elements are checked and swapped for each selected element

    Stable: YES
        - logical ordering is maintained

    Memory: O(1)
        - sorts in place, original list re-used so no extra space

    Adaptivity: YES
        - if there were no swaps on an iteration, we know the list is already sorted and can break out early (known as "short bubble")

    Notes:
        - O(n^2) == terrible, OMFG
        - advantage over selection sort: adaptivity
    """
    for i in range(len(input_list)):
        swapped = False
        # i represents the last position in list that is sorted
        for j in range(len(input_list) - 1, i, -1):
            if input_list[j] < input_list[j - 1]:
                input_list[j - 1], input_list[j] = input_list[j], input_list[j - 1]
                swapped = True
        # if no swaps, list already sorted so we can break out
        if not swapped:
            break
        return input_list
