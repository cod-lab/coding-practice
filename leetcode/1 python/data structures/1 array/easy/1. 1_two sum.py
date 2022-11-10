# def twoSum(self, nums: list[int], target: int) -> list[int]:

def method1(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j:
                if nums[i] + nums[j] == target:
                    return[i,j]


def method2(nums, target):
	# cache = [[],[]]
	cache2 = {}
	for i in range(len(nums)):
		# cache += [[i],[target - nums[i]]]\
		# if (nums[i] <= target) or (nums[i] in cache2):
		if nums[i] in cache2:
			print(cache2)
			return[cache2[nums[i]],i]
		cache2[target - nums[i]] = i



# nums = [-3,4,3,90]
# target = 0
nums = [3,2,4]
target = 6
# nums = [11,3,2,15,5,7,4]
# target = 9

print("m1",method1(nums, target),"\n")
print("m2",method2(nums, target))
