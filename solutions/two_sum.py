def two_sum(nums, target):

    # Return the indices of two numbers that add up to target.

    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []