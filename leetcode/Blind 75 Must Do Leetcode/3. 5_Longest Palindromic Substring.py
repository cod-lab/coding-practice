# using recursion, not efficient in TC & SC
def method1(s: str,i: int,j: int,count: int) -> int:
    # size = len(s)
    # if size==1: return s
    # if size==2: return s[0]
    
    if i>j: return count
    if i==j: return count+1
    if s[i]==s[j]:
        # i+=1
        # j-=1
        count = method1(s,i+1,j-1,count) + 2
        # print(count)
    else:
        count = method1(s,i,j-1,count+2) #+ 2
        count = method1(s,i+1,j,count+2) #+ 2

    # if i>j:
    # if s[i] == s[j]:
    #     method1(s[i+1:j])


# using dp, very poor efficiency in both TC(n^2) & SC(n^2)
def method2(s: str) -> str:
    if not s: return ""
    
    size = len(s)
    # dp_T = [[0]*size]*size
    dp_T = [[0]*size for i in range(size)]
    # print(dp_T)

    for k in range(size):
        i=0
        j=k
        while j<size:
            if k==0: #i==j:
                dp_T[i][j] = 1
            elif k==1: #j-i==1:
                if s[i] == s[j]:
                    dp_T[i][j] = 1
            elif s[i] == s[j]:
                if dp_T[i+1][j-1]: #dp_T[i+1][j-1]==1
                    dp_T[i][j] = 1

            if dp_T[i][j]: #dp_T[i][j]==1
                count = k+1
                p,q=i,j
                # print(i,j,k,dp_T[i][j],count)

            i+=1
            j+=1    

    # print(p,q,count)
    # print(dp_T)
    return s[p:q+1]


# using "Expand Around Center" approach, efficient in SC(n) only and little bit in TC(n^2)
def method3(s: str) -> str:
    if not s: return ""
    
    s = s.replace("","#")
    print(s)
    size = len(s)

    # maxlen=1
    p,q=0,1
    for i in range(1,size-1):
        # print("i",i)
        j=1
        # count=1
        while i-j >= 0 and i+j <= size-1:
            # print(i,j,s[i-j],s[i],s[i+j])
            if s[i-j] == s[i+j]:
                # count = count+2
                j+=1
            else:
                # if count > maxlen:
                    # maxlen = count
                    # print("\ti:",i,"j:",j,"count:",count)
                    # a += [[i,j-1]]
                    # print("\t",a)
                break

        # print(i,j,count)
        if j>q:
            # maxlen = count
            # a = [i,j-1]
            p,q = i,j
            # print("\t",i,j,p,q)

        # if j+j-1>=size-i-1:
        if j-1 >= size-i-2:
            # print(i,j-1,size,size-i-2)
            break
        # else: print("no")

    # print(maxlen)
    print(p,q-1)
    # print(s[a[-1][0]-a[-1][1]:a[-1][0]+a[-1][1]+1].replace("#",""))
    # print(s[a[0]-a[1]+1:a[0]+a[1]].replace("#",""))
    # print(s[p-q+1 : p+q])
    # print("->",s[p-(q-2) : p+(q-1) : 2])
    print("->",s[p-q+2 : p+q-1])
    return s[p-q+2 : p+q-1 : 2]


# modified method3, efficient in SC(n) only and little bit in TC(n^2)
''' 
starting from center, take every ele and find its pallindrome, if its pallindrome length is c+c+1 then its the ans otherwise shift c in both two directions(left,right) by 1(one by one) and find their pallindrome, if pallindrome length comes l+l+1 then its the ans, and if length is r+r+1 then its the ans (anyone can be ans); but in this we are missing all the pallindromes created at each rejected center which can be used in future
'''
def method4(s: str) -> str:
    if not s: return ""

    s = s.replace("","#")
    print(*[i for i in range(len(s))],sep=" , ")
    print(*s,sep=" , ")
    size = len(s)

    # if size==5 and s[1] != s[3]: return s[1]

    c = int(size/2)
    j=1
    while c-j >= 0 and c+j <= size-1 and s[c-j] == s[c+j]:
        # print(c-j,c+j)
        j+=1

    # print("\nj:",j,"c:",c)
    # print(c-j,c+j)
    # print(c-(j-1),c+(j-1)+1)
    # print(s[c-(j-1) : c+(j-1)+1])
    # print(s[c-j+2 : c+j-1])

    # if not s: j+1  #j == size-c: return s[c-j+2 : c+j-1 : 2]
    # if not s: j+1  #j-1 == c: return s[c-j+2 : c+j-1 : 2]

    if j == c+1: return s[1 : size-1 : 2]
    # elif j == c-1: return s[3 : size-3 : 2]
    # else: print("no")
    else:
        p=j
        for i in range(1,c-1):
            l=c-i
            r=c+i

            j=1
            while l-j >= 0 and s[l-j] == s[l+j]:
                print(l-j,l+j,i,j,c-i)
                j+=1
            # if j-1 == l: return s[l-j+2 : l+j-1 : 2]
            # if j == c-i: return s[l-j+2 : l+j-1 : 2]
            # if j-1 > l-2: return s[1 : size-1 : 2]

            # if j == l+1: return s[l-(j-1) : l+(j-1)+1 : 2]
            if j>=p:
                if j == c-i+1: return s[l-(j-1) : l+(j-1)+1]
            else: print("1 no")
            # print("\nl/r ","j  ","l-j  ","l+j")
            # print(l,j,l-i,l+j,i,sep="    ")
            # break

            j=1
            while r+j <= size-1 and s[r-j] == s[r+j]:
                # print(r-j,r+j,i,j,c-i)
                j+=1
            # if j+i == r: return s[r-j+2 : r+j-1 : 2]
            # if j == c-i: return s[r-j+2 : r+j-1 : 2]
            # if j-1 > r-2: return s[1 : size-1 : 2]
            if j>=p:
                if j == c-i+1: return s[r-(j-1) : r+(j-1)+1]
            else: print("2 no")
            # elif j == c-i-2: return s[r-(j-1) : r+(j-1)+1 : 2]
            # print(r,j,r-i,r+j,i,sep="    ")
            # print("\n")
        
            # if j-i > j+i: return s[l-j+2 : l+j-1 : 2]
            # else: return s[r-j+2 : r+j-1 : 2]

        return s[c-p+2 : c+p-1]
    # return s[1]    



            
# using "Manacher's algo", efficient in both TC(2n) & SC(n)
def method5(s: str) -> str:
    if not s: return ""
    
    s = s.replace("","#")
    print(s)
    size = len(s)

    j=1
    p=[1]
    c,l,r,m=1,1,1,1
    # for i in range(1,size-1):
        
        
        

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
# print(s)

# for i in range(len(s)):
# print("\nm1",method1(s[1],0,len(s[1])-1,0))
# print("\nm2",method2(s[1]))
    # print("m3",method3(s[i]),"\n")
print("m4",method4(s[2]),"\n")

