def method1(nums):          # poor effiency in both TC & SC
    res=[]
    size = len(nums)
    if size<2: return res

    nums.sort()

    for i in range(size-2):
        l=i+1
        r=size-1
        while l<r:
            add = nums[l]+nums[r]
            if -nums[i] == add:
                if [nums[i],nums[l],nums[r]] not in res:
                    res += [[nums[i],nums[l],nums[r]]]
                l+=1
                r-=1
            elif -nums[i] < add: r-=1
            else: l+=1

    return res


def method2(nums):          # efficient in both TC & SC
    res=[]
    size = len(nums)
    if size<2: return res

    nums.sort()

    for i in range(size-2):
        if i>0 and nums[i]==nums[i-1]: continue

        l=i+1
        r=size-1
        while l<r:
            add = nums[i]+nums[l]+nums[r]
            if add > 0: r-=1
            elif add < 0: l+=1
            else:
                res += [[nums[i],nums[l],nums[r]]]
                l+=1
                while nums[l]==nums[l-1] and l<r: l+=1

    return res



# nums = [-1,2,0,-2,-1,-4,4,2,-2,1,3,3,3,-3,3,-3]
nums = [-1,-1,0,1,3,2,2,-1,4]
# nums = [-1,1,0]
# nums = [-1]
# nums = [0,0,0,0]
# nums = [3,0,-2,-1,1,2]



# print("\nm1",method1(nums))
print("\nm2",method2(nums))

