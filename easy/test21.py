'''
21. 合并两个有序链表
执行用时：40 ms, 在所有 Python3 提交中击败了85.23%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了15.35%的用户
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        r = l1 if l1.val < l2.val else l2
        r.next = self.mergeTwoLists(self,r.next,l1 if l1.val >= l2.val else l2)
        return r



if __name__ == '__main__':
    a = ListNode(1, ListNode(2, ListNode(3, None)))
    b = ListNode(2, ListNode(4, ListNode(5, None)))
    s = Solution
    r = s.mergeTwoLists(s,a,b)
    while r!=None:
        print(r.val)
        r = r.next