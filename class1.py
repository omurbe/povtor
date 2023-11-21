class Hello:
    def __init__(self, name):
        self.name = name


class Hi(Hello):
    def __init__(self, name):
        Hello.__init__(self, name)

    def __str__(self):
        return self.name
