def method1(s: str) -> int:     # efficient in TC; using list
    size = len(s)
    if size==0: return 0

    i=0
    j=1
    count=0
    l1=[]

    while j<size:
        if s[j] in s[i:j]:
            count=j-i
            l1+=[count]
            i=s.index(s[j],i,j)+1
        j+=1
    l1 += [j-i]

    return max(l1)


def method2(s: str) -> int:     # very poorly efficient in TC & SC; using list & some extra condn's.
    size = len(s)
    if size==0: return 0

    i=0
    j=1
    count=0
    l1=[]

    while j<size:
        if s[j] in s[i:j]:
            count=j-i
            l1+=[count]

            i=s.index(s[j],i,j)+1

            if max(l1) >= size-i: break
        j+=1

    if len(l1)==0: return j-i
    
    longest_substring = max(l1)
    if longest_substring < size-i:
        return j-i
    return longest_substring


def method3(s: str) -> int:     # most efficient in TC & SC, no ds used
    size = len(s)
    if size==0: return 0

    i=0
    j=1
    count=0

    while j<size:
        if s[j] in s[i:j]:
            if count < j-i:
                count=j-i

            i=s.index(s[j],i,j)+1

        j+=1

    if count < j-i:
        count=j-i
    return count


def method4(s: str) -> int:     # not much efficient in TC & SC; using dict
    size = len(s)
    if size==0: return 0

    i=0
    j=0
    count=0

    d={}
    for k in range(size): d[s[k]] = 0

    while j<size:
        if d[s[j]] < 1:
            d[s[j]] = 1
        else:
            count = max(count,j-i)
            while s[i] != s[j]: 
                d[s[i]] = 0
                i+=1
            i+=1
        j+=1

    count = max(count,j-i)
    return count


s=[]
s += ["abcabcbb"]
# s="abc abc bd"
s += [""]
s += ["pwwkew"]
s += ["au"]
s += ["bbbb"]
s += ["dvdf"]
s += ["abrexrzx"]

# for i in range(len(s)):
    # print("\nm1",method1(s))
    # print("\nm2",method2(s))
    # print("\nm3",method3(s[i]))
print("\nm4",method4(s[6]))


