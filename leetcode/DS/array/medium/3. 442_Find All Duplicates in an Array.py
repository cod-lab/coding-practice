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
    # l2=[]
    for x in nums:
        if x not in d:      # l2:
            d[x]=1
            # l2 += [x]
        else: l1 += [x]

    # print(l1,l2)
    return l1

'''
def method3(nums):
    l1 = nums
    print(nums)
    print(l1)
    
    # for i in range(len(nums)):
    i=0
    j=0
    while i<len(nums):
        if l1[j] == nums[i]:
            # l1 = l1[:j]+l1[j+1:]
            del[l1[j]]
            print(l1)
            i+=1
        else: j+=1
    
    return l1
'''

def method4(nums):              # correct but TLE
    l1=[]
    # d={}
    for i in range(len(nums)):
        if nums[i] not in l1 and nums[i] in nums[i+1:]:
                l1 += [nums[i]]
                # d[nums[i]] = 1

    return l1   # d.keys()

'''
def method5(nums):
    cache={}
    for i in range(len(nums)):
        if nums[i] in cache:
            return [nums[i],i]
        cache[0-nums[i]] = i
        print(cache)
'''

def method6(nums):              # correct but TLE
    size = len(nums)
    for i in range(size):
        # if nums[i] > 0 and 
        print(i)
        if nums[i] in nums[:i]:
            nums[i] *= -1

    print(nums)
    return [-x for x in nums if x<0]

    
def method7(nums):          # very less efficient in both TC & SC
    l1=[]
    size = len(nums)
    for i in range(size):
        # print(nums[i],abs(nums[i]),abs(nums[i])-1,nums[abs(nums[i])-1])
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

