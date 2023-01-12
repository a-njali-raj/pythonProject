class animal:
    def speak(self):
        print("Animal Speaks.")
class dog(animal):
    def bark(self):
        print("Dog barks.")
class cow(animal):
    def cry(self):
        print("Cow cries.")
d=dog()
d.speak()
d.bark()
b=cow()
b.speak()
b.cry()
