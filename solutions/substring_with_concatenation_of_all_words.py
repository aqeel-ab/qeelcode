from collections import Counter


def findSubstring(s: str, words: list[str]) -> list[int]:
    if not s or not words:
        return []

    word_length = len(words[0])
    word_count = len(words)
    total_length = word_length * word_count

    if len(s) < total_length:
        return []

    word_frequency = Counter(words)
    result = []

    for offset in range(word_length):
        left = offset
        seen = Counter()
        count = 0

        for right in range(offset, len(s) - word_length + 1, word_length):
            word = s[right:right + word_length]

            if word not in word_frequency:
                seen.clear()
                count = 0
                left = right + word_length
                continue

            seen[word] += 1
            count += 1

            while seen[word] > word_frequency[word]:
                left_word = s[left:left + word_length]
                seen[left_word] -= 1
                count -= 1
                left += word_length

            if count == word_count:
                result.append(left)

                left_word = s[left:left + word_length]
                seen[left_word] -= 1
                count -= 1
                left += word_length

    return sorted(result)


# Manual test
s = "barfoothefoobarman"
words = ["foo", "bar"]

print("Starting indices:", findSubstring(s, words))