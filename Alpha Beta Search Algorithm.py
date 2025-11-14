from typing import Any, List, Tuple, Union

Leaf = int
Node = Union[Leaf, List["Node"]]

def alphabeta(node: Node,
              maximizing: bool,
              alpha: float = float("-inf"),
              beta: float = float("inf"),
              visited: List[Leaf] = None,
              pruned: List[Leaf] = None) -> Tuple[float, List[Leaf], List[Leaf]]:

    if visited is None:
        visited = []
    if pruned is None:
        pruned = []

    if not isinstance(node, list):
        visited.append(node)
        return node, visited, pruned

    if maximizing:
        value = float("-inf")
        for child in node:
            if value >= beta:
                def gather_leaves(n):
                    if not isinstance(n, list):
                        return [n]
                    s = []
                    for c in n:
                        s += gather_leaves(c)
                    return s
                pruned += gather_leaves(child)
                break

            child_val, visited, pruned = alphabeta(child, False, alpha, beta, visited, pruned)
            if child_val > value:
                value = child_val
            if value > alpha:
                alpha = value
        return value, visited, pruned

    else:
        value = float("inf")
        for child in node:
            if value <= alpha:
                def gather_leaves(n):https://github.com/Mithun-M2004/AI/tree/main
                    if not isinstance(n, list):
                        return [n]
                    s = []
                    for c in n:
                        s += gather_leaves(c)
                    return s
                pruned += gather_leaves(child)
                break

            child_val, visited, pruned = alphabeta(child, True, alpha, beta, visited, pruned)
            if child_val < value:
                value = child_val
            if value < beta:
                beta = value
        return value, visited, pruned


tree = [
    [
        [ [21, 5], [15, 11] ],
        [ [12, 8], [9, 13] ]
    ],
    [
        [ [5, 12], [13, 12] ],
        [ [13, 14], [7, 10] ]
    ]
]

if __name__ == "__main__":
    value, visited, pruned = alphabeta(tree, maximizing=True)
    print("Minimax value at root:", value)
    print("Leaves visited (in order):", visited)
    print("Leaves pruned (not visited):", pruned)
