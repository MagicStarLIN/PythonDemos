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
    

nums1 = [1,2]
nums2 = [3,4]

print(findMedianSortedArrays(nums1,nums2))

#TypeError: None is not valid value for the expected return type double
# Line 54 in _driver (Solution.py)
# Line 63 in <module> (Solution.py)
# During handling of the above exception, another exception occurred:
# TypeError: must be real number, not NoneType
# Line 18 in _serialize_float (./python3/__serializer__.py)
# Line 59 in _serialize (./python3/__serializer__.py)
# Line 52 in _driver (Solution.py)