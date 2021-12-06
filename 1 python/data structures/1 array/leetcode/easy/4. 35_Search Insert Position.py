def method1(nums,t):        # using recursion, so only TC is efficient
    if nums[0] > t: return 0
    if nums[-1] < t: return len(nums)

    if nums[0] < 0:
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == t: return i
            if nums[i] < t: return i+1
            # print("i:",i,"len(nums)-i-1:",len(nums)-i-1)

    #else:
    if t == 0: return 0

    # print("\n1:",nums)

    if len(nums) > t:
        # print(nums[t])
        if nums[t] == t: return t
        nums = nums[:t]
    # print("\n2:",nums)

    if nums[-1] == t: return len(nums)-1
    # print("len(nums)-1:",len(nums)-1,"\tt:",t)

    if nums[-1] < t: return len(nums)

    y=0
    y = method1(nums[:len(nums)-1],t)
    # print("\n3:",nums,"y:",y)
    return y


def method2(nums,t):        # using loop, so both TC & SC are efficient
    if nums[0] > t: return 0
    if nums[-1] < t: return len(nums)
    
    if nums[0] < 0:
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == t: return i
            if nums[i] < t: return i+1
            print("i:",i,"len(nums)-i-1:",len(nums)-i-1)
    
    if t == 0: return 0
    
    # print("\n1:",nums)

    if len(nums) > t:
        # print(nums[t])
        if nums[t] == t: return t
        nums = nums[:t]
    # print("\n2:",nums)

    for i in range(len(nums)-1,-1,-1):
        if nums[i] == t: return i
        if nums[i] < t: return i+1
        print("i:",i,"len(nums)-i-1:",len(nums)-i-1)


def binary_search(nums,size,t):
    # if nums[0] > -1:
    #     if t == 0: return 0
    #     if size > t:
    #         if nums[t] == t: return t
    #         nums = nums[:t]

    # size = len(nums)
    i=0
    while i <= size:
        mid = i + (size - i) // 2

        if nums[mid] == t: return mid

        if nums[mid] < t: i = mid+1
        else: size = mid - 1


def method3(nums,t):            # using binary search
    if nums[0] > t: return 0
    size = len(nums)
    if nums[-1] < t: return size

    if nums[0] < 0:
        if t in nums: 
            return binary_search(nums,size,t)

        for i in range(size-1,-1,-1):
            if nums[i] < t: return i+1
            # print("i:",i,"len(nums)-i-1:",len(nums)-i-1)

    if t == 0: return 0

    # print("\n1:",nums)

    if size > t:
        # print(nums[t])
        if nums[t] == t: return t
        nums = nums[:t]
    # print("\n2:",nums)

    size = len(nums)
    if t in nums:
        return binary_search(nums,size,t)

    for i in range(size-1,-1,-1):
        if nums[i] < t: return i+1
        # print("i:",i,"len(nums)-i-1:",len(nums)-i-1)



# nums = [2,3,5,6]
nums = [0,1,3,5,7,8,10]
# nums = [0,1,2,3,5,6]
# nums = [1,3,4,6]
# nums = [5,6,8,10,13]
# nums = [2,5]



# print("\nm1",method1(nums,6),nums)
# print("\nm2",method2(nums,2),nums)
print("\nm3",method3(nums,2),nums)

