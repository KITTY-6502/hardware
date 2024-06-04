# What is a KITTY? (an introduction)

![](board.png)

The **KITTY** (Kewl Interactive Text Terminal sYstem) is a new 8bit 65c02-based fantasy homebrew computer developed by smal (that's me!), it envisions a microcomputer which never existed, with colorful text based graphics, an unique sound system and, oddly, cartridges as its main form of media and expansion.

Looking at the back of the system, we see an austere sight: An audio/video SCART port and two cartridge ports, and not a single peripheral port in sight! In fact, the basic cartridge that came bundled with every sold system had to include audio jacks on the cart itself in order to allow one to save their programs. Rather than a failure, this was the driving design philosphy behind the cost-saving design of the KITTY, to allow programs to come bundled with any extra features they might need, while leaving the base design unburdened, after all, what use would an extra port or feature be without an accompaning program to use it?

Sadly we do not have access to this particular alternate reality (perhaps because it is imaginary), so we can not judge the success of this particular design approach. However, I have designed and built a version of this system here in our own world for anyone to play with, and this is what this manual is all about.

I wish you a fun and (hopefully) educational time exploring this little system

![](photo.jpg)

> The original v0a board prototype

## Details

The current iteration of the KITTY board (v1a) uses only in-production parts and is open hardware that anyone can tweak and build upon, on the v1a board custom features like video and audio are all implemented through the means of discrete 74-series logic. All ICs are in either Dual-In-Line packages or PLCC packages using through hole sockets, so that no surface mount soldering is required for assembly and all ICs can be easily placed or removed.

Finally, all components, their values, and their general function within the circuit are written on the silkscreen itself, as I wanted a board that was easy to assemble and understand.

## SPECS

* **CPU** 65c02 @ ~2.2mhz (3mhz bus)
* **RAM** 28Kb Static Ram
* **MEDIA** 2 cartridge slots for programs or expansion, each with up to 128 banks of 32kb for a theoretical max of 4Mb per cartridge
* **VIDEO** Custom, 8x8 pixel characters on a 32x32 grid, selectable background/foreground colors from a pallette of 16 
* **AUDIO** Custom, 4 channels of 8x1 wavetable audio (3 melodic, 1 percussive), with 4bit+4bit stereo volume control
* **INPUT** Custom 40-key mechanical keyboard 
* **OUTPUT** SCART, using RGB progressive PAL @50.1hz
* **POWER** 5v DC via a center positive barrel jack

```
    .--------------------.                          .----------------------.
    | 64KiB Memory Space |                          |          I/O         |
    |--------------------|                          |--------------+-------|
    |                    | $0000                    | KEY 1        | $7000 |
    |                    | $0800                    | KEY 2        | $7010 |
    |                    | $1000                    | KEY 3        | $7020 |
    |                    | $1800                    | KEY 4        | $7030 |
    |                    | $2000                    | KEY 5        | $7040 |
    |      WORK RAM      | $2800                    | BANK Register| $70D0 |
    |       28KiB        | $3000                    | CH Freq 1    | $70E0 |
    |                    | $3800                    | CH Freq 2    | $70E1 |
    |                    | $4000                    | CH Freq 3    | $70E2 |
    |                    | $4800                    | CH Control   | $70E3 |
    |                    | $5000                    | CH Volume 1  | $70F0 |
    |                    | $5800                    | CH Volume 2  | $70F1 |
    |                    | $6000                    | CH Volume 3  | $70F2 |
    |   (video memory)   | $6800                    | CH Volume 4  | $70F3 |
    |--------------------| $7000                    | CH Waveform 1| $70F4 |
    |        I/O         | $7800                    | CH Waveform 2| $70F5 |
    |--------------------| $8000                    | CH Waveform 3| $70F6 |
    |                    | $8800                    | CH Waveform 4| $70F7 |
    |                    | $9000                    +--------------+-------+
    |                    | $9800
    |                    | $A000
    |     CART SPACE     | $A800
    |       32KiB        | $B000
    |    (256 Banks)     | $B800
    |                    | $C000
    |                    | $C800
    |                    | $D000
    |                    | $D800
    |                    | $E000
    |                    | $E800
    |                    | $F000
    |                    | $F800
    +--------------------+

```