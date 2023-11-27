def max_subarray_sum(arr):
    """
    Finds the contiguous subarray with the largest sum in the given array.

    Parameters:
    - `arr`: A list of integers.

    Returns:
    - If the array is not empty, returns a string with the maximum subarray sum.
    - If the array is empty, returns "The given array is empty".
    """
    if not arr:
        return "The given array is empty"
    local_maximum = arr[0]
    max_sum = arr[0]
    
    for number in arr[1:]:
        if number > local_maximum + number:
            local_maximum = number
        else:
            local_maximum += number
        max_sum = max(max_sum, local_maximum)
    return f"The maximum subarray sum is {max_sum}"