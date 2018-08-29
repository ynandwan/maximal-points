#findPreSuc from - https://www.geeksforgeeks.org/inorder-predecessor-successor-given-key-bst/
#from IPython.core.debugger import Pdb


class Node:
    def __init__(self,k,v,lc = None, rc = None, parent = None):
        self.key = k
        self.val = v
        self.left = lc 
        self.right = rc 
        self.parent = parent 
        self.update_hb()
    
    def update_hb(self):
        lh,rh = 0,0
        if self.left:
            lh = self.left.height
        if self.right:
            rh = self.right.height

        self.height = 1 + max(lh,rh)
        self.balance = lh - rh 

    def is_imbalance(self):
        return (abs(self.balance) > 1)

    def is_leaf(self):
        return ((self.left is None) and (self.right is None))

    def is_left(self):
        return (self.parent and (self == self.parent.left))

    def is_right(self):
        return (self.parent and (self == self.parent.right))

    def search(self,k):
        if self.key == k:
            return self
        elif k < self.key and self.left:
            return self.left.search(k)
        elif k > self.key and self.right:
            return self.right.search(k)
        else:
            return None


    def find_successor(self):
        #assumes that self has a right child
        right = self.right
        left = right.left
        if left is None:
            return right

        while left.left:
            left = left.left
        #
        return left


        
    def inorder_traverse(self):
        result = []
        if self.left:
            result.extend(self.left.inorder_traverse())

        result.append(self.val)
        if self.right:
            result.extend(self.right.inorder_traverse())

        return result

    def display(self,level=0):
        if self.right:
            self.right.display(level + 1)
            print (('\t' * level), ('    /'))
 
        print (('\t' * level), self)
 
        if self.left:
            print( ('\t' * level), ('    \\'))
            self.left.display( level + 1)


    def __str__(self):
        "String representation."
        return '{}:{}:{}'.format(self.key,self.height,self.balance)
 
    def __repr__(self):
        "String representation."
        return str(self)



#debug = False 


class AVLTree:
    def __init__(self):
        self.root = None

    def insert_at(self,at_node,key,val,is_left = True, parent = None):
        if at_node is None:
            at_node =  Node(key,val,parent=parent)
            if is_left:
                parent.left = at_node
            else:
                parent.right = at_node
            #
            #if debug:
            #    print('inserted at leaf, start rebalance')
            self.rebalance(at_node)
            return 
        #
        if key < at_node.key:
            self.insert_at(at_node.left,key,val,True,at_node)
        elif key > at_node.key:
            self.insert_at(at_node.right, key, val, False, at_node)
            


    def rebalance(self,at_node):
        #if debug:
        #    print('reb',at_node)
        #this recursion starts from a leaf
        #we update the balance of the parent of at_node assuming at_node is balanced and updated
        #while inserting we stop as soon as we rotate once
        parent = at_node.parent
        #Pdb().set_trace()
        if parent is None:
            self.root = at_node 
            #if debug: 
            #    print('reb ret from root')
            return

        prev_ht = parent.height
        parent.update_hb()
        if parent.is_imbalance():
            parent = self.rotate(parent)
            if parent.parent is None:
                #if debug:
                #    print('reb, set root',at_node)
                self.root = parent
            
            new_ht = parent.height
            if prev_ht == new_ht:
                #if debug:
                #    print(' stop reb',at_node)
                return
            else:
                #print('continue even after one rotation',at_node,parent)
                self.rebalance(parent)
                #if debug:
                #    print('return reb after rot',at_node)
        else:
            self.rebalance(parent)
            #if debug:
            #    print('return reb',at_node)


    def rotate_left(self,z):
        y = z.right
        x = y.right
        T2 = y.left
        parent = z.parent
        is_left = z.is_left()
        is_right = z.is_right()

        z.right = T2
        if T2:
            T2.parent = z
        
        y.left = z
        z.parent = y

        y.parent = parent

        if is_left:
            parent.left = y
        elif is_right:
            parent.right = y

        
        z.update_hb()
        y.update_hb()
        return y

    def rotate_right(self, z):
        y = z.left
        x = y.left
        T3 = y.right
        parent  = z.parent
        is_left = z.is_left()
        is_right = z.is_right()

        z.left = T3
        if T3:
            T3.parent = z

        y.right = z
        z.parent = y

        y.parent = parent

        if is_left:
            parent.left = y
        elif is_right:
            parent.right = y

        z.update_hb()
        y.update_hb()
        return y



    def rotate(self,z):
        if z.balance > 0:
            y = z.left
        else:
            y = z.right

        if y.balance > 0:
            x = y.left
        else:
            x = y.right

        #do rotations with z, y and x

        if y.is_left():
            if x.is_left():
                return self.rotate_right(z)
            else:
                self.rotate_left(y)
                return self.rotate_right(z)
        else:
            if x.is_right():
                return self.rotate_left(z)
            else:
                self.rotate_right(y)
                return self.rotate_left(z)



    def insert(self,key, val):
        if self.root is None:
            self.root = Node(key,val)
            return 
        #
        self.insert_at(self.root, key, val)


    def delete(self,key):
        #Pdb().set_trace()
        if self.root is None:
            raise KeyError
        elif self.root.left is None and self.root.right is None:
            if self.root.key == key:
                del self.root
                self.root = None
                return 
            else:
                raise KeyError

        #root exists and has at least 1 child
        found_at = self.root.search(key)
        if found_at is None:
            raise KeyError

        #3 cases - 
        #case 1 - its a leaf
        #case 2 - has 1 child
        #case 3 - has 2 children

        #reduce case 3 to case 2 or case 1
        if found_at.left and found_at.right:
            #case 3 - two children
            suc = found_at.find_successor()
            found_at.key = suc.key
            found_at.val = suc.val
            found_at = suc
            #delete found_at which now has only 1 or 0 child

        #
        #in avl tree if a node has only one child then its ht is always 2
        child = None 
        if found_at.left:
            child = found_at.left
        elif found_at.right:
            child = found_at.right

        rebalance_at = None 
        if child:
            found_at.key = child.key 
            found_at.val = child.val
            found_at.left = None
            found_at.right = None
            del child
            rebalance_at = found_at

        else:
            #if found_at is a leaf node
            rebalance_at = found_at.parent
            if rebalance_at is None:
                #this has been handled above as well. shouldn't happen.
                return 
            is_left = found_at.is_left()
            is_right = found_at.is_right()
            if is_left:
                rebalance_at.left = None
            elif is_right:
                rebalance_at.right = None
            #
            del found_at
        #
        prev_ht = rebalance_at.height
        rebalance_at.update_hb()
        new_ht = rebalance_at.height
        if rebalance_at.is_imbalance():
            rebalance_at  = self.rotate(rebalance_at)
            if rebalance_at.parent is None:
                self.root = rebalance_at
            new_ht == rebalance_at.height 

        if prev_ht == new_ht:
            return
        else:
            self.rebalance(rebalance_at)

    def inorder_traverse(self):
        if self.root is None:
            return []

        return self.root.inorder_traverse()

    def display(self):
        if self.root is None:
            return
        
        self.root.display()


def rangeSearch(root, key1, key2):
    if root is None:
        return []
    #
    keys_in_left = []
    keys_in_right = []
    if key1 < root.key:
        keys_in_left = rangeSearch(root.left,key1,key2)
    if key2 > root.key:
        keys_in_right = rangeSearch(root.right,key1, key2)
    #
    rv = None
    if len(keys_in_left) > len(keys_in_right):
        keys_in_left.extend(keys_in_right)
        rv = keys_in_left
    else:
        keys_in_right.extend(keys_in_left)
        rv = keys_in_right

    if key1 <= root.key and key2 >= root.key:
        rv.append(root.key)
    #
    return rv




def findPreSuc(root, key , extractor):
    resetPreSuc()
    _findPreSuc(root,key,extractor)
    p,s = _findPreSuc.pre, _findPreSuc.suc
    resetPreSuc()
    return p,s 



def _findPreSuc(root, key, extractor):
    # Base Case
    if root is None:
        return
    # If key is smaller than root's key, go to left subtree
    if extractor(root) > key :
        _findPreSuc.suc = root 
        _findPreSuc(root.left, key, extractor)

    else: # go to right subtree
        _findPreSuc.pre = root 
        _findPreSuc(root.right, key, extractor)


def resetPreSuc():
    _findPreSuc.pre = None
    _findPreSuc.suc = None




if __name__ == "__main__":
    tree = AVLTree()
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    from random import randrange
    for key in data:
        tree.insert(key,-key)

    for key in [4,3]:
        tree.delete(key)

    print (tree.inorder_traverse())
    tree.display()
 

if False:
    import numpy as np
    np.random.seed(1)
    data = list(set(np.random.randint(100000, size = 10000)))
    from avl1 import *
    tree = AVLTree()
    for key in data:
        tree.insert(key,key)

    #
    np.random.seed(130)
    delete_ind = list(set(np.random.randint(len(data),size = 500)))
    for i in delete_ind:
        tree.delete(data[i])

