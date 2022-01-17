from datetime import datetime
import time

from RPLCD.i2c import CharLCD

from lcdclock.char4 import Char4Segment, Char4String


def register(lcd, segments):
    for s in segments:
        lcd.create_char(s.addr, s.data)


def main():
    lcd = CharLCD('PCF8574', 0x27)
    lcd.clear()
    segments = Char4Segment.ALL
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
