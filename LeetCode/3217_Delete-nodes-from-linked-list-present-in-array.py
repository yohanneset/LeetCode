# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        set_ = set(nums)
        temp = ListNode()
        curr = temp

        while head:
            if head.val not in set_:
                curr.next= ListNode(head.val)
                curr = curr.next
            head = head.next

        return temp.next