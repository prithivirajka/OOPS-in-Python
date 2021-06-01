class Hello():
    def __init__(self, *args, **kwargs): # To know the usage of variables and dictionaries in classes
        self.args = args
        self.kwargs = kwargs
        print(self.args)
        print(self.kwargs)

hello = Hello("a","b","c", first_name="prithivi", last_name = "karthikeyan")