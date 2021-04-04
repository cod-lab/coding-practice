def method1(nums):          # poor effiency in both TC & SC
    res=[]
    size = len(nums)
    if size<2: return res

    '''
    index1 = []
    if 0 in nums:
        for i in range(size):
            # print("i:",i)
            if nums[i] != 0:
                if nums[i] not in index1:
                    if nums[i] in nums[i+1:]:
                        # index1 += [nums[i+1:].index(-nums[i]) + (i+1)]
                        index1 += [nums.index(nums[i],i+1,size)]
                    elif -nums[i] in nums[i+1:]:
                        index1 += [nums.index(-nums[i],i+1,size)]


    # print(index1,nums[index1[0]],nums[index1[1]],nums[index1[2]])
    print(nums)
    print(*index1,[nums[i] for i in index1])
    # print(index1,nums[index1[0:]])

    index1=[]
    if 0 in nums:
        for x in nums:
            if x != 0:
                if -x not in index1 and x not in index1:
                    index1 += [x]
                # print("\nx:",x,"index1:",index1)
                # if -x not in index1:
                #     index1 += [-x]

    print(index1)
    '''

    nums.sort()
    print(nums)

    for i in range(size-2):
    # while i<size-3:
        # if i>0 and nums[i]==nums[i-1]:
        #     continue
               
        l=i+1
        r=size-1
        print("\ni:",i,",l:",l,",r:",r)
        while l<r:
            # if l>1 and nums[l]==nums[l-1]:
            #     l+=1
            #     continue
            print("\tl:",l,",r:",r)
            add = nums[l]+nums[r]
            if -nums[i] == add:
                if [nums[i],nums[l],nums[r]] not in res:
                    res += [[nums[i],nums[l],nums[r]]]
                l+=1
                r-=1
            elif -nums[i] < add:
                r-=1
            # elif -nums[i] > nums[l]+nums[r]: l+=1
            else: l+=1

    return res



def method2(nums):          # efficient in both TC & SC
    res=[]
    size = len(nums)
    if size<2: return res

    nums.sort()
    print(size,nums)

    for i in range(size-2):
        if i>0 and nums[i]==nums[i-1]:
            continue

        l=i+1
        r=size-1
        print("\ni:",i,",l:",l,",r:",r)
        while l<r:
            print("\tl:",l,",r:",r)
            add = nums[i]+nums[l]+nums[r]
            if add > 0: r-=1
            elif add < 0: l+=1
            else:
                # if [nums[i],nums[l],nums[r]] not in res:
                res += [[nums[i],nums[l],nums[r]]]
                l+=1
                while nums[l]==nums[l-1] and l<r: l+=1
                # r-=1
                # while nums[r]==nums[r+1] and l<r: r-=1


    return res



# nums = [-1,2,0,-2,-1,-4,4,2,-2,1,3,3,3,-3,3,-3]
nums = [-1,-1,0,1,3,2,2,-1,4]
# nums = [-1,1,0]
# nums = [-1]
# nums = [0,0,0,0]
# nums = [3,0,-2,-1,1,2]



# print("\nm1",method1(nums))
print("\nm2",method2(nums))

