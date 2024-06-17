import pytest
from add_two import add_two


def test_add_two():
    assert add_two(2, 3) == 5
