HDMI
----

* https://daniel.lawrence.lu/blog/y2023m12d15  using an 8k display as a regular computer monitor


Eink
----

* https://dmitry.gr/?r=05.Projects&proj=29.%20eInk%20Price%20Tags
* https://github.com/markfodor/InkCal


I2C
---

Very good LCD. It has an I2C Funduino chip in the back with a jumper to turn on
and off the backlight. It has 4 pins, VCC - 5v, GND and SDA e SCL. It has a
small pot to adjust the contrast of the display and a Led to show that´s
powered up.

Cons:

To use with the Arduino UNO put the SDA pin on A4 (analog 4) and the SCL pin on
A5. Then use the following library:
http://arduino-info.wikispaces.com/file/view/LiquidCrystal_I2C2004V1.zip/341635418/LiquidCrystal_I2C2004V1.zip

OtherThoughts:

The adress of the LCD is 0x27. The main advantage is the use of only two pin of
the Arduino board, instead of the lot of pinss used by paralelal display


Affordable. Small foot print. Can be configured to work with arduino.
I2C address = 0x27
Use new LCD library at.
https://bitbucket.org/fmalpartida/new-liquidcrystal/wiki/Home

Use:
#define I2C_ADDR 0x27
#define BACKLIGHT_PIN 3
#define En_pin 2
#define Rw_pin 1
#define Rs_pin 0
#define D4_pin 4
#define D5_pin 5
#define D6_pin 6
#define D7_pin 7
LiquidCrystal_I2C lcd(I2C_ADDR,En_pin,Rw_pin,Rs_pin,D4_pin,D5_pin,D6_pin,D7_pin,BACKLIGHT_PIN,POSITIVE);

Mine works fine this way. I will order more!

Cons:

Can't make work with the manual provided (none).  Took me hours/days to get it
working, but with my details, you may have faster results. Look out for the
libraries, ans there are many, that look the same, but do not act the same.


This is, by far, the least expensive I2C LCD that I've found. It works as
expected: you need just 2 pins to control the LCD, including the backlight.
There are a number of available pinouts available for extending the product,
such as adding 5V or Gnd pins for other devices, or connecting other I2C
devices to the data and clock lines. In addition to program control, the
backlight has an on/off switch (a jumper, actually). A surprisingly
well-designed board.

Cons:

The mapping of LCD pins to I2C data pins isn't documented anywhere, and isn't
compatible with existing Arduino I2C LCD libraries. So, some code changes are
needed in order to use this. It would be super awesome if the backpack could
easily be removed from the LCD (to use with a 4x20 LCD), but they are soldered
together. Nothing that a desoldering pump and some wick can't fix, though.

OtherThoughts:

The LCD is white on blue, avg quality. The I2C controller is a PCF8574. Its
data pins are connected to the LCD as follows: P0=RS, P1=RW, P2=E,
P3=Backlight,P4=D4, P5=D5, P6=D6, P7=D7



Pros: Seems like its is well buildt and works greate when you get it to work.
Cons: No documentation or anything to help you get started. Got a working
library from this site,
https://bitbucket.org/fmalpartida/new-liquidcrystal/wiki/Home. But i had to
find a working code anothere place


Good LCD display with 16 characters on 2 lines. Potentiometer for contrast
adjustment and display backlight can be controlled over I2C.

Cons:

There is no datasheet attached but the details required to interface with the
display are available via review comments: - there is a PCF8574 I/O expander
(I2C adress 0x27) connected to the display - P0 = RS - P1 = RW - P2 = EN - P3 =
BACKLIGHT - P4 = D4 - P5 = D5 - P6 = D6 - P7 = D7 -> initialize the display to
4-bit mode

OtherThoughts:

Majority of the available documentation covers interfacing with Arduino/clones
using existing LCD libraries but I decided to go with Raspberry Pi and
implemented display control on top of I2C driver by myself. I2C pins SDA & SCL
and GND + VCC (5V) connected directly between the display and Raspberry Pi.
After enabling I2C in Raspberry and connecting the display you can check that
it is alive by issuing command: i2cdetect -y 0 (or 1).

For control commands take a look at Hitachi HD44780 manual. I have attached one
photo of the display in action with backlight on.
