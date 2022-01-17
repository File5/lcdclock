from lcdclock.segment import Segment


class Char4Segment(Segment):
    pass


Char4Segment.S0 = Char4Segment(ord(' '), tuple(), False)
Char4Segment.S1 = Char4Segment(0, (
    0b01111,
    0b01111,
    0b01100,
    0b01100,
    0b01100,
    0b01100,
    0b01111,
    0b01111,
))
Char4Segment.S2 = Char4Segment(1, (
    0b11110,
    0b11110,
    0b00110,
    0b00110,
    0b00110,
    0b00110,
    0b11110,
    0b11110,
))
Char4Segment.S3 = Char4Segment(2, (
    0b01110,
    0b01110,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b01110,
    0b01110,
))
Char4Segment.S4 = Char4Segment(3, (
    0b01111,
    0b01111,
    0b01100,
    0b01100,
    0b01100,
    0b01100,
    0b00000,
    0b00000,
))
Char4Segment.S5 = Char4Segment(4, (
    0b01100,
    0b01100,
    0b01100,
    0b01111,
    0b01111,
    0b00000,
    0b00000,
    0b00000,
))
Char4Segment.S6 = Char4Segment(5, (
    0b00110,
    0b00110,
    0b00110,
    0b11110,
    0b11110,
    0b00000,
    0b00000,
    0b00000,
))
Char4Segment.S7 = Char4Segment(6, (
    0b00000,
    0b00000,
    0b00000,
    0b01110,
    0b01110,
    0b00000,
    0b00000,
    0b00000,
))
Char4Segment.S8 = Char4Segment(7, (
    0b00110,
    0b00110,
    0b00110,
    0b00110,
    0b00110,
    0b00000,
    0b00000,
    0b00000,
))
Char4Segment.ALL = [
    Char4Segment.S1, Char4Segment.S2, Char4Segment.S3, Char4Segment.S4,
    Char4Segment.S5, Char4Segment.S6, Char4Segment.S7, Char4Segment.S8
]


class Char4:
    def __init__(self, c, s_repr):
        self.c = c
        self.s_repr = s_repr

    @classmethod
    def from_char(cls, c):
        if c in '0123456789':
            if c == '0':
                s_repr = [
                    [Char4Segment.S4, Char4Segment.S8],
                    [Char4Segment.S5, Char4Segment.S6],
                ]
            elif c == '1':
                s_repr = [
                    [Char4Segment.S0, Char4Segment.S8],
                    [Char4Segment.S0, Char4Segment.S8],
                ]
            elif c == '2':
                s_repr = [
                    [Char4Segment.S3, Char4Segment.S2],
                    [Char4Segment.S5, Char4Segment.S7],
                ]
            elif c == '3':
                s_repr = [
                    [Char4Segment.S3, Char4Segment.S2],
                    [Char4Segment.S7, Char4Segment.S6],
                ]
            elif c == '4':
                s_repr = [
                    [Char4Segment.S5, Char4Segment.S8],
                    [Char4Segment.S0, Char4Segment.S8],
                ]
            elif c == '5':
                s_repr = [
                    [Char4Segment.S1, Char4Segment.S3],
                    [Char4Segment.S7, Char4Segment.S6],
                ]
            elif c == '6':
                s_repr = [
                    [Char4Segment.S1, Char4Segment.S3],
                    [Char4Segment.S5, Char4Segment.S6],
                ]
            elif c == '7':
                s_repr = [
                    [Char4Segment.S4, Char4Segment.S8],
                    [Char4Segment.S0, Char4Segment.S8],
                ]
            elif c == '8':
                s_repr = [
                    [Char4Segment.S1, Char4Segment.S2],
                    [Char4Segment.S5, Char4Segment.S6],
                ]
            elif c == '9':
                s_repr = [
                    [Char4Segment.S1, Char4Segment.S2],
                    [Char4Segment.S7, Char4Segment.S6],
                ]
            return cls(c, s_repr)
        elif c == ' ':
            return cls(c, [
                [Char4Segment.S0, Char4Segment.S0],
                [Char4Segment.S0, Char4Segment.S0],
            ])
        else:
            raise ValueError("unsupported char4")


class Char4String:
    def __init__(self, s, char4s):
        self.s = s
        self.char4s = char4s

    @classmethod
    def from_str(cls, s):
        char4s = []
        for c in s:
            c4 = Char4.from_char(c)
            char4s.append(c4)
        return cls(s, char4s)

    @property
    def lines(self):
        line1 = []
        line2 = []
        for c4 in self.char4s:
            line1 += c4.s_repr[0]
            line2 += c4.s_repr[1]
        return [line1, line2]

    def print(self, lcd):
        for line in self.lines:
            i = 0
            for s in line:
                lcd.write(s.addr)
                i += 1
            if i < 20:
                lcd.write_string('\r\n')