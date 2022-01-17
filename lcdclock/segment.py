class Segment:
    def __init__(self, addr, data, register=True):
        self.addr = addr
        self.data = data
        self.register = register