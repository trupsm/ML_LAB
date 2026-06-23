def alphabeta(depth, node, isMax, values, max_depth, alpha, beta):
    # Leaf node reached
    if depth == max_depth:
        return values[node]
    if isMax:
        best = float('-inf')
        for i in range(2):
            value = alphabeta(depth + 1,node * 2 + i,False,values,max_depth,alpha,beta)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:  # Pruning condition
                break
        return best

    else:
        best = float('inf')
        for i in range(2):
            value = alphabeta(depth + 1,node * 2 + i,True,values,max_depth,alpha,beta)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha: # Pruning condition
                break
        return best
# ---------------- INPUT ----------------
tree_depth = int(input("Enter depth of tree: "))
leaf_nodes = 2 ** tree_depth
print(f"Enter {leaf_nodes} leaf node values:")
values = list(map(int, input().split()))
player = input("Enter starting player (MAX/MIN): ").upper()
isMax = True if player == "MAX" else False
# Function Call
result = alphabeta(0,0,isMax,values,tree_depth,float('-inf'),float('inf'))
print("Optimal Value =", result)