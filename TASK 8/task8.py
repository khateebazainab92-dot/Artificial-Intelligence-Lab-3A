# Minimax Algorithm Implementation

def minimax(depth, nodeIndex, isMaximizingPlayer, values, height):
    # Base case: leaf node reached
    if depth == height:
        return values[nodeIndex]

    if isMaximizingPlayer:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, height)
        )

# Example values (leaf nodes of game tree)
values = [3, 5, 6, 9, 1, 2, 0, -1]

import math
height = int(math.log2(len(values)))

# Call minimax
result = minimax(0, 0, True, values, height)

print("The optimal value is:", result)