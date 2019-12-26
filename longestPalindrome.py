def longestPalindrome(s):
    if len(s) < 2:
        return s

    radiusStr = '#' + '#'.join(s) + '#'
    maxFlag = 0
    for i in range(len(radiusStr)):
        left = i - 1
        right = i + 1
        r = 0
        while left >= 0 and right < len(radiusStr) and radiusStr[left] == radiusStr[right]:
            r += 1
            left -= 1
            right += 1
        
        if r > maxFlag:
            maxFlag = r
            start = (i - r) // 2
    return s[start : start + maxFlag]


print(longestPalindrome('babad'))
