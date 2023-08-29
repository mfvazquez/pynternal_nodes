from src.pynternal_nodes import find_internal_nodes_num


def test_find_internal_nodes_num_basic_tree():
    """
            4
         /  |  \
        1   0   5
       /       / \
      2       6   3
    """

    tree = [4, 4, 1, 5, -1, 4, 5]
    assert find_internal_nodes_num(tree) == 3


def test_find_internal_nodes_num_smaller_tree():
    """
            4
         /  |  \
        1   0   5
           / \
          2   3
    """

    tree = [4, 4, 5, 5, -1, 4, 5]
    assert find_internal_nodes_num(tree) == 2


def test_find_internal_nodes_num_bigger_tree():

    """
               4
            /  |  \
           1   0   5
          /    |  / \
         2     7 6   3
    """

    tree = [4, 4, 1, 5, -1, 4, 5, 7]
    assert find_internal_nodes_num(tree) == 4


def test_find_internal_nodes_num_piramid():
    """
             4
           /   \
          1     0
         /       \
        2         3
    """

    tree = [4, 4, 1, 0, -1]
    assert find_internal_nodes_num(tree) == 3


def test_find_internal_nodes_num_one_node():
    """
        0
    """

    tree = [-1]
    assert find_internal_nodes_num(tree) == 0


def test_find_internal_nodes_num_linear_tree():
    """
        4
        |
        3
        |
        2
        |
        1
        |
        0
    """

    tree = [1, 2, 3, 4, -1]
    assert find_internal_nodes_num(tree) == 4


def test_find_internal_nodes_num_empty_tree():
    assert find_internal_nodes_num([]) == 0


def test_find_internal_nodes_num_two_nodes():
    """
        0
        |
        1
    """

    tree = [-1, 0]
    assert find_internal_nodes_num(tree) == 1


def test_find_internal_nodes_num_large_linear_tree():
    """
      999999
        |
        3
        |
       ...
        |
        1
        |
        0
    """
    tree = [i for i in range(-1, 1000000)]
    assert find_internal_nodes_num(tree) == 1000000


def test_find_internal_nodes_num_large_tree():
    """
               499999
              /      \
           499998   500000
            /          \
          ...          ...
          /              \
         1             999998
        /                 \
       0                999999
    """
    left = [i for i in range(1, 500000)]
    right = [i for i in range(499999, 1000000)]
    tree = left + [-1] + right
    assert find_internal_nodes_num(tree) == 999999
