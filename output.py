class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_bst_from_level_order(values):
    if not values or values[0] == '-1':
        return None

    # Convert to integer and handle invalid input
    try:
        root = TreeNode(int(values[0]))
    except ValueError:
        return None

    queue = [root]
    index = 1

    while queue and index < len(values):
        current = queue.pop(0)

        if index < len(values) and values[index] != '-1':
            try:
                current.left = TreeNode(int(values[index]))
                queue.append(current.left)
            except ValueError:
                return None
        index += 1

        if index < len(values) and values[index] != '-1':
            try:
                current.right = TreeNode(int(values[index]))
                queue.append(current.right)
            except ValueError:
                return None
        index += 1

    return root

def findSecondLargest(bst):
    if not bst or (bst.left is None and bst.right is None):
        return [-1, -1]

    current = bst
    prev = None

    # Go to the rightmost node (largest)
    while current.right:
        prev = current
        current = current.right

    # If the largest node has a left subtree
    if current.left:
        current = current.left
        while current.right:
            current = current.right
        return [current.value, prev.value]
    else:
        # The largest node has no left subtree
        return [prev.value, -1] if prev else [-1, -1]

# Get input from stdin
bst_input = input().strip()
bst_nodes = bst_input.split()

# Build the BST from level order input
bst = build_bst_from_level_order(bst_nodes)

# Call the function to find the second largest
result = findSecondLargest(bst)

# Print the result in the required format
print(result)
