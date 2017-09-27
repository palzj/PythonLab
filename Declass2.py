class A():
    """Class A"""

    def __init__(self, sa):
        self.a = sa

    def Hia(self):
        print ("{0:12}:{1}".format(self.__doc__, self.a))


class B():
    """Class B"""

    def __init__(self):
        pass

    def Hib(self):
        print (self.__doc__,":", "hi b!")


class C(A,B):
    """Class C"""

    def __init__(self):
        A.__init__(self, "default for C")