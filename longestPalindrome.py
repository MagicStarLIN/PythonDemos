# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
# 输入: "cbbd"
# 输出: "bb"

# 执行结果：通过
# 执行用时 :2436 ms, 在所有 python3 提交中击败了46.46%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了99.21%的用户

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

def manacher(s):
    if len(s) < 2:
        return s
    radiusStr = '#' + '#'.join(s) + '#'
    pArr = [0 for _ in range(len(radiusStr))]
    # 双指针，它们是一一对应的，须同时更新
    maxR = 0
    center = 0

    # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
    max_len = 1
    # 原始字符串的最长回文子串的起始位置，与 max_len 必须同时更新
    start = 1

    for i in range(len(radiusStr)):
        if i < maxR:
            mirror = 2 * center - i
            pArr[i] = min(pArr[mirror],maxR - i)

        left = i - (1 + pArr[i])
        right = i + (1 + pArr[i])

        while left >= 0 and right < len(radiusStr) and radiusStr[left] == radiusStr[right]:
            pArr[i] += 1
            left -= 1
            right += 1
        if i + pArr[i] > maxR:
            maxR = i + pArr[i]
            center = i
        
        if pArr[i] > max_len:
            max_len = pArr[i]
            start = (i - max_len) // 2

    return s[start : start + max_len]

print(manacher('abvbc'))