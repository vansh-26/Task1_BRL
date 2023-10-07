class A:
    def first_function(self):
        print("First")

class B(A):
     def second_function(self):
        print("Second")

class C(B):
     def third_function(self):
        print("Third")
        super(C, self).first_function()

class D(B):
     def fourth_function(self):
        print("Fourth")

class E(C, D):
   def fifth_function(self):
        print("That's it")


e = E()
e.first_function()
e.second_function()
e.third_function()
e.fourth_function()
e.fifth_function()