class MClass():
    """Test for Class Property"""

    @property
    def Val(self):return self.__val

    @Val.setter
    def Val(self, value):self.__val = value

    @Val.deleter
    def Val(self):del self.__val

    def GetStr(self):
        return "{0}{1}{2}".format(self.__doc__, ":", self.Val)
