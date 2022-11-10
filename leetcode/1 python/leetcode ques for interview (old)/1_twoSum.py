class TwoSum:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def unsorted_list(self, nums, target):
        cache={}
        for i in range(len(nums)):
            # if nums[i] < target:      # only works for Z+
                print(cache)                         # i=4
                '''
                    # if cache.get(nums[i]) != None:
                    #     return [cache[nums[i]], i]      # i=2
                    # else: cache[target - nums[i]] = i         # i=0,1

                    # if cache.get(nums[i]) == None:      # if key(no.) not in dict
                    # if nums[i] not in cache:
                    #     cache[target - nums[i]] = i         # i=0,1
                    # else: return [cache[nums[i]], i]      # i=2
                '''

                if nums[i] in cache:                 # i=4
                    return [cache[nums[i]], i]
                cache[target - nums[i]] = i         # i=3

    def sorted_list(self,nums,target):
        nums.sort()
        cache={}
        # for i in range(len(nums[:target])):
        for i in range(len(nums)):
            # if nums[i] < target:      # only works for Z+
                print(cache)                         # i=4
                '''
                    # if cache.get(nums[i]) != None:
                    #     return [cache[nums[i]], i]      # i=2
                    # else: cache[target - nums[i]] = i         # i=0,1

                    # if cache.get(nums[i]) == None:      # if key(no.) not in dict
                    # if nums[i] not in cache:
                    #     cache[target - nums[i]] = i         # i=0,1
                    # else: return [cache[nums[i]], i]      # i=2
                '''
                
                if nums[i] in cache:                 # i=4
                    return [cache[nums[i]], i]
                cache[target - nums[i]] = i         # i=3


obj1=TwoSum()
print("UNSORTED:")
# print(obj1.unsorted_list([7,10,12,8,2,15],9))
print(obj1.unsorted_list([-3,4,3,90],0))
print("\nSORTED:")
print(obj1.sorted_list([7,10,3,8,2,15],13))

# 23781015
# [1,2,7,10,12,15]
# 23781115
