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


@pytest.mark.parametrize(argnames="not_list", argvalues=[("A"), (5), ((3, 7, 0))])
def test_append_list(not_list):
    test = LinkedList()
    assert test.append_list(not_list) == False
    assert test.append_list(test_list) == True


def test_delete_node_with_index():
    test = LinkedList()
    test.append_list(test_list)
    assert test.delete_node_with_index(6) == False
    assert test.delete_node_with_index(3) == True
    assert test.delete_node_with_index(1) == True


def test_delete_node_with_val():
    test = LinkedList()
    test.append_node(5)
    assert test.delete_node_with_val(6) == False
    assert test.delete_node_with_val(5) == True
    assert test.delete_node_with_val(5) == False
    test.append_list(test_list)
    assert test.delete_node_with_val(4) == True


@pytest.mark.test
def test_find_node_with_val():
    test = LinkedList()
    test.append_node(5)
    assert test.find_node_with_val(6) == False
    assert test.find_node_with_val(5) == True
