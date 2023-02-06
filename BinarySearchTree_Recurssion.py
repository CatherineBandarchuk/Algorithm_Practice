class TreeNode:
    def __init__(self, key, value = None):
        if value == None:
            value = key

        self.value = value
        self.key = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key,value)
        else:
            current = self.root
            parent = None
            while current!= None:
                parent = current
                if current.key > key:
                    current = current.left
                    #return self.add(current.left, key, value)
                else:
                    current = current.right
                    #return self.add(current.right, key, value)
            if parent.key > key:
                parent.left = TreeNode(key, value)
            else:
                parent.right = TreeNode(key, value)

    def add2(self, key, value = None):
        new_node = TreeNode(key, value)
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while current:
            if key < current.key:
                if not current.left:
                    current.left = new_node
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    return
                current = current.right

    def add_helper(self, current, node):
        if node.key < current.key:
            if not current.left:
                current.left = node
                return
            self.add_helper(current.left, node)
        else:
            if not current.right:
                current.right = node
                return
            self.add_helper(current.right, node)

    def add_recursion(self, key, value = None):
        newNode = TreeNode(key, value)
        if not self.root: 
            self.root = newNode
        else:
            self.add_helper()
        return self.add_helper(self.root, newNode)


    def helper_find_recursive(self, current, key):
        if not current:
            return None
        elif key == current.key:
            return current.value
        elif key < current.key:
            return self.helper_find_recursive(current.left, key)
        else:
            return self.helper_find_recursive(current.right, key)       

    def find_recursive(self, key):
        return self.helper_find_recursive(self.root, key)

    def find_iterative(self, key):
        current = self.roof
        if not current: 
            return None

        while (key != current.key) or (not current.left and not current.right):
            if key <= current.key:
                current = current.left
            else:
                current = current.right
        return current.value

    
    def delete(key, value):
        pass

newTree = Tree()
print(newTree.root == None)
newTree.add(5)
newTree.add(7)
print(newTree.root.key == 5)
print(newTree.root.right.key == 7)



