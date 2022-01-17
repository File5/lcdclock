from lcdclock.segment import Segment


class Char9Segment(Segment):
    pass


Char9Segment.S0 = Char9Segment(ord(' '), tuple(), False)
Char9Segment.S1 = Char9Segment(0, (
    0b00000,
    0b00000,
    0b11111,
    0b11111,
    0b11111,
    0b00000,
    0b00000,
    0b00000,
))
Char9Segment.S2 = Char9Segment(1, (
    0b00000,
    0b00000,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
))
Char9Segment.S3 = Char9Segment(2, (
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b00000,
    0b00000,
    0b00000,
))
Char9Segment.S4 = Char9Segment(3, (
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
    0b01110,
))
Char9Segment.S5 = Char9Segment(4, (
    0b00000,
    0b00000,
    0b01110,
    0b01110,
    0b01110,
    0b00000,
    0b00000,
    0b00000,
))
Char9Segment.ALL = [
    Char9Segment.S1, Char9Segment.S2, Char9Segment.S3, Char9Segment.S4, Char9Segment.S5
]


class Char9:
    def __init__(self, c, s_repr):
        self.c = c
        self.s_repr = s_repr

    @classmethod
    def from_char(cls, c):
        if c in '0123456789':
            if c == '0':
                s_repr = [
                    [Char9Segment.S2, Char9Segment.S1, Char9Segment.S2],
                    [Char9Segment.S4, Char9Segment.S0, Char9Segment.S4],
                    [Char9Segment.S3, Char9Segment.S1, Char9Segment.S3],
                ]
            elif c == '1':
                s_repr = [
                    [Char9Segment.S0, Char9Segment.S0, Char9Segment.S2],
                    [Char9Segment.S0, Char9Segment.S0, Char9Segment.S4],
                    [Char9Segment.S0, Char9Segment.S0, Char9Segment.S3],
                ]
            elif c == '2':
                s_repr = [
                    [Char9Segment.S5, Char9Segment.S1, Char9Segment.S2],
                    [Char9Segment.S2, Char9Segment.S1, Char9Segment.S3],
                    [Char9Segment.S3, Char9Segment.S1, Char9Segment.S5],
                ]
            elif c == '3':
                s_repr = [
                    [Char9Segment.S5, Char9Segment.S1, Char9Segment.S2],
                    [Char9Segment.S5, Char9Segment.S1, Char9Segment.S4],
                    [Char9Segment.S5, Char9Segment.S1, Char9Segment.S3],
                ]
            elif c == '4':
                s_repr = [
                    [Char9Segment.S2, Char9Segment.S0, Char9Segment.S2],
                    [Char9Segment.S3, Char9Segment.S1, Char9Segment.S4],
                    [Char9Segment.S0, Char9Segment.S0, Char9Segment.S3],
                ]
            elif c == '5':
                s_repr = [
                    [Char9Segment.S2, Char9Segment.S1, Char9Segment.S5],
                    [Char9Segment.S3, Char9Segment.S1, Char9Segment.S2],
                    [Char9Segment.S5, Char9Segment.S1, Char9Segment.S3],
                ]
            elif c == '6':
                s_repr = [
                    [Char9Segment.S2, Char9Segment.S1, Char9Segment.S5],
                    [Char9Segment.S4, Char9Segment.S1, Char9Segment.S2],
                    [Char9Segment.S3, Char9Segment.S1, Char9Segment.S3],
                ]
            elif c == '7':
                s_repr = [
                    [Char9Segment.S5, Char9Segment.S1, Char9Segment.S2],
                    [Char9Segment.S0, Char9Segment.S0, Char9Segment.S4],
                    [Char9Segment.S0, Char9Segment.S0, Char9Segment.S3],
                ]
            elif c == '8':
                s_repr = [
                    [Char9Segment.S2, Char9Segment.S1, Char9Segment.S2],
                    [Char9Segment.S4, Char9Segment.S1, Char9Segment.S4],
                    [Char9Segment.S3, Char9Segment.S1, Char9Segment.S3],
                ]
            elif c == '9':
                s_repr = [
                    [Char9Segment.S2, Char9Segment.S1, Char9Segment.S2],
                    [Char9Segment.S3, Char9Segment.S1, Char9Segment.S4],
                    [Char9Segment.S5, Char9Segment.S1, Char9Segment.S3],
                ]
            return cls(c, s_repr)
        elif c == ' ':
            return cls(c, [
                    [Char9Segment.S0],
                    [Char9Segment.S0],
                    [Char9Segment.S0],
            ])
        else:
            raise ValueError("unsupported char9")


class Char9String:
    def __init__(self, s, char9s):
        self.s = s
        self.char9s = char9s

    @classmethod
    def from_str(cls, s):
        char9s = []
        for c in s:
            c9 = Char9.from_char(c)
            char9s.append(c9)
        return cls(s, char9s)

    @property
    def lines(self):
        line1 = []
        line2 = []
        line3 = []
        for c9 in self.char9s:
            line1 += c9.s_repr[0]
            line2 += c9.s_repr[1]
            line3 += c9.s_repr[2]
        return [line1, line2, line3]

    def print(self, lcd):
        for line in self.lines:
            i = 0
            for s in line:
                lcd.write(s.addr)
                i += 1
            if i < 20:
                lcd.write_string('\r\n')