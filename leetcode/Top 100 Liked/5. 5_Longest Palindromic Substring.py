# MEDIUM

# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# import re

def method1(s: str) -> str:
    slen = len(s)
    if slen == 1: return s
    if slen == 2:
        # if s[0] != s[1]: return s[0]
        return s if s[0] == s[1] else s[0]

    s = s.replace("","#")
    print(s,'\n')

    # l= len(s)
    # slen = len(s)-2
    # if slen == 1: return s[1]
    # slen = ((slen*2)+1) - 2           # right but more calc
    slen = (slen*2) - 1         # excluding first & last ele i.e. '#'
    # print(s,slen)

    # plen = 0
    # p=[]
    q=r=''
    # x=y=-1

    for i in range(1,slen):
        j=i
        k=0
        while s[j-k] == s[j+2+k]:
            # plen += 2
            # p=s[i]+s[i+2]
            # p = s[j]+p+s[j+2]
            # xs = s[j-k] + (xs or s[j+k+1]) + s[j+2+k]
            # xs = s[j-k] + (xs or s[j+1]) + s[j+2+k]           # this is also right
            # xs = s[j-k] + xs + s[j+2+k]
            # x = j-k             # this is also right
            # y = j+2+k           # this is also right
            k += 1
            # if j==k or j+k == slen:
            if j==k or j+k == slen-1:           # if left = s[0] & right = s[-1], bcz excluding both first and last ele i.e. '#'
            # if j<k or j+k == slen:
                break

        # xs = s[x:y+1]           # this is also right
        # xs = s[j-(k-1):j+2+k]
        # xs = s[j-(k-1):j+2+k].replace('#','')
        r = s[j-(k-1):j+2+k].replace('#','')
        # r = s[j-(k-1):j+2+k]

        # print(xs,i)
        # p += [xs]
        # q = xs if len(xs) > len(q) else q
        # if len(xs) > len(q): q = xs
        if len(r) > len(q):
            # q = r[1::2] if r[0] == '#' else r[::2]
            q = r
        # if len(xs.replace('#','')) > len(q.replace('#','')): q = xs
        # if len(re.findall('\w',xs)) > len(re.findall('\w',q)):
            # q = xs
        # print(xs,i)
        # plen += 1
        # xs = ''
        # r = ''
        # if i+1 == len(s)//2 and len(q)> len(s)//2: return q.replace('#','')
        # if i == len(s)//2 and len(q) == len(s): return q.replace('#','')

        # if i+1 == len(s)//2:
        # if i >= slen//2:

        # if i >= len(s)//2:
        # if i == len(s)//2:

            # if len(q) > len(s)//2: return q.replace('#','')

            # if len(q) == len(s): return q.replace('#','')
            # if len(q) >= ((len(s)//2) - i) + ((len(s)//2) - i -1):
            # if len(q) >= ((len(s)//2) - (i+1)) + ((len(s)//2) - (i+1) -1):
                # return q.replace('#','')
        # if i >= len(s)//2:
        # if i >= (len(s)//2)-1:
        if i >= slen//2:                # when i passes center (from center to end)
        # if i >= (len(s)//2)-2:
        # if i >= (len(s)//2)+1:
            '''print(
                '\t\t',i,l,l//2,
                '\t',l-i,(l - i) + (l - i -1)-2,
                '\t',len(q),(slen - i) + (slen - i -1)-2,
                ((l-1) - i) + ((l-1) - i -1)-2,
            )'''
            # print('\t\t',l,i,2*(slen-i) - 1)
            # if len(q) >= ((len(s)//2) - i) + ((len(s)//2) - i -1):
            # if len(q) >= (l - i) + (l - i -1) - 2:
            # if len(q) >= (l - i) + (l - i -1) - 3:
            # if len(q) >= 2*(slen-i) - 1:                # checking next position max string limit
            print(q,(len(q)*2)-3, 2*(slen-i)-3,'\t',len(q), slen-i,'\t',i)
            # if (len(q)*2)-1 >= 2*(slen-i) - 1:
            # if len(q) >= 2*(slen-i) - 3:
            if len(q) >= slen-i:
            # if 2*len(q) - 3 >= 2*(slen-i) - 3:
                # return q.replace('#','')
                # return q[1::2] if q[0] == '#' else q[::2]
                return q

            if slen - i == 2: return q      # if given string has no palindrome

    # print(l,slen,plen,p,xs,q)

    # return q
    # return q[::2]
    # return q.replace('#','')



s = []
s += ["abcddcbawe"]
s += ["jnlabcdcbahbu"]
s += ["babad"]
s += ["a"]
s += ["cbbd"]
s += ["bbcd"]
s += ["abababab"]
s += ["abccbc"]
s += ["abaxabaxabybaxabyb"]
s += ["dvdf"]
s += ["aaaebbbb"]
s += ["bbbbbbbb"]
s += ["pwwkewwe"]
s += ["abrexrzx"]
s += ["abdv"]
s += ["ac"]


for x in s:
    print(x)
    print(method1(x),'\n\n')
# print('\n',method1('abrexrzx'))


# test cases
# "abcddcbawe"
# "jnlabcdcbahbu"
# "babad"
# "a"
# "abdv"
# "cbbd"
# "bbcd"
# "bbbbbbbb"
# "pwwkewwe"
# "abababab"
# "abccbc"
# "abaxabaxabybaxabyb"
# "dvdf"
# "abrexrzx"


