from typing import Tuple, TypeVar, Generic


class Node:
    """Create a node."""

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


T = TypeVar("T")


class LinkedList(Generic[T]):
    """Create a linked list."""

    length = 0

    def __init__(self):
        self.head = None
        self.tail = None

    def list_nodes(self) -> list:
        """List nodes."""
        current_node = self.head
        list_temp = []
        while current_node:
            list_temp.append(current_node.val)
            current_node = current_node.next
        return list_temp

    def append_node(self, val: T) -> Tuple[Node, T]:
        """Append a node.

        Args:
            val (T): Gereric value.
        """
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return new_node, val

        self.tail.next = new_node
        self.tail = self.tail.next
        self.length += 1
        return new_node, val

    def append_list(self, list_obj: list) -> bool:
        """Append a list.

        Args:
            list_obj (list): a list.
        """
        if not isinstance(list_obj, list) or not list_obj:
            print("=== The data must be a list type. ===")
            return False

        for i in list_obj:
            self.append_node(i)

        return True

    def delete_node_with_index(self, index: int) -> bool:
        """Delete a node with index.

        Args:
            index (int): a index value in a linked list.
        """
        msg = f"=== The node of the index({index}) is deleted. ==="

        if index > self.length:
            print(f"=== The index({index}) you input is out of bound. ===")
            return False

        position = 1
        current_node = self.head
        last_node = current_node

        if index == 1:
            self.head = self.head.next
            self.length -= 1
            print(msg)
            return True

        while position != index and current_node:
            last_node = current_node
            current_node = current_node.next
            position += 1

        last_node.next = current_node.next
        print(msg)
        self.length -= 1
        return True

    def delete_node_with_val(self, val: T) -> bool:
        """Delete a node with value.

        Args:
            val (T): Gereric value.
        """
        if not self.head:
            print("The linked list is empty.")
            return False

        current_node = self.head
        last_node = current_node
        msg = f"=== The node {val} is deleted. ==="

        if val == self.head.val:
            self.head = self.head.next
            self.length -= 1
            print(msg)
            return True

        while current_node and current_node.val != val:
            last_node = current_node
            current_node = current_node.next

        if current_node is None:
            print(
                f"=== The value {val} you want to delete does not exist in linked list. === "
            )
            return False

        last_node.next = current_node.next
        self.length -= 1
        print(msg)
        return True

    def find_node_with_val(self, val: T) -> bool:
        """find a node with value.

        Args:
            val (T): Gereric value.
        """
        if not self.head:
            print("The linked list is empty.")
            return False

        current_node = self.head
        last_node = current_node
        msg = f"=== The node value {val} is in linked list. ==="

        if val == self.head.val:
            print(msg)
            return True

        while current_node and current_node.val != val:
            last_node = current_node
            current_node = current_node.next

        if current_node is None:
            print(
                f"=== The value {val} you want to find does not exist in linked list. === "
            )
            return False

        print(msg)
        return True

if __name__ == "__main__":
    LN = LinkedList()
    print(f"The node '{LN.append_node("A")[1]}' is appended into linked list.")
    LN.append_list([2, 3, 4, 5])
    # LN.append_list(3)
    print(f"The linked list:{LN.list_nodes()}")
    LN.delete_node_with_index(2)
    print(f"The linked list:{LN.list_nodes()}")
    LN.delete_node_with_val("A")
    print(f"The linked list:{LN.list_nodes()}")
    LN.delete_node_with_val(6)
    print(f"The linked list:{LN.list_nodes()}")
    print(f"The node '{LN.append_node("A")[1]}' is appended into linked list.")
    print(f"The linked list:{LN.list_nodes()}")
    LN.find_node_with_val(3)
