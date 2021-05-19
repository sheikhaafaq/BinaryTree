class Node:
    def __init__(self):
        self.data = input("Enter Data: ")
        self.left = None
        self.right = None
        
    def addNode(self):
        print("LEFT")
        self.left = Node()
        print("RIGHT")
        self.right = Node()
    
    def preOrder(self):
        if self.data:
            print(self.data)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()
        
    def postOrder(self):
        if self.left:
            self.left.postOrder()
            
        if self.right:
            self.right.postOrder()
        
        if self.data:
            print(self.data)
    
    def inOrder(self):
        if self.left:
            self.left.inOrder()
        
        if self.data:
            print(self.data)
    
        if self.right:
            self.right.inOrder()
       

#Create Tree
print("Root Node")
root = Node()

#Addnewnode
print("root")
root.addNode()
print("root->left")
root.left.addNode()
print("root->right")
root.right.addNode()

#Traversing
print("PreOrder Traversing")
root.preOrder()
print("PostOrder Traversing")
root.postOrder()
print("inOrder Traversing")
root.inOrder()