from typing import List


def find_internal_nodes_num(tree: List[int]) -> int:
    tree = set(tree)
    tree.discard(-1)
    return len(tree)
