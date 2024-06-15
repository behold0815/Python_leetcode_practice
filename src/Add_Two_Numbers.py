l1 = [2,4,3]
l2 = [5,6,4]
output = []

carrier = 0

for index in range(len(l1)):
    temp = l1[index] + l2[index] + carrier
    carrier, mod = divmod(temp, 10)
    output.append(mod)

# print(output)
# class ListNode:
#     def __init__(self, data = 0, next = None):
#         self._data = data
#         self._next = next
#         return

# output = []
# carrier = 0
# lc1 = [2,4,3]
# lc2 = [5,6,4]

# head = ListNode()
# tail = head

# for node in lc1:
    # if l1 is None:
    #     l1 = ListNode(node)
    #     head = l1
    #     tail = l1
    #     continue

    # new_node = ListNode(node)
    # tail = new_node
    # tail._next = None

