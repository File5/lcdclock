import argparse
from datetime import datetime
import time

from RPLCD.i2c import CharLCD

from lcdclock.char4 import Char4Segment, Char4String
from lcdclock.char9 import Char9Segment, Char9String


def register(lcd, segments):
    for s in segments:
        lcd.create_char(s.addr, s.data)


def main(args):
    lcd = CharLCD('PCF8574', 0x27)
    lcd.clear()

    if args.font == '4':
        segments = Char4Segment.ALL
    else:
        segments = Char9Segment.ALL

    register(lcd, segments)
    prev_time = ''
    prev_date = ''

    if args.font == '4':
        f_time = ' %H %M %S '
    else:
        f_time = '%H %M %S'

    f_date = '%a %d.%m.%Y'
    while True:
        now = datetime.now()
        time_str = now.strftime(f_time)
        date_str = now.strftime(f_date)
        if time_str != prev_time:
            lcd.cursor_pos = (0, 0)

            if args.font == '4':
                s = Char4String.from_str(time_str)
            else:
                s = Char9String.from_str(time_str)

            s.print(lcd)
            prev_time = time_str
        if date_str != prev_date:
            lcd.cursor_pos = (3, 0)
            s = '{: ^20}'.format(date_str)
            lcd.write_string(s)
            prev_date = date_str
        time.sleep(0.1)
    lcd.close()

parser = argparse.ArgumentParser(description='LCD 2004 Clock')
parser.add_argument('font', nargs='?', default='9', help='font (4 or 9)')
args = parser.parse_args()
main(args)
