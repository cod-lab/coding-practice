# using dp, very poor efficiency in both TC(n^2) & SC(n^2)
def method2(s: str) -> str:
    if not s: return ""
    
    size = len(s)
    dp_T = [[0]*size for i in range(size)]

    for k in range(size):
        i=0
        j=k
        while j<size:
            if k==0:
                dp_T[i][j] = 1
            elif k==1:
                if s[i] == s[j]:
                    dp_T[i][j] = 1
            elif s[i] == s[j]:
                if dp_T[i+1][j-1]:
                    dp_T[i][j] = 1

            if dp_T[i][j]:
                p,q=i,j

            i+=1
            j+=1    

    return s[p:q+1]


# using "Expand Around Center" approach, efficient in SC(n) only and little bit in TC(n^2)
def method3(s: str) -> str:
    if not s: return ""
    
    s = s.replace("","#")
    size = len(s)

    p,q=0,1
    for i in range(1,size-1):
        j=1
        while i-j >= 0 and i+j <= size-1:
            if s[i-j] == s[i+j]: j+=1
            else: break

        if j>q: p,q = i,j

        if j-1 >= size-i-2: break

    return s[p-q+2 : p+q-1 : 2]
     
        
        

s = [""]
s += ["a"]
s += ["abdv"]
s += ["cbbd"]
s += ["bbbbbbbb"]
s += ["pwwkewwe"]
s += ["babad"]
s += ["abababab"]
s += ["abccbc"]
s += ["abaxabaxabybaxabyb"]
s += ["dvdf"]
s += ["abrexrzx"]

# for i in range(len(s)):
    # print("\nm2",method2(s[1]))
    # print("m3",method3(s[i]),"\n")

