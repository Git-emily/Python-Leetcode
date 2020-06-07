'''给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807 '''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        l3 = ListNode(0)  # 引用ListNode类定义类一个链表节点并赋给l3
        res = l3
        flag = 0
        while l1 and l2:
            temp = 0
            temp = l1.val + l2.val + flag
            l1 = l1.next
            l2 = l2.next
            temp_pre = ListNode(temp % 10)
            flag = int(temp / 10)
            res.next = temp_pre
            res = res.next

        if l1:
            while l1:
                temp = 0
                temp = l1.val + flag
                l1 = l1.next
                temp_pre = ListNode(temp % 10)
                flag = int(temp // 10)
                res.next = temp_pre
                res = res.next
        if l2:
            while l2:
                temp = 0
                temp = l2.val + flag
                l2 = l2.next
                temp_pre = ListNode(temp % 10)
                flag = int(temp // 10)
                res.next = temp_pre
                res = res.next

        if flag:
            res.next = ListNode(1)
        return l3.next

