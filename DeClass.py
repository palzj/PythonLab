class A():
    """Class A"""
    
    def __init__(self,sa):
        self.a = sa
    
    def Hi(self):
        print self.__doc__, ":", self.a
     
        
class B(A):
    """Class B"""
    def __init__(self,sb):
        A.__init__(self,sb)


class C(B):
    """Class C"""

    def __init__(self):
        B.__init__(self,"default for C")

