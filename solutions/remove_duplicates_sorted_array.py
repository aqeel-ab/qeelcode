def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1

    return k


# Manual test
nums = [1, 1, 2]

k = removeDuplicates(nums)

print("Number of unique elements:", k)
print("Modified array:", nums[:k])