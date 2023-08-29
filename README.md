# pynternal_nodes

A single function that returns the number of internal nodes in a generic tree composed of consecutive integers.

## Usage

This function calculates the number of internal nodes on a tree.
The tree must be represented by a list `L` such as `L[i]` identifies the parent of `i` (the root has no parent and is denoted with -1).

For example:

```python
tree = [4, 4, 1, 5, -1, 4, 5]
internal_nodes = find_internal_nodes_num(tree)
print(f"Number of internal nodes: {internal_nodes}")
# Prints: Number of internal nodes: 3
```

The function asumes that the tree is valid
A tree is valid if:

- All the elements in the list `L` are integers from -1 to `len(L) - 1` 
- There is only one root node, thos means that the list `L` contains the value -1 at some index and can only have one occurrence of -1 within it
- The tree is asyclic
- There is a unique path between any two nodes in the graph

The function has a time complexity of O(n), where 'n' represents the number of nodes in the tree. Additionally, the function has a memory complexity of O(n), as it requires memory proportional to the number of nodes in the tree.

### Tests

You can run the tests from the root dir running the following command:

```bash
PYTHONPATH=${PWD} pytest
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## 
For any questions or feedback, feel free to contact me at mfvazquez@fi.uba.ar.
