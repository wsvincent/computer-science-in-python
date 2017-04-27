def quick_sort(input_list):
    """
    The default sorting algo in many standard libraries due to its speed.

    A divide-and-conquer algorithm. The difference between Merge Sort and Quick Sort is the partition is not based on length or an artificial index, but on a 'pivot'.

    A pivot is an element from the list. The list is partitioned with all elements smaller than the pivot on one side and larger than the pivot on the other.

    The pivot is appleid to all sub-lists until the list is sorted.

    Which pivot to use?

    Time Complexity: O(n log N) on average
        - O(n^2) in worst case

    Stable: NO
        - does not preserve relevant ordering

    Memory: O(log n)
        - call stack in recursion

    Adaptivity: NO
        - no way to know whether list is already sorted before iterations are done

    Notes:
        - usually preferable to Merge sort, better cache performance
    """
    def partition(list_to_sort, start, end):
        pivot = list_to_sort[start]
        left = start
        right = end

        # determine where pivot should go
        while left < right:
            while list_to_sort[left] <= pivot and left < right:
                left += 1
            while list_to_sort[right] > pivot:
                right -= 1
            if left < right:
                # move items around if they are in wrong position relative to pivot
                list_to_sort[left], list_to_sort[right] = list_to_sort[right], list_to_sort[left]

        # finally put pivot in correct spot
        list_to_sort[start], list_to_sort[right] = list_to_sort[right], list_to_sort[start]

        return right

    def quick_sort_helper(list_to_sort, start, end):
        # if segment has only one element, return
        # also takes care of possibility for invalid input
        if start < end:
            partition_index = partition(list_to_sort, start, end)
            quick_sort_helper(list_to_sort, start, partition_index - 1)
            quick_sort_helper(list_to_sort, partition_index + 1, end)

    quick_sort_helper(input_list, 0, len(input_list) - 1)
    return input_list
