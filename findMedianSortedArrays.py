# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 你可以假设 nums1 和 nums2 不会同时为空。
# 示例 1:
# nums1 = [1, 3]
# nums2 = [2]
# 则中位数是 2.0
# 示例 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# 则中位数是 (2 + 3)/2 = 2.5


# 执行结果：通过
# 执行用时 :92 ms, 在所有 python3 提交中击败了99.61%的用户
# 内存消耗 :12.8 MB, 在所有 python3 提交中击败了99.43%的用户


def findKthElm(nums1,nums2,k):
    min_int = -9223372036854775807
    assert (1 <= k and k <= len(nums1) + len(nums2))
    left = max(0,k-len(nums2))
    right = min(len(nums1),k)
    while right > left:
        mid = left + (right - left) // 2
        if nums2[k - mid - 1] > nums1[mid]:
            left = mid + 1 
        else:
            right = mid

    nums1leftMax = min_int if (left == 0) else nums1[left - 1]
    nums2leftMax = min_int if (left == k) else nums2[k - left - 1]

    return max(nums1leftMax,nums2leftMax)


def findMedianSortedArrays (nums1 , nums2) :
    n = len(nums1) + len(nums2)
    if n&1 :
        return float(findKthElm(nums1,nums2,(n>>1)+1))
    else:
        return float((findKthElm(nums1,nums2,n>>1)+findKthElm(nums1,nums2,(n>>1)+1))/2)