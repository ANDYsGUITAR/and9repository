class Parent():
    def altered(self):
        print("Parent altered()")
class Child(Parent):
    def altered(self):
        print("Child,before altered()")
        super(Child, self).altered()
        print("Child, after altered()")

dad = Parent()
son = Child()
dad.altered()
son.altered()
