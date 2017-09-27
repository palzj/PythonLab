class Hello:
    def Hello(self):
        print self.content

    def __init__(self):
        self.content = 'hello world!'

    def __str__(self):
        return  'the string is:' + self.content