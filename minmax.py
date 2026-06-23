def minimax(depth, node, isMax, values, max_depth):
    # Leaf node reached
    if depth == max_depth:
        return values[node]
    if isMax:
        return max(
            minimax(depth + 1, node * 2, False, values, max_depth),
            minimax(depth + 1, node * 2 + 1, False, values, max_depth)
        )
    else:
        return min(
            minimax(depth + 1, node * 2, True, values, max_depth),
            minimax(depth + 1, node * 2 + 1, True, values, max_depth)
        )
# User Input
depth = int(input("Enter depth of tree: "))
leaf_nodes = 2 ** depth
print(f"Enter {leaf_nodes} leaf node values:")
values = list(map(int, input().split()))
player = input("Enter starting player (MAX/MIN): ").upper()
isMax = True if player == "MAX" else False
# Function Call
result = minimax(0, 0, isMax, values, depth)
print("Optimal Value =", result)