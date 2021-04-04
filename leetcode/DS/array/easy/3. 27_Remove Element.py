def method1(nums,val):      # python dependent
    rep = nums.count(val)
    for i in range(rep):
        nums.remove(val)
    return len(nums)


def method2(nums,val):
    if val in nums:
        size = len(nums)
        nums.sort()
        rep = nums.count(val)
        i = nums.index(val)
        nums[:] = nums[:i] + nums[rep+i:]
        return size - rep


def method3(nums,val):      # brute force
    if val in nums:
        size = len(nums)
        i = nums.index(val)
        del[nums[i]]

        while i < size-1:
            if nums[i] == val:
                del[nums[i]]
                size-=1
            else: i+=1


def method4(nums,val):      # advance methods3
    if val in nums:
        
        size = len(nums)
        if size == 1:
            del[nums[0]]
            return 0
        
        rep = nums.count(val)
        i = nums.index(val)
        if rep == 1:
            del[nums[i]]
            return size-1

        del[nums[i]]
        size-=1
        while rep > 1:
            if nums[i] == val:
                del[nums[i]]
                size-=1
                rep-=1
            else: i+=1

        return size


def method5(nums,val):      # without performing any del opt
    if val in nums:
        
        size = len(nums)
        if size == 1:
            del[nums[0]]
            return 0
        
        rep = nums.count(val)
        i = nums.index(val)
        if rep == 1:
            del[nums[i]]
            return size-1

        j=i
        while i+1 < size:
            if nums[i+1] != val:
                nums[j] = nums[i+1]
                rep-=1
                j+=1
            i+=1

    return j



# nums1 = [0,0,1,1,1,2,2,3,3,4]
# nums2 = [2,1]
nums2 = [1,0,0,1,1,1,2,2,3,3,1,1,4,4]
# nums2= [1]
# nums5 = [3,2,2,3]


# print("\nm1",method1(nums1,3),nums1)
print("\nm2",method2(nums2,1),nums2)
# print("\nm3",method3(nums3,1),nums3)
# print("\nm4",method4(nums4,3),nums4)
# print("\nm5",method5(nums5,2),nums5)

