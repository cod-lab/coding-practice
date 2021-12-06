class Solution:
    def singleNumber(self, nums) -> int:        
        ''' 
            # out=[]
            # count=1
            # for i in range(len(nums)):
                # if nums[i] in out:
                #     out.remove(nums[i])
                # else:    
                #     out.append(nums[i])
                    
                # if nums[i] not in out:
                #     out.append(nums[i])
                # else:
                #     out.remove(nums[i])
                    
                # out.append(nums[i]) if nums[i] not in out else out.remove(nums[i])        # slow code
                # temp = nums[i]
                # print(temp)
                # if temp in nums[:i] or temp in nums[i+1:]:
                #     nums.remove(nums[i])
                #     print(nums)
                # # else:
                # #     count+=1
                # print(temp) 
        # '''

        '''
            for i in range(len(nums)):
                print("\ni: ",i)
                print("nums: ", nums)
                if len(nums) == 1:
                    break
                else:
                    temp = nums[i]
                    print("temp: ",temp)
                    if temp in nums[:i] or temp in nums[i+1:]:
                        nums.remove(nums.pop(i))
                        print("--- ", nums)
        '''

        # lowest space complexity & highest time complexity
        '''
            j=-1
            for i in range(len(nums)):
                j+=1
                print("\ni: ",i)
                print("nums: ", nums)
                if len(nums) == 1:
                    break
                else:
                    temp = nums[j]
                    print("temp: ",temp)
                    if temp in nums[:j] or temp in nums[j+1:]:
                        nums.remove(nums.pop(j))
                        print("res: ", nums)
                        j=-1
                        print("j: ",i)
        '''
        
        # using bit manipulation
        
        
        
        return nums[0]


obj1=Solution()
print(obj1.singleNumber([4,1,2,1,2]))


'''
    if nums[i] not in out:
        out.append(nums[i])
    else:
        out.remove(nums[i])
'''

# old sol. (bad code)
'''
    class Solution:
        def singleNumber(self, nums: List[int]) -> int:
            out=[]
            for i in range(len(nums)):
                if nums[i] not in out:
                    out.append(nums[i])
                else:
                    out.remove(nums[i])

            return out[0]
'''
