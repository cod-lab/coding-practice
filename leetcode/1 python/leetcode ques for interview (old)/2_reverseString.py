class Solution:
    # def reverseString(self, s: List[str]) -> None:
    def reverseString(self, s) -> None:
        l=len(s)
        i=0
        s.extend(s[-(i+1)::-1])
        del(s[i:l])
        print("reversed string: ", s)


obj1=Solution()
obj1.reverseString(["h","e","l","l","o"])
# print("original string: ", obj1.reverseString())
# print("reversed string: ", obj1.reverseString(["h","e","l","l","o"]))
# print(obj1.unsorted_list([7,10,12,8,2,15],9))
