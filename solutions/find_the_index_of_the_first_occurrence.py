def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1


# Manual test
haystack = "sadbutsad"
needle = "sad"

print("First occurrence index:", strStr(haystack, needle))