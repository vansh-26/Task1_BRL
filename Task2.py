class A:
    def __init__(self):
        print("First")

class B(A):
     def __init__(self):
        print("second")
class C(B):
     def __init__(self):
        print("third")

class D(B):
     def __init__(self):
        print("fourth")

class E(C,D):
   def __init__(self):
        super(Fourth, self).__init__()
        print("that's it")

