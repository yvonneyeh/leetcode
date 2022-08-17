def characterReplacement(s: str, k: int) -> int:
    # start = 0
    # max_char_count = 0
    # max_length = 0
    # frequency_map = {}
    #
    # for end in range(len(s)):
    #     right_char = s[end]
    #     if right_char not in frequency_map:
    #         frequency_map[right_char] = 1
    #     frequency_map[right_char] += 1
    #     max_char_count = max(max_char_count, frequency_map[right_char])
    #
    #     if (end - start - max_char_count + 1 ) > k:
    #         left_char = s[start]
    #         frequency_map[left_char] -= 1
    #         start += 1
    #
    #     max_length = max(max_length, end - start + 1)
    #
    # return max_length

    # INCORRECT ^

    # window_start, max_length, max_repeat_letter_count = 0, 0, 0
    # frequency_map = {}
    #
    # for window_end in range(len(s)):
    #     right_char = s[window_end]
    #
    #     if right_char not in frequency_map:
    #         frequency_map[right_char] = 0
    #
    #     frequency_map[right_char] += 1
    #
    #     max_repeat_letter_count = max(
    #         max_repeat_letter_count, frequency_map[right_char])
    #
    #     if (window_end - window_start + 1 - max_repeat_letter_count) > k:
    #         left_char = s[window_start]
    #         frequency_map[left_char] -= 1
    #         window_start += 1
    #
    #     max_length = max(max_length, window_end - window_start + 1)
    #
    # return max_length

    # ^ PASSES

    frequency = {}
    window = 0

    for i, char in enumerate(s):
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1
        if window + 1 - max(frequency.values()) <= k:
            window += 1
        else:
            left_char = s[i-window]
            frequency[left_char] -= 1

    return window

    #     d[char] = d.get(char, 0) + 1
    #    is equivalent to
    #
    # if char not in hash:
    #       hash[char] = 1
    # else:
    #       hash[char] += 1

    #
    # frequency = {}
    # window = 0
    #
    # for i, char in enumerate(s):
    #
    #     frequency[char] = frequency.get(char, 0) + 1
    #     if window+1 - max(frequency.values()) <= k:
    #         window += 1
    #     else:
    #         frequency[s[i-window]] -= 1
    #
    # return window

print("ABAB", 2, "-> 4 :", characterReplacement("ABAB", 2))
print("AABABBA", 1, "-> 4:", characterReplacement("AABABBA", 1))
