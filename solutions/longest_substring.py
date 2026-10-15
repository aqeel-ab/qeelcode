def lenLongestSubstr(s:str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left]) #remove the leftmost character from the set if duplicate is found
            left += 1

        seen.add(s[right])
        max_len = max(max_len,right-left+1)
    return max_len



