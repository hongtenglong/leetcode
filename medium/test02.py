#https://leetcode-cn.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = l1.val + l2.val
        if (l1.next == None and l2.next == None):
            if (sum < 10):
                return ListNode(val=sum, next=None)
            else:
                return ListNode(val=sum % 10, next=ListNode(val=1, next=None))

        else:
            if (sum < 10):
                return ListNode(val=sum, next=self.addTwoNumbers(self
                                                                 ,ListNode(l1.next.val, l1.next.next) if l1.next != None else ListNode(0,None)
                                                                 ,ListNode(l2.next.val, l2.next.next) if l2.next != None else ListNode(0,None)
                                                                 ))
            else:
                return ListNode(val=sum % 10,
                                next=self.addTwoNumbers(self,ListNode(l1.next.val+1, l1.next.next) if l1.next != None else ListNode(1,None)
                                                            ,ListNode(l2.next.val, l2.next.next) if l2.next != None else ListNode(0,None)))



l1 = ListNode(9,ListNode(9,(ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9))))))))))
l2 = ListNode(9,ListNode(9,(ListNode(9,ListNode(9,ListNode(9))))))
# l2 = ListNode(9,ListNode(9,(ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9))))))))))
s = Solution
a = s.addTwoNumbers(s,l1,l2)
while a.next:
    print(a.val)
    a = a.next
print(a.val)