# lcdclock

Clock with custom chars for 2004 LCD display

![image](https://user-images.githubusercontent.com/14141957/152680247-46bfa327-4337-4740-a619-d990bff71b56.png)

## Idea

2004 LCD display with HD44780 Hitachi controller allows to create 8 custom
characters. This can be used to create a custom multiline font similar to 7
segment display for displaying digits.

This task is more complicated than it seems to be because we can't use 7 segment representation directly - we control different pieces of the screen, not the 7 segment-like pieces. The restriction of 8 custom chars is an interesting challenge, that's why I'm doing this.

## Implementation

### 2-line font (Font 4)

The initial idea was to start with the existing font for digits and make the
pixels twice as big making them with 4 native pixels. Later here, in my notes, I consider 1 pixel which is displayed by 4 native pixels.

![image](https://user-images.githubusercontent.com/14141957/152678584-34450d27-b9b5-4c43-aad3-0ef518839918.png)

As a result I've significantly exceeded the "8 custom chars" limit of the display.

Then, I've decided to go with the 7 segment digits which are known to have a simple representation and are familiar to people.

![image](https://user-images.githubusercontent.com/14141957/152678672-b4acf3b2-f750-49cb-bb67-0cf2f8e10051.png)

Now, it's better but still exceeds the "8 custom chars" limit.

Then, I've spent a significant amount of time trying to reduce the number of
custom chars by combining similar chars and reusing common chars. It doesn't
sound like a hard task but it was quite challenging to maintain the
readability of the font. I did my best to design such font, although, some
might argue that it is not that good.

![image](https://user-images.githubusercontent.com/14141957/152678937-56f662af-b67e-4ee7-8878-6de67bd6dba8.png)

Some of the digits have become less readable but that's as far as I got with this font.

The final improvement I've been able to make was filling the gap between
pixels within the same LCD char with native pixels and making the spacing on
the outer side of the digit. This helped to improve the overall readability
when multiple digits are next to each other.

### 3-line font (Font 9)

The 2-line font can also be used with 1602 LCD displays but I wanted to also make use of my gorgeous 2004 LCD. Hence, making 3-line font for digits.

Here, once again, starting from the 7 segment digits I've quickly come to a
possible digit font. After making the segments thicker I was able to improve
readability and reduce the overall number of custom chars to 5.

Here, I only show digit "2" but with 1 segment misplaced only for the purpose
of demonstration (segment 4 should be replaced with segment 2). You can
easily imagine the representation of every digit.

![image](https://user-images.githubusercontent.com/14141957/152679512-1c6ae062-6baf-47d9-8c3d-262646b10232.png)

The only thing I want to mention is that I've put the digit "1" centered in
the 9 char rectancle compared to the traditional 7 segment representation of
it on the right of the indicator. This improved the overall readability when
the digit "1" is used.
