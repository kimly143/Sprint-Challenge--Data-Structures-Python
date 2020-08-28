class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value: 
            if self.left: # we have a left node
                self.left.insert(value)
            else: # it doesnt have a left node yet, we create a new node for it
                self.left = BSTNode(value)
        else:
            if self.right: # we have a right node
                self.right.insert(value)
            else: # it doesnt have a right node, we create a new node for it
                self.right = BSTNode(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value and self.left: #left
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
        return False


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
