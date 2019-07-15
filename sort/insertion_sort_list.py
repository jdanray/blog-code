class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# given the head of a linked list,
# perform an insertion sort on the linked list
def insertion_sort(head):
	if not head:
		return None
		
	node1 = head.next
	while node1:
		node2 = head
		while node2.val < node1.val:
			node2 = node2.next
			
		oldval = node1.val
		while node2 != node1:
			oldval, node2.val = node2.val, oldval
			node2 = node2.next
		node1.val = oldval
			
		node1 = node1.next
			
	return head
