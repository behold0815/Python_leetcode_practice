from typing import TypeVar, Generic

class Node:
    """Create a node."""
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

T = TypeVar('T')

class LinkedList(Generic[T]):
    """Create a linked list."""
    length = 0

    def __init__(self):
        self.head = None
        self.tail = None

    def list_nodes(self):
        """List nodes."""
        current_node = self.head
        list_temp = []
        while current_node:
            list_temp.append(current_node.val)
            current_node = current_node.next
        print(f"The linked list:{list_temp}")

    def append_node(self, val: T):
        """Append a node,

        Args:
            val (T): Gereric value.
        """
        new_node = Node(val)
        msg = f"The node '{val}' is appended into linked list."
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            print(msg)
            return

        self.tail.next = new_node
        self.tail = self.tail.next
        self.length += 1
        print(msg)

    def append_list(self, list_obj: list):
        """Append a list.

        Args:
            list_obj (list): a list.
        """
        if not isinstance(list_obj, list):
            raise TypeError("=== The data must be a list type. ===")
        for i in list_obj:
            self.append_node(i)

    def delete_node_with_index(self, index: int):
        """Delete a node with index.

        Args:
            index (int): a index value in a linked list.
        """
        msg = f"=== The node of the index({index}) is deleted. ==="

        if index > self.length:
            print("=== The index you input is out of bound. ===")
            return

        position = 1
        current_node = self.head
        last_node = current_node

        if index == 1:
            self.head = self.head.next
            self.length -= 1
            print(msg)
            return

        while position != index and current_node:
            last_node = current_node
            current_node = current_node.next
            position += 1

        last_node.next = current_node.next
        print(msg)
        self.length -= 1

    def delete_node_with_val(self, val: T):
        """Delete a node with value.

        Args:
            val (T): Gereric value.
        """
        current_node = self.head
        last_node = current_node
        msg = f"=== The node {val} is deleted. ==="

        if val == self.head.val:
            self.head = self.head.next
            self.length -= 1
            print(msg)
            return

        while current_node and current_node.val != val:
            last_node = current_node
            current_node = current_node.next

        if current_node is None:
            print("=== The value you want to delete does not exist in linked list. === ")
        else:
            last_node.next = current_node.next
            print(msg)
            self.length -= 1

# TODO:寫單元測試 
if __name__ == "__main__":
    LN = LinkedList()
    LN.append_node("A")
    LN.append_list([2,3,4,5])
    LN.list_nodes()
    LN.delete_node_with_index(3)
    LN.delete_node_with_val("A")
    LN.list_nodes()
