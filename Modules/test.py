class Bar:
    y = 'her'
    def __init__(self, x):
        self.x = x

    def Foo(self):
        print(self.y)


t = Bar('bla')
t.Foo()
