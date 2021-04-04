def method1(s: str) -> int:     # efficient in TC; using list
    size = len(s)
    if size==0: return 0

    i=0
    j=1
    count=0
    l1=[]

    # print("i :","j","count","s[j]","[s[i:j]]","l1\n")
    while j<size:

        # print(i,":",j,count,s[j],[s[i:j]],l1)
        if s[j] in s[i:j]:
            count=j-i
            l1+=[count]

            # print(i,j,count)
            i=s.index(s[j],i,j)+1

            # print(i,j,count,"\n")
        # else: print("i:",i,"j:",j)
        j+=1

    # print("\n",i,j,count,l1,j-i)
    l1 += [j-i]
    # print(l1)
    return max(l1)


def method2(s: str) -> int:     # very poorly efficient in TC & SC; using list & some extra condns.
    size = len(s)
    if size==0: return 0

    i=0
    j=1
    count=0
    l1=[]

    # print("i :","j","count","s[j]","[s[i:j]]","l1\n")
    while j<size:

        print(i,":",j,count,s[j],[s[i:j]],l1)
        if s[j] in s[i:j]:
            count=j-i
            l1+=[count]

            # print(i,j,count)
            i=s.index(s[j],i,j)+1

            # print("i:",i,"size:",size)
            if max(l1) >= size-i: break

            # print(i,j,count,"\n")
        # else: print("i:",i,"j:",j)
        j+=1

    print("\n",i,j,count,l1,j-i,size-i)
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

    # print("i :","j","count","s[j]","[s[i:j]]","\n")
    while j<size:

        # print(i,":",j,count,s[j],[s[i:j]])
        if s[j] in s[i:j]:
            if count < j-i:
                count=j-i

            # print(i,j,count)
            i=s.index(s[j],i,j)+1

            # print(i,j,count,"\n")
        # else: print("i:",i,"j:",j)
        j+=1

    # print("\n",i,j,count,j-i)
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
    # print(d)

    while j<size:
        if d[s[j]] < 1:
            d[s[j]] = 1
            # print("j",j,s[j],d)
        else:
            count = max(count,j-i)
            # print(count)
            while s[i] != s[j]: 
                d[s[i]] = 0
                i+=1
            i+=1
            # print("i:",i,s[i],d)
        j+=1

    # print("\n",i,j,count,j-i)
    count = max(count,j-i)
    # print(d)
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
# print(s)

# for i in range(len(s)):
    # print("\nm1",method1(s))
    # print("\nm2",method2(s))
    # print("\nm3",method3(s[i]))
print("\nm4",method4(s[6]))


