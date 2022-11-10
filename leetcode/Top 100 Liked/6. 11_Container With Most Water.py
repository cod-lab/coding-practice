# Medium

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:

# Input: height = [1,1]
# Output: 1

# Constraints:

# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

# naive approach - brute force
# TC - O(n^2), SC - O(1)
def method1(height: list[int]) -> int:          # not completed

        for i in range(len(height)):
            for j in range(len(height)):
                if i != j:
                    x=height[i]
                    y=height[j]
                    area = (i-j) * min(x,y)
                    print(i,j,x,y,area)


# advanced approach
# TC - O(n), SC - O(1)
def method2(h: list[int]) -> int:
    l,r = 0,len(h)-1
    x,y = h[0],h[r]
    maxArea = r * min(x,y)

    # print('area',maxArea)

    while l < r:
        if x < y:
            l += 1
            x = h[l]
        # elif y < x:
        else:
            r -= 1
            y = h[r]
        # else:
        #     l += 1
        #     r -= 1

        maxArea = max(maxArea, (r-l) * min(x,y))

        # print(l,r,x,y,maxArea)
    return maxArea


lists = [[1,8,6,2,5,4,8,3,7]]
lists += [[1,1]]

for l in lists:
    print(l,'\n',method2(l),'\n')



