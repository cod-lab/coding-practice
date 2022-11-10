# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Constraints:

# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

# naive approach - brute force
# TC - O(n^2), SC - O(1)
def method1(n: list[int], t: int) -> list[int]:         # not completed
    l = len(n)
    m = n[l//2]

    i,j=1,l-1
    k = 0
    t2 = t-n[k]

    while t2 != n[-2]:
        while i<=j:
            if n[i] == t2 or n[j] == t2:
                return [i+1, j+1]
            elif n[i] < t2:
                i += 1
            elif n[j] > t2:
                j -= 1
        k += 1
        t2 = t-n[k]


# advanced approach
# TC - O(n), SC - O(1)
def method2(n: list[int], t: int) -> list[int]:
    i,j = 0,len(n)-1
    s = n[i] + n[j]

    while i<j:
            # if t == s:
            #     return [i+1,j+1]

            if t > s:
                # while n[i] == n[i+1]:
                # while n[i-1] == n[i]:
                while 1:
                    # print('i',i)
                    i += 1
                    if n[i-1] != n[i]: break
            elif t < s:
                # while n[j] == n[j-1]:
                # while n[j+1] == n[j]:
                while 1:
                    # print('j',j)
                    j -= 1
                    if n[j+1] != n[j]: break
            else: return [i+1,j+1]

            s = n[i] + n[j]



lists = [[[2,7,11,15],9]]
lists += [[[2,3,4],6]]
lists += [[[-1,0],-1]]
lists += [[[0,2,2,9,12,13,14,15,15,15],9]]
lists += [[[0,0,0,1,1,2,9,9,9,11,12,15,15,15],14]]

for l in lists:
    print(*l,'\n',method2(*l),'\n')

# test cases
# [[2,7,11,15],9]
# [[2,3,4],6]
# [[-1,0],-1]
# [[0,2,2,9,12,13,14,15,15,15],9]
# [[0,0,0,1,1,2,9,9,9,11,12,15,15,15],14]


