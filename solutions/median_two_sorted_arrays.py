
def findMedianSortedArray(nums1: list[int], nums2: list[int]) -> float:
    # Always perform binary search on the smaller array.
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m = len(nums1)
    n = len(nums2)

    left = 0
    right = m

    while left <= right:
        # Find partition positions.
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1

        # Find the four boundary values.
        max_left1 = (
            nums1[partition1 - 1]
            if partition1 > 0
            else float("-inf")
        )
        min_right1 = (
            nums1[partition1]
            if partition1 < m
            else float("inf")
        )

        max_left2 = (
            nums2[partition2 - 1]
            if partition2 > 0
            else float("-inf")
        )
        min_right2 = (
            nums2[partition2]
            if partition2 < n
            else float("inf")
        )

        # Check whether the partition is correct.
        if max_left1 <= min_right2 and max_left2 <= min_right1:

            # Even number of elements.
            if (m + n) % 2 == 0:
                return (
                    max(max_left1, max_left2)
                    + min(min_right1, min_right2)
                ) / 2

            # Odd number of elements.
            return float(max(max_left1, max_left2))

        # Move the partition in nums1 to the left.
        elif max_left1 > min_right2:
            right = partition1 - 1

        # Move the partition in nums1 to the right.
        else:
            left = partition1 + 1

    raise ValueError("Input arrays must not both be empty")


# Manual tests
#print(findMedianSortedArray([1, 3], [2]))           # 2.0
#print(findMedianSortedArray([1, 2], [3, 4]))        # 2.5
#print(findMedianSortedArray([1, 4, 7], [2, 3, 8])) # 5.5

