def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0
    cur_length = 0
    lookup = []
    if len(s) == 0:
        return 0
    for i, item in enumerate(s):
        if item not in lookup:
            lookup.append(item)
            cur_length += 1
        else:
            index = lookup.index(item)
            lookup = lookup[index + 1:]
            lookup.append(item)
            cur_length = len(lookup)
        if cur_length > max_length:
            max_length = cur_length
    return max_length
