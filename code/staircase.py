import os,random,math
import avl
class Staircase2D(object):
    def __init__(self):
        self.maximal_points = avl.avltree()
        self.size = 0

    def update(self, p):
        #print(self.maximal_points.inorder_traverse())
        #if self.size > 0:
        #    self.maximal_points.display()
        #
        if self.size == 0:
            self.maximal_points.insert(p.x,p)
            self.size += 1
            return True
        """
        if self.size == 1:
            if self.maximal_points.node.val.dominates(p):
                return False
            else:
                self.maximal_points.insert(p.x,p)
                self.size += 1
                return True
        """
        #
        prex,sucx =  avl.findPreSuc(self.maximal_points,p.x, lambda node: node.key)
        #if sucx is None:
        #    #highest x coordinate
        #    self.maximal_points.insert(p.x,p)
        #    self.size += 1
        #    return True

        if sucx is not None and sucx.val.dominates(p):
            return False
        
        #we will always return true post this point
        if prex is None:
            self.maximal_points.insert(p.x,p)
            self.size += 1
            return True
        #
        prey,sucy = avl.findPreSuc(self.maximal_points, -1*p.y, lambda node: -1*node.val.y)
        if sucy is None:
            self.maximal_points.insert(p.x,p)
            self.size += 1
            return True
        #

        #have to delete all points between sucy and prex(inclusive)
        #find all points between sucy and prex and delete them(inclusive)
        keys_to_delete = avl.rangeSearch(self.maximal_points,sucy.key, prex.key)
        for key in keys_to_delete:
            self.maximal_points.delete(key)
            self.size -= 1
        #
        #add given point
        self.maximal_points.insert(p.x,p)
        self.size += 1
        return True

        
