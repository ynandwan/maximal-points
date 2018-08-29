
class Point3D(object):
    def __init__(self,ind,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.ind = ind

    def __str__(self):
        return('{},{},{},{}'.format(self.ind,self.x, self.y, self.z))

    def __repr__(self):
        return (self.__str__())

class Point2D(object):
    def __init__(self,ind,x,y):
        self.x = x
        self.y = y
        self.ind = ind

    def dominates(self,p):
        return (self.x > p.x and self.y > p.y)

    def __str__(self):
        return('{},{},{}'.format(self.ind,self.x, self.y))

    def __repr__(self):
        return (self.__str__())


