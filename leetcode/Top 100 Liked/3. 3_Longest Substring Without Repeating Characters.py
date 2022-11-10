# MEDIUM

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:

# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.

def method1(s: str) -> int:         # ✖ wrong method
    # a = set()
    a=[]
    l=[]
    for c in s:
        if c not in a:
            a.append(c)
        # print(c)
        # if c in a:
        #     print(a)
        #     l.append(len(a))
        #     a=[]
        # else: a.append(c)
        else:
            l.append(len(a))
            a=[c]

    l.append(len(a))

    print(a,l)

def method2(s: str) -> int:     # little less efficient but almost equal
    print('s',s)
    # a={}
    # a=[]
    a=''
    l=[]
    # for i in range(len(s)):
    for c in s:
        # if s[i] not in a:
        if c not in a:
            # a[s[i]] = i
            # a += [s[i]]
            a += c
        else:
            l += [len(a)]
            print('1',a,l)
            # j = s[i]
            # j=0
            # while a[0] != s[i]:
            while a[0] != c:
            # while 1:
                # del a[a[]]
                # print(j,a[j],s[i],i)
                # if a[0] != s[i]:
                    # del a[0]
                    a = a[1:]
                # else: break
                # j += 1
            # a += [s[i]]
            # a = a[1:] + [s[i]]
            # a = a[1:] + [c]
            # print('1',a,l)
            a = a[1:] + c
            # l += [len(a)]
            print('2',a,l)

    l += [len(a)]

    print(a,l,'\n')

def method3(s: str) -> int:     # little more efficient but almost equal
    print('s',s)

    size = len(s)
    if not size: return 0

    i=0
    j=1
    l=0

    while j<size:
        if s[j] in s[i:j]:
            print('1.',i,j,l)
            if l<j-i: l = j-i
            # while s[i] != s[j]: i += 1    # correct but slower
            # i += 1
            i = s.index(s[j],i,j) + 1
        # else: j += 1
        j += 1
        print('2.',i,j,l)

    # if l<j-i: l = j-i
    return j-i if j-i > l else l

    # print(i,j,l,'\n')



s = ['abcabcbb']
s += ['bbbbb']
s += ['pwwkew']
s += ['dvdf']
s += ['abrexrzx']
s += ['hbacdeagh']
# s = ['hbacdeagh']

print(s,'\n')
for s in s:
    # print(method2(s))
    method3(s)


