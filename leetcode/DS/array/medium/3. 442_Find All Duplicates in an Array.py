def method1(nums):              # best of all from below methods
    nums2 = set(nums)
    for x in nums:
        if x in nums2:
            nums2.remove(x)
        else: nums2.add(x)
    
    return nums2


def method2(nums):
    l1=[]
    d={}
    for x in nums:
        if x not in d:
            d[x]=1
        else: l1 += [x]

    return l1


def method4(nums):              # correct but TLE
    l1=[]
    for i in range(len(nums)):
        if nums[i] not in l1 and nums[i] in nums[i+1:]:
                l1 += [nums[i]]

    return l1


def method6(nums):              # correct but TLE
    size = len(nums)
    for i in range(size):
        if nums[i] in nums[:i]:
            nums[i] *= -1

    return [-x for x in nums if x<0]

    
def method7(nums):          # very less efficient in both TC & SC
    size = len(nums)
    for i in range(size):
        if nums[abs(nums[i])-1] < 0:
            nums += [abs(nums[i])]
        nums[abs(nums[i])-1] *= -1

    return nums[size:]


nums = [4,3,2,7,8,2,3,1,1,10]


# print("\nm1",method1(nums))
# print("\nm2",method2(nums))
# print("\nm3",method3(nums))
# print("\nm4",method4(nums))
# print("\nm5",method5(nums))
# print("\nm6",method6(nums))
print("\nm7",method7(nums))

