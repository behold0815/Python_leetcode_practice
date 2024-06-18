import pytest
from List_Node import *

test_list = [2, 3, 4]


def test_list_nodes():
    test = LinkedList()
    test.append_list(test_list)
    assert all([a == b for a, b in zip(test.list_nodes(), test_list)])


def test_append_node():
    test = LinkedList()
    assert test.append_node(5)[1] == 5
    assert test.append_node("A")[1] == "A"


@pytest.mark.test
@pytest.mark.parametrize(argnames="not_list", argvalues=[("A"), (5), ((3, 7, 0))])
def test_append_list(not_list):
    test = LinkedList()
    assert test.append_list(not_list) == False
    assert test.append_list(test_list) == True


# TODO:test_delete_node_with_index
# TODO:查coverage指令
@pytest.mark.test
def test_delete_node_with_index():
    test = LinkedList()
    test.append_list(test_list)
    assert test.delete_node_with_index(6) == False
    assert test.delete_node_with_index(3) == True
    assert test.delete_node_with_index(1) == True
