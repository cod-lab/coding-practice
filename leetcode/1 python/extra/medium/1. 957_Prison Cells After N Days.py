# There are 8 prison cells in a row and each cell is either occupied or vacant.

# Each day, whether the cell is occupied or vacant changes according to the following rules:

# If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

# You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant, and you are given an integer n.

# Return the state of the prison after n days (i.e., n such changes described above).

# Example 1:

# Input: cells = [0,1,0,1,1,0,0,1], n = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation: The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

# Example 2:

# Input: cells = [1,0,0,1,0,0,1,0], n = 1000000000
# Output: [0,0,1,1,1,1,1,0]

# Constraints:

# cells.length == 8
# cells[i] is either 0 or 1.
# 1 <= n <= 10^9

# import pprint as pp
# from pprint import pprint as pp
import re

def method1(cells: list[int], n: int) -> list[int]:       # TLE err but right solution with high TC
    l=[0]*8

    while n:
        # print(cells,l)
        for i in range(6):
            if cells[i] == cells[i+2]:
                l[i+1] = 1
            else: l[i+1] = 0
            # print(i,i+2,'cells:',cells[i],cells[i+2],'l:',l[i+1])

        cells = list(l)
        n -= 1

    print(cells,l)
    return l


def method2(cells: list[int], n: int) -> list[int]:      # new approach but not so efficient both TC & SC
    dp = []
    # noofdp=65
    # while n and noofdp:
    # k=0

    l=[0]*8
    # x=0
    while n:
        if cells not in dp:
            for i in range(6):                  # 6 bcz cells len is 8 & 0,7 are fixed i.e. 0
                if cells[i] == cells[i+2]:
                    l[i+1] = 1
                else: l[i+1] = 0

            dp += [cells]
            cells = list(l)
            n -= 1
            # x += 1
        else:
            # dp += [cells]
            break
    # print(dp,cells,l,n,x,len(dp)-1,dp[13+1])
    # print(dp,cells,l,n,x)

    if not n: return l

    # if cells not in dp:
    # dp += [cells]

    # print(dp,cells,l,n,x)

    if dp[0][0] or dp[0][7]:
        # dp = dp[1:]            # not an in-place method, i.e., takes extra space
        del dp[0]

    # return dp[(n%len(dp))+1]

    return dp[n%len(dp)]


def method3(cells: list[int], n: int) -> list[int]:      # same approach and little more efficiency than method2
    s = ''.join(str(x) for x in cells)      # convert list to string (for efficiency)
    l = ['0'] * 8
    print(s,l,len(l))

    dp={}
    # dp=set()
    while n:
        if s in dp: break
        # if s in dp.values(): break

        for i in range(6):          # 6 bcz cells len is 8 & 0,7 are fixed i.e. 0
            # if s[i] == s[i+2]:
            #     l[i+1] = '1'
            # else: l[i+1] = '0'
            l[i+1] = '1' if s[i] == s[i+2] else '0'

        dp[s] = n
        # dp[n] = s
        s = ''.join(l)
        n -= 1

    print(dp,s,n)

    if not n: return l

    cycle =  list(dp.keys())
    # print(cycle)

    # if dp[len(dp)+n][0] == '1' or dp[len(dp)+n][-1] == '1':
    #     del dp[len(dp)+n]

    if cycle[0][0] == '1' or cycle[0][7] == '1':
        del cycle[0]

    # return dp[n%len(dp)]
    return cycle[n%len(cycle)]


def method4(cells: list[int], n: int) -> list[int]:      # same approach and little more efficiency than method3
    # dp=[]
    dp=[cells]

    while n:
        # if cells in dp: print('break')
        # dp += [cells]
        # print(n,'1',dp,'\t',cells)
        n -= 1
        cells = [0] + [cells[i] ^ cells[i+2] ^ 1 for i in range(6)]  + [0]     # 6 bcz cells len is 8 & 0,7 are fixed i.e. 0
        # cells = str([0] + [cells[i] ^ cells[i+2] ^ 1 for i in range(6)]  + [0])

        # if cells in dp: break
        if cells in dp:
            # return dp[(n%(len(dp)-1))+1]
            l=len(dp)
            if l>14: return dp[(n%(l-1))+1]     # 14 is the max no. of lists(combinations) in a cycle, getting list from dp[[]] of len 15

        dp += [cells]
        # print(n,'2',dp,'\t',cells)
        # n -= 1

    # print(dp,cells)
    # if not n: return cells

    # print(n,j,len(dp))
    # if dp[0][0] | dp[0][7]:     # using bitwise or '|'
        # del dp[0]

    # return dp[n%len(dp)]
    return cells


def method5(cells: list[int], n: int) -> list[int]:      # same approach but worst efficiency than all
    # s = ''.join(str(*cells,sep=''))
    dp = { str(cells): n }
    print(dp)

    while n:
        print('1',dp,cells,n)
        n -= 1
        cells = [0] + [cells[i] ^ cells[i+2] ^ 1 for i in range(6)]  + [0]

        if str(cells) in dp:
            # n = n % (dp[str(cells)] - n)
            n %= dp[str(cells)] - n

        dp[str(cells)] = n
        print('2',dp,cells,n)

    return cells


def method6(cells: list[int], n: int) -> list[int]:      # same approach but worst efficiency than all (same as method5)
    dp = { str(cells): n }
    # s = ''.join(str(x) for x in cells)      # convert list to string (for efficiency)
    # dp = { s: n }

    while n:
        # print(cells,n)
        n -= 1
        cells = [0] + [cells[i] ^ cells[i+2] ^ 1 for i in range(6)]  + [0]

        if str(cells) in dp:
            l = len(dp)
            s = list(dp.keys())
            # print('found',cells,l)

            if l > dp[str(cells)] - n:
            # if l > 14:
                # return list(dp.keys())[(n%(l-1))+1]
                # print(list(dp.keys())[(n%(l-1))+1])
                # x=list(dp.keys())
                # print(y for y in x)
                # return x[(n%(l-1))+1]
                # return list(x[0])
                # s = list(dp.keys())[(n%(l-1))+1]
                # return re.sub(r'\[+|\]+|,+', '', s)
                # return re.sub(r'\[+|\]+|,+', '', s)
                # return re.sub(r'[^01]', '', s)
                return re.sub(r'[^01]', '', s[(n%(l-1))+1])       # matching pattern inside r'', replacing substring, string
            # return cells
            return re.sub(r'[^01]', '', s[n%l])

        dp[str(cells)] = n

    return cells


def method7(cells: list[int], n: int) -> list[int]:      # same approach but fastest of all
    dp=[cells]
    m=n

    while n:
        n -= 1
        cells = [0] + [cells[i] ^ cells[i+2] ^ 1 for i in range(6)]  + [0]

        if cells in dp:
            # print(dp)
            l = len(dp)

            # if l>14: return dp[(n%(l-1))+1]
            # if l>m-n: return dp[(n%(l-1))+1]
            # if dp[0][0] | dp[0][7]: return dp[(n%(l-1))+1]          # this also right but less efficient
            # print(n,l,n%l,(n%(l-1))+1)
            # if l > (l+n) - n: return dp[(n%(l-1))+1]
            if l > (m - dp.index(cells)) - n:
                return dp[(n%(l-1))+1]
            return dp[n%l]

        dp += [cells]

    return cells



lists = [[[0,1,0,1,1,0,0,1],7]]
lists += [[[0,1,0,1,1,0,0,1],70]]
lists += [[[1,0,0,1,0,0,1,0],1000000000]]
lists += [[[0,0,1,1,1,1,0,0],8]]
lists += [[[0,0,1,1,1,0,0,0],682529619]]
lists += [[[1,1,0,1,1,0,1,1],6]]
lists += [[[0,0,1,0,0,1,0,0],44640906]]


for l in lists:
    print(*l)
    print(method7(*l),'\n')
# print(method4(*lists[4]),'\n')


# test cases
# [0,1,0,1,1,0,0,1]
# 7
# [0,1,0,1,1,0,0,1]
# 70
# [1,0,0,1,0,0,1,0]
# 1000000000
# [0,0,1,1,1,1,0,0]
# 8
# [0,0,1,1,1,0,0,0]
# 682529619
# [1,1,0,1,1,0,1,1]
# 6
# [0,0,1,0,0,1,0,0]
# 44640906


