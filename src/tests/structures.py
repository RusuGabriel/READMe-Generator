class Token:
    def __init__(self, question, multiline, start, end):
        self.multiline = multiline
        self.question = question
        self.start = start
        self.end = end
        super().__init__()

    def __str__(self):
        return '(Q:{0:} ,M:{1:} ,Start: {2:} ,End: {3:} )'.format(self.question, self.multiline, self.start, self.end)
