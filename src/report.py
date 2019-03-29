class Report(object):

    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def generate(self):
        raise NotImplementedError("Not implemented.")
