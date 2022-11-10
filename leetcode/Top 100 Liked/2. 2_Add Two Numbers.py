# MEDIUM

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    # least efficient
    def method1(self, l1: ListNode, l2: ListNode) -> ListNode:
        # x=y=''
        x=[]
        y=[]
        z=[]
        # a=[]
        i=0
        while 1:
        # while l1.next or l2.next:
        # while l1.val or l2.val:
            if l1.next:
                # x = x + str(l1.val)
                x += [l1.val]
                # z.append(l1.val)
                # a.append(l1.val)
                l1 = l1.next

            if l2.next:
                # y = y + str(l2.val)
                y += [l2.val]
                # z[i] = z[i] + l2.val
                # a.append(l2.val)
                l2 = l2.next

            if not l1.next and not l2.next:
                # x = x + str(l1.val)
                # y = y + str(l2.val)
                x += [l1.val]
                y += [l2.val]
                # z.append(l1.val + l2.val)
                # a.extend(l1.val,l2.val)
                break
            # if not l1.val and not l2.val: break
            i+=1
        print(x,y,z)
        # z = str(int(x) + int(y))
        l3 = tmp = ListNode()
        # return [7,0,8]

        j=0
        # loop = max(len(x),len(y))
        xlen = len(x)
        ylen = len(y)
        # print(xlen,ylen)
        # a = x+y
        sum=0
        carry=0
        while 1:
            if j<xlen and j<ylen:
                sum=x[j]+y[j] + carry
                if sum > 9:
                    # sum = (sum-10) + carry
                    sum = sum-10
                    carry = 1
                    # sum = (sum-10) + 1
                else: carry = 0
                z.append(sum)
                tmp.val = sum
                j+=1
                if j>=xlen and j>=ylen: break
                else:
                    tmp.next = ListNode()
                    tmp=tmp.next
                # print(j,xlen,ylen)
                continue
            if j>=xlen and j<ylen:
                sum = 0+y[j] + carry
                if sum > 9:
                    sum = sum-10
                    carry = 1
                else: carry = 0
                z.append(sum)
                tmp.val = sum
                j+=1
                if j>=xlen and j>=ylen: break
                else:
                    tmp.next = ListNode()
                    tmp=tmp.next
                # print(j,xlen,ylen)
                continue
            if j<xlen and j>=ylen:
                sum = x[j]+0 + carry
                if sum > 9:
                    sum = sum-10
                    carry = 1
                else: carry = 0
                z.append(sum)
                tmp.val = sum
                j+=1
                if j>=xlen and j>=ylen: break
                else:
                    tmp.next = ListNode()
                    tmp=tmp.next
                # print(j,xlen,ylen)
                continue

            break
        if carry:
            z.append(1)
            tmp.next = ListNode()
            tmp=tmp.next
            tmp.val = 1
            # tmp.next=None
        # else: tmp.next=None
        print('z',z,'\nl3',l3)
        return l3


    # most efficient
    def method2(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = tmp = ListNode()
        sum = 0

        while l1 or l2 or sum:
            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            # print('1 tmp',tmp)

            # tmp.val = sum%10
            tmp.next = ListNode(sum%10)
            tmp = tmp.next
            sum = sum//10

        print('l3',l3,'\n',tmp)
        return l3.next


    # medium efficiency
    def method3(self, l1: ListNode, l2: ListNode) -> ListNode:
        x=y=''
        while l1:
            x += str(l1.val)
            l1=l1.next
        while l2:
            y += str(l2.val)
            l2=l2.next

        z=str(int(x[::-1])+int(y[::-1]))[::-1]

        l3=tmp=ListNode()
        for n in z:
            tmp.next = ListNode(n)
            tmp=tmp.next

        print(x,y,z,l3)
        # print(x,y,z)

        return l3.next



x = [2,4,3,7,8,9]
y = [5,6,1]

xlen = len(x)
ylen = len(y)

l1 = t1 = p1 = ListNode()
l2 = t2 = p2 = ListNode()

# create linked lists
while xlen or ylen:
    if xlen:
        t1.next = ListNode(x[-xlen])
        t1 = t1.next
        xlen -= 1

    if ylen:
        t2.next = ListNode(y[-ylen])
        t2 = t2.next
        ylen -= 1

# print linked lists
while p1 or p2:
    if p1:
        print(p1.val)
        p1=p1.next
    if p2:
        print(p2.val)
        p2=p2.next


obj = Solution()
print(obj.method3(l1.next,l2.next))

