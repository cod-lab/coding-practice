# Medium

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Constraints:

# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

# naive approach - brute force
# TC - O(n^3), SC - O(1)
# def method1(a: list[int]) -> list[list[int]]:
#     for i in range(len(a)-2):
#        for j in range(1,len(a)-1):
#             for k in range(len(a)):


# advanced approach - using two sum (after sorting array) method
# TC - O(n^2), SC - O(1)
def method2(n: list[int]) -> list[list[int]]:
    # l=len(n)-1
    # if l<2: return []         # n always has at least 3 elements

    n.sort()
    print(n)

    # if n[0] > 0 or n[l] < 0: return []
    if n[0] > 0 or n[-1] < 0: return []

    # array starting from 0 i.e., NO -ves
    if n[0] == 0:
    # if not n[0]:
        # if n.count(0) >= 3: return [[0,0,0]]
        # if n[0]==n[1]==n[2]: return [[0,0,0]]
        if n[1]==n[2]==0: return [[0,0,0]]
        return []

    # array ending at 0 i.e., NO +ves
    # if n[l] == 0:
    if n[-1] == 0:
    # if not n[-1]:
        # if n[l]==n[l-1]==n[l-2]: return [[0,0,0]]
        # if n[-1]==n[-2]==n[-3]: return [[0,0,0]]
        if n[-2]==n[-3]==0: return [[0,0,0]]
        return []

    l = len(n)-1
    op = []
    k = 0

    # for k in range(l-1):
    while k != l-1:
        i,j = k+1,l
        t = -n[k]
        # s = n[i] + n[j]

        while i<j:
            s = n[i] + n[j]
            # print(i,j,s)

            if s < t:
                i += 1
                # while i<j:
                #     i += 1
                #     if n[i-1] != n[i]: break
            elif s > t:
                j -= 1
                # while i<j:
                #     j -= 1
                #     if n[j+1] != n[j]: break
            else:
                op += [[-t,n[i],n[j]]]
                # op.append([-t,n[i],n[j]])
                # op.extend([[-t,n[i],n[j]]])
                # while i<j:
                #     i += 1
                #     if n[i-1] != n[i]: break
                # while i<j:
                #     j -= 1
                #     if n[j+1] != n[j]: break

                # i += 1
                # j -= 1

                while i<j:
                    i,j = i+1,j-1
                    if n[i-1] != n[i] or n[j+1] != n[j]: break

            # s = n[i] + n[j]

            # while 1:
            #     k += 1
            #     if n[k-1] != n[k]: break

        # while n[k] == n[k+1]:
        #     k += 1
        # if n[k] >= 0: break
        # print('->',k,-t,op)
        # if -t > 0: return op

        # if t == 0:
        # if not t:
            # if n[k]==n[k+1]==n[k+2]:
            #     return op + [[0,0,0]]
            # return op
            # return op + [[0,0,0]] if n[k]==n[k+1]==n[k+2] else op
            # return op + [[0,0,0]] if n[k+1]==n[k+2]==0 else op
            # return op

        # print(-t,'op',op)
        # if -t > 0: return op

        if t == 0 or -t > 0:
            return op

        while 1:
            k += 1
            if n[k-1] != n[k]: break

    return op


# advanced approach - using two sum (after sorting array) method (just like method2 with little diff)
# TC - O(n^2), SC - O(1)
def method3(n: list[int]) -> list[list[int]]:
    n.sort()
    # print(n)

    if n[0] > 0 or n[-1] < 0: return []

    if n[0] == 0:                                       # array starting from 0 i.e., NO -ves
        if n[1]==n[2]==0: return [[0,0,0]]
        return []

    if n[-1] == 0:                                      # array ending at 0 i.e., NO +ves
        if n[-2]==n[-3]==0: return [[0,0,0]]
        return []

    # l = len(n)-1
    l = len(n)
    # l = -len(n) + 2
    op = []

    # while l:
    while l-2:
    # while l+2:
        # i,j = -l,l
        i,j = -l+1,-1
        # i,j = l+1,-1
        # i,j = l-1,-1

        # t = -n[i-1]
        t = -n[-l]
        # t = -n[l]
        # t = -n[l-2]

        # print(l,i,j,t)

        while i<j:
            s = n[i] + n[j]
            # print(l,i,j,t,s)

            if s < t: i += 1
            elif s > t: j -= 1
            else:
                op += [[-t,n[i],n[j]]]

                while i<j:
                    i,j = i+1,j-1
                    if n[i-1] != n[i] or n[j+1] != n[j]:
                        break
                    # print('mid while',i,j)

        if t == 0 or -t > 0:
            return op

        while 1:
        # while l:
            l -= 1
            # l += 1

            # print('last while',l,'\n')

            # if n[l-1] != n[l]: break
            if n[-l-1] != n[-l]: break
            # if n[l-1] != n[l-2]: break

            # print('last while',l)

    return op


# fastest of all
# advanced approach - using two sum (after sorting array) method (just like method3 with little diff)
# TC - O(n^2), SC - O(1)
def method4(n: list[int]) -> list[list[int]]:
    n.sort()

    if n[0] > 0 or n[-1] < 0: return []

    if n[0] == 0:                                       # array starting from 0 i.e., NO -ves
        if n[1]==n[2]==0: return [[0,0,0]]
        # if not n[1]|n[2]: return [[0,0,0]]            # this is also right
        return []

    if n[-1] == 0:                                      # array ending at 0 i.e., NO +ves
        # if n[-2]==n[-3]==0: return [[0,0,0]]
        # if not n[-2]|n[-3]: return [[0,0,0]]          # this is also right
        return []

    l = -len(n)
    op = []

    while l+2:
        i,j = l+1,-1
        t = -n[l]

        while i<j:
            s = n[i] + n[j]

            if s < t: i += 1
            elif s > t: j -= 1
            else:
                op += [[-t,n[i],n[j]]]

                while i<j:
                    i,j = i+1,j-1
                    if n[i-1] != n[i] or n[j+1] != n[j]:
                        break

        if t == 0 or -t > 0:
            return op

        while 1:
            l += 1
            if n[l-1] != n[l]: break

    return op


# advanced approach
# using two sum (without sorting array)
# but using extra space - 1 set & 1 dict
# fast(not more than method4) but not the right approach bcz using extra space
# TC - O(n^2), SC - O(n)
def method5(n: list[int]) -> list[list[int]]:
    # d = {}

    # l = len(n)-1
    l = len(n)-2
    # op = []
    op = set()

    k = 0
    # kSet = set()
    # kSet = set([])
    # kSet = {'-x'}
    # kSet = {0}
    # kSet = {}
    # kSet = { n[k] }
    kSet = { n[0] }

    d = { -n[0] - n[1]: 1 }

    j = 2

    # while k != l-1:
    # while k < l-1:
    # while k <= l-1:
    while k < l:
        # i,j = k+1,l
        # j = k+1
        # t = -n[k]

        print('1.\t',l-1,k,n[k])

        # if n[k] in kSet:
        #     k += 2
        #     while 1:
        #      while k != l-1:
        #         k += 1
        #         if n[k-1] != n[k]: break
        #     j = k
        # else:
        #     kSet.add(n[k])
        #     j = k+1

        # while n[k] in kSet:
        #     k += 1
            # if k >= l-1: return op

        # if k >= l-1: break

        # kSet.add(n[k])

        t = -n[k]
        # j = k+1
        # j = k

        print('2.\t',k,n[k],t,j)
        print('3.\t',kSet,d)

        # while i<j:
        # for i in range(j,len(n)):
        # for i in range(j,l):
        for i in range(j,l+2):
            # if -t in kSet and n[i] in kSet: continue
            # if t - n[i] in kSet and n[i] in kSet: continue
            # if n[i] in kSet or t - n[i] in kSet: continue           # current or future no.
            # x = set(sorted([-t,n[d[n[i]]],n[i]]))
            # if x in op: continue
            if n[i] in d:
                # op += [[-t,n[d[n[i]]],n[i]]]
                # op.add(tuple([-t,n[d[n[i]]],n[i]]))
                # op.add([-t,n[d[n[i]]],n[i]])
                # op.add(tuple(sorted([-t,n[d[n[i]]],n[i]])))
                # op.add(tuple(sorted(x)))
                # x = set(sorted([-t,n[d[n[i]]],n[i]]))
                x = sorted([-t,n[d[n[i]]],n[i]])
                # x = [-t,n[d[n[i]]],n[i]]
                if set(x) in op: continue
                # op.add(x)
                op.add(tuple(x))
                # d = {}
            # d[t - n[i]] = i
            else: d[t - n[i]] = i
            # d[i] = t - n[i]
            print('\t\t\t',i,d)
            print('\t\t\t',op,'\n')

        # k += 1
        # if n[k] in kSet:
            # k += 2
            # while 1:
            # while k != l-1:
                # k += 1
                # if n[k-1] != n[k]: break
            # j = k
        # else:
        #     kSet.add(n[k])

        while k < l:
            k += 1
            if n[k] not in kSet: break

        if k >= l: return op

        j = k+1
        kSet.add(n[k])
        d = {}

    return op



lists = []
lists += [[-1,0,1,2,-1,-4]]
lists += [[0,1,1]]
lists += [[0,0,0]]
lists += [[0,0,0,0,0,0]]
lists += [[0,0,0,0,0,0,0,0,0]]
lists += [[0,1,0,0,0,0,0,0,0]]
lists += [[-3,-2,-1]]
lists += [[-3,-2,-1,0]]
lists += [[-1,1,1]]
lists += [[-2,1,1]]
lists += [[-2,1,1,2]]
lists += [[-3,-2,1,1,2,5]]
lists += [[-2,0,0,2,2]]
lists += [[-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]]
lists += [[-2,0,2,7,11,15]]

for l in lists:
    print(l,'\n')
    print('\n',method5(l),'\n-------------------------')
# print(lists,'\n',method2(lists[0]))


# test cases
# [-1,0,1,2,-1,-4]
# [0,1,1]
# [0,0,0]
# [0,0,0,0,0,0]
# [0,0,0,0,0,0,0,0,0]
# [0,1,0,0,0,0,0,0,0]
# [-3,-2,-1]
# [-3,-2,-1,0]
# [-1,1,1]
# [-2,1,1]
# [-2,1,1,2]
# [-3,-2,1,1,2,5]
# [-2,0,0,2,2]
# [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]

