from datetime import datetime
import time

from RPLCD.i2c import CharLCD


class Segment:
    def __init__(self, addr, data, register=True):
        self.addr = addr
        self.data = data
        self.register = register


Segment.S0 = Segment(ord(' '), tuple(), False)
Segment.S1 = Segment(0, (
    0b01111,
    0b01111,
    0b01100,
    0b01100,
    0b01100,
    0b01100,
    0b01111,
    0b01111,
))
Segment.S2 = Segment(1, (
    0b11110,
    0b11110,
    0b00110,
    0b00110,
    0b00110,
    0b00110,
    0b11110,
    0b11110,
))
Segment.S3 = Segment(2, (
    0b01110,
    0b01110,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b01110,
    0b01110,
))
Segment.S4 = Segment(3, (
    0b01111,
    0b01111,
    0b01100,
    0b01100,
    0b01100,
    0b01100,
    0b00000,
    0b00000,
))
Segment.S5 = Segment(4, (
    0b01100,
    0b01100,
    0b01100,
    0b01111,
    0b01111,
    0b00000,
    0b00000,
    0b00000,
))
Segment.S6 = Segment(5, (
    0b00110,
    0b00110,
    0b00110,
    0b11110,
    0b11110,
    0b00000,
    0b00000,
    0b00000,
))
Segment.S7 = Segment(6, (
    0b00000,
    0b00000,
    0b00000,
    0b01110,
    0b01110,
    0b00000,
    0b00000,
    0b00000,
))
Segment.S8 = Segment(7, (
    0b00110,
    0b00110,
    0b00110,
    0b00110,
    0b00110,
    0b00000,
    0b00000,
    0b00000,
))
Segment.ALL = [
    Segment.S1, Segment.S2, Segment.S3, Segment.S4,
    Segment.S5, Segment.S6, Segment.S7, Segment.S8
]


def register(lcd, segments):
    for s in segments:
        lcd.create_char(s.addr, s.data)


class Char4:
    def __init__(self, c, s_repr):
        self.c = c
        self.s_repr = s_repr

    @classmethod
    def from_char(cls, c):
        if c in '0123456789':
            if c == '0':
                s_repr = [
                    [Segment.S4, Segment.S8],
                    [Segment.S5, Segment.S6],
                ]
            elif c == '1':
                s_repr = [
                    [Segment.S0, Segment.S8],
                    [Segment.S0, Segment.S8],
                ]
            elif c == '2':
                s_repr = [
                    [Segment.S3, Segment.S2],
                    [Segment.S5, Segment.S7],
                ]
            elif c == '3':
                s_repr = [
                    [Segment.S3, Segment.S2],
                    [Segment.S7, Segment.S6],
                ]
            elif c == '4':
                s_repr = [
                    [Segment.S5, Segment.S8],
                    [Segment.S0, Segment.S8],
                ]
            elif c == '5':
                s_repr = [
                    [Segment.S1, Segment.S3],
                    [Segment.S7, Segment.S6],
                ]
            elif c == '6':
                s_repr = [
                    [Segment.S1, Segment.S3],
                    [Segment.S5, Segment.S6],
                ]
            elif c == '7':
                s_repr = [
                    [Segment.S4, Segment.S8],
                    [Segment.S0, Segment.S8],
                ]
            elif c == '8':
                s_repr = [
                    [Segment.S1, Segment.S2],
                    [Segment.S5, Segment.S6],
                ]
            elif c == '9':
                s_repr = [
                    [Segment.S1, Segment.S2],
                    [Segment.S7, Segment.S6],
                ]
            return cls(c, s_repr)
        elif c == ' ':
            return cls(c, [
                [Segment.S0, Segment.S0],
                [Segment.S0, Segment.S0],
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


def main():
    lcd = CharLCD('PCF8574', 0x27)
    lcd.clear()
    segments = Segment.ALL
    register(lcd, segments)
    prev_time = ''
    prev_date = ''
    f_time = ' %H %M %S '
    f_date = '%a %d.%m.%Y'
    while True:
        now = datetime.now()
        time_str = now.strftime(f_time)
        date_str = now.strftime(f_date)
        if time_str != prev_time:
            lcd.cursor_pos = (0, 0)
            s = Char4String.from_str(time_str)
            s.print(lcd)
            prev_time = time_str
        if date_str != prev_date:
            lcd.cursor_pos = (3, 0)
            s = '{: ^20}'.format(date_str)
            lcd.write_string(s)
            prev_date = date_str
        time.sleep(0.1)
    lcd.close()

main()
