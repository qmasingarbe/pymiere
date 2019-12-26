# from pymiere import Pymiere
#
# pymiere = Pymiere()
#
# print(pymiere.eval_script("""$._pymiere.generateId()"""))

class A(object):
    def myclass(self):
        print(self.__class__.__name__)

class B(A):
    pass

B().myclass()