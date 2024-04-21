class NextRequest:

    def __init__(self):
        self.i = 1

    def next_re(self):
        for _ in range(1, 20):
            yield _
            self += 1
