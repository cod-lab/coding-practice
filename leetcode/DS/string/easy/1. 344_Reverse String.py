def method1(s: list) -> None:
    print(s[::-1])
    print(s[-1::-1])
    print(s[-1 : -len(s)-1 : -1])

    # s = s[::-1]
    s[:] = s[::-1]
    
    return s

    
def method2(s: list) -> None:
    size = len(s)
    l,r = 0,size-1
    while l<r:
        if s[l] != s[r]:
            s[l],s[r] = s[r],s[l]
        l+=1
        r-=1

    return s



s=["h","e","l","l","o"]
# s=["H","a","n","n","a","h"]

# print(method1(s))
print("m2",method2(s))

