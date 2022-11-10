def method1(nums):      # best sol for TC only and also python dependent
    nums[:]=sorted(list(set(nums)))
    return len(nums)


def method2(nums):      # best sol for SC only
    size = len(nums)
    i=1
    while i < size:
        # print(i-1,nums[i-1])
        # print("nums",nums)
        # print("size",size)
        if nums[i-1] == nums[i]:
            del[nums[i-1]]
            size-=1
            i-=1
        i+=1
    return size

'''
def method3(nums):
    cache = []
    j=0
    cache += [nums[+j]]
    print("cache",cache)
    size = len(nums)
    i=1
    while i < size:
        # print(i-1,nums[i-1])
        # print("nums",nums)
        # print("size",size)
        if nums[i] == cache[j]:
            del[nums[i-1]]
            size-=1
            i-=1
            j+=1
        i+=1
    return len(nums)
'''

def method4(nums):      # best sol for both TC & SC
    size = len(nums)
    i=1
    j=1
    while i < size:
        # print("nums",nums)
        # print("i:",i,"j:",j)
        # print("size",size)
        if nums[i-1] != nums[i]:
            nums[j] = nums[i]
            j+=1
        i+=1

    # print("after loop\nnums",nums)
    # print("i:",i,"j:",j,"size:",size)
    return j


def method5(nums):      # method4 using for loop
    size = len(nums)
    j=1
    for i in range(size-1):
        if i < size:
            # print("nums",nums)
            # print("i:",i,"j:",j)
            # print("size",size)
            if nums[i] != nums[i+1]:
                nums[j] = nums[i+1]
                j+=1

    # print("after loop\nnums",nums)
    # print("i:",i,"j:",j,"size:",size)
    return j


nums1 = [0,0,1,1,1,2,2,3,3,4]
nums2 = [0,0,1,1,1,2,2,3,3,4]
nums3 = [0,0,1,1,1,2,2,3,3,4]
nums4 = [0,0,1,1,1,2,2,3,3,4]
nums5 = [0,0,1,1,1,2,2,3,3,4]

# print("m1",method1(nums1),nums1,"\n")
# print("m2",method2(nums2),nums2)
# print("m3",method3(nums3),nums3)
print("\nm4",method4(nums4),nums4)
print("\nm5",method5(nums5),nums5)










# def method2(nums):
    # for i in range(len(nums)):
    #     print(nums)
    #     print(i, nums[i], nums[i+1])
    #     if nums[i] == nums[i+1]:
    #         del[nums[i]]
    #         i-=1
    # return(nums)
    
    # i=0
    # for x in nums:
    #     if x == nums[i+1]:
    #         del[nums[i]]
    #         print(x)

    # size = len(nums)
    # i=0
    # for i  in range(size):
    #     print("nums",nums)
    #     print("i = ",i, nums[i], nums[i+1])        
    #     if nums[i] == nums[i+1]:
    #         del[nums[i]]
    #         i-=1
    #         size-=1
    #         print("i = ",i,"size = ",size)
    # return(nums)