# nums = [4,1,2,1,2]

# for i in range(len(nums)):
#     print("\ni: ",i)
#     print("nums: ", nums)
#     if len(nums) == 1:
#         break;
#     else:
#         temp = nums[i]
#         print("temp: ",temp)
#         if temp in nums[:i] or temp in nums[i+1:]:
#             # z=nums[i]
#             # del(nums[i])
#             nums.remove(nums.pop(i))
#             # nums.remove(nums[i])
#             print("--- ", nums)

# print(nums)

def solve (N, S, A):
    # Write your code here
    print("\nold A: ", A)
    temp={}
    for i in range(N):
        # if S[i] in temp:
        #     x = temp.get(S[i])
        # else:
        #     temp[S[i]] = i
         
        if temp.get(S[i]) == None:      # if not in temp
            temp[S[i]] = i              # then add in temp
        else:             
            j = temp.get(S[i]) # 0
            # print("found clr at: ",i)

            swap = A[j]  # [0]=1
            print("swap: ", swap)
            print("i: ", i)
            print("j: ", j)
            A=A.replace(A[j],A[i])      #[0] = [4]
            print("(1 removed) A: ", A)
            B=A[i:].replace(A[i],swap)
            print("A: ", B)

    print("\n",temp,"\n")
    

    # return A
    

# N = int(input())
# S = input()
# A = input()

solve(4, "RGBR", "1054")
# print ("j: ",out_)