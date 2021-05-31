class Hello():
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        print(self.args)
        print(self.kwargs)

hello = Hello("a","b","c", first_name="prithivi", last_name = "karthikeyan")