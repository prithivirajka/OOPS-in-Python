#for declaring private methods
class Hello():
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.a = 10
        self._b = 20
        self.__c = 30 

    def public_method(self):
        print(self.args)
        print(self.kwargs)
        print(self.__c) 
        print("inside public method")
        self.__private_method()


    def __private_method(self):
        print("inside private method")

hello = Hello("a","b","c", first_name="prithivi", last_name = "karthikeyan")
print(hello.a)
print(hello._b)
hello.public_method()