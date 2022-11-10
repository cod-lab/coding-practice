# HARD

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6

# def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
# def method1(nums1: List[int], nums2: List[int]) -> float:
def method1(nums1: list[int], nums2: list[int]) -> float:       # naive approach
    print(nums1,nums2)

    nums3 = sorted(nums1 + nums2)
    l = len(nums3)
    mp = (l // 2)
    print(nums3,l,mp)

    median = nums3[mp] if l % 2 else (nums3[mp-1] + nums3[mp]) / 2

    return median


def method2(l1: list[int], l2: list[int]) -> float:             # little efficient self made approach
    # l = (len(l1) + len(l2)) // 2
    # l = l // 2 if l % 2 else (l // 2) + 1

    l = len(l1) + len(l2)
    mid = (l // 2) + 1
    print(l,mid)

    # i=j=0
    i,j=len(l1),len(l2)
    x=y=0
    while mid and i and j:                    # sorting & finding mid point
        print(len(l1)-i,len(l2)-j)
        x = y
        # if l1[i] < l2[j]:
        if l1[-i] < l2[-j]:
            # x = y
            y = l1[-i]
            # i += 1
            i -= 1
            # if l-1: i += 1
        else:
            # x = y
            y = l2[-j]
            # j += 1
            j -= 1
            # if l-1: j += 1
        # x = min(l1[i], l2[j])

        # i += 1
        # j += 1
        mid -= 1
        # print(i,j,l,x,l1[i-1],l2[j-1],l1[i],l2[j])
        # print(i,j,l,x,l1[i],l2[j])

    print(mid,x,y,i,j)

    if mid == 1:
        x = y
        y = l1[-i] if i else l2[-j]
    if mid > 1:
        x = l1[-i+mid-2] if i else l2[-j+mid-2]
        y = l1[-i+mid-1] if i else l2[-j+mid-1]
        # y = l1[-i+mid] if i else l2[-j+mid]

    print(x,y)
    median = y if l % 2 else (x+y) / 2
    return median


def method3(nums1: list[int], nums2: list[int]) -> float:             # little efficient self made approach
    n = len(nums1)
    m = len(nums2)

    # n = m if n > m else n               # alwaz smaller array
    # m = len(nums1) if n == m else m     # alwaz larger array

    if n>m: method3(nums2, nums1)

    l,h=0,n

    while l<=h:         # binary searching
        # print(h-l)
        cut1 = (l+h)//2      # array1 cut
        cut2 = ((n + m + 1)//2) - cut1      # array2 cut

        l1 = nums1[cut1-1] if cut1 else -1
        r1 = nums1[cut1] if cut1 != n else -1
        # r1 = nums1[cut1] if cut1 < n else -1
        l2 = nums2[cut2-1] if cut2 else -1
        r2 = nums2[cut2] if cut2 != m else -1
        # r2 = nums2[cut2] if cut2 < m else -1

        if l1<=r2 and l2<=r1:
            x = max(l1,l2)
            if (n+m)%2: return x
            return (x + min(r1,r2))/2

        if l1 > r2: high = cut1 - 1          # so moving partition line left
        else: low = cut2 + 1          # so moving partition line right

    return 0



lists = [[[1,3],[2]]]
lists += [[[1,2],[3,4]]]
lists += [[[0,0],[0,0]]]
lists += [[[1,3],[2,4]]]
lists += [[[2,8,15,18],[5,9,12,17]]]
lists += [[[1, 3, 5, 7],[2, 4, 6, 8]]]
lists += [[[1, 5, 8, 10],[6, 7, 9, 11]]]
lists += [[[1,2,3],[4,5,6,7,8,9,10]]]

for l in lists:
    print(l)
    # print(l,method2(*l),'\n')
    print(method3(*l),'\n')

