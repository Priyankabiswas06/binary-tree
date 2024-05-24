class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return TreeNode(value)
        if value == node.value:
            print(f"Duplicate entry '{value}' ignored")
            return node  # Duplicate entry, do nothing
        elif value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        return node

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            node.value = self._min_value_node(node.right).value
            # Delete the inorder successor
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def display(self):
        print("Inorder Traversal: ", self.inorder_traversal())
        print("Preorder Traversal:", self.preorder_traversal())
        print("Postorder Traversal:", self.postorder_traversal())

def main():
    bst = BinarySearchTree()
    elements = [50, 30, 20, 40, 70, 60, 80]

    # Inserting elements
    for el in elements:
        bst.insert(el)

    # Attempting to insert duplicate
    bst.insert(70)

    # Display the tree
    bst.display()

    # Search for elements
    print("Search for 40:", bst.search(40) is not None)
    print("Search for 100:", bst.search(100) is not None)

    # Delete elements
    bst.delete(20)
    bst.delete(30)
    bst.delete(50)

    # Display the tree after deletion
    bst.display()

if __name__ == "__main__":
    main()
