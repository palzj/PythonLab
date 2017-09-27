# -*- coding: utf-8 -*-

def main():
    """The enter point function"""
    ## test Hello world
    #   from  Hello import Hello
    #       h = Hello()
    #       h.Hello()

    ## test user defined iterator
    # from  MIterator import Data
    # d = Data(1, 2, 3)
    # for x in d: print x

    ## test single Derived class
    # from DeClass import A,B,C
    #
    # A("a call").Hi()
    #
    # b = B('c call')
    # b.Hi()
    #
    # C().Hi()

    # # test multi-Derived class
    # from Declass2 import A,B,C
    # A("defalut for c").Hia()
    # B().Hib()
    # c = C()
    # c.Hia()
    # c.Hib()

    # # test for Mclass
    # from MClass import MClass
    # m = MClass()
    # m.Val = "you"
    # print m.GetStr()
    #
    # m.Val = "love"
    # print m.GetStr()

    # # Test for TArcCpy
    # from TArcCpy import Test
    # Test()

    # Test for TransportationEvalute
    from TransportationEvaluate import ExcuteEvaluate
    lca = r"c:\users\lengyue\desktop\数据\520201zsq.gdb\LCA"
    lrrl = r"c:\users\lengyue\desktop\数据\520201zsq.gdb\LRRL"
    lrdl = r"c:\users\lengyue\desktop\数据\520201zsq.gdb\LRDL"
    ExcuteEvaluate(lca,lrrl,lrdl)

    

























if __name__ == '__main__':
    main()


