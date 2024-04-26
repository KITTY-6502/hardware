# System Assembling

## Bill of Materials

### Integrated Circuits

Name        | Qty | Package             | Description
------------|-----|---------------------|-------------
74HC00      |  1  | dip-14              | quad NAND
74HC14      |  1  | dip-14              | hex NOT (Schmitt-Trigger)
74HC85      |  1  | dip-16              | 4-bit Comparator
74HC138     |  2  | dip-16              | 3to8 Decoder
74HC139     |  1  | dip-16              | dual 2to4 Decoder
74HC153     |  1  | dip-16              | dual 4to1 Selector
74HC157     |  1  | dip-16              | quad 2to1 Selector
74HC165     |  5  | dip-16              | parallel-in Shift Register
74HC273     |  1  | dip-20              | 8-bit Register w/Reset
74HC574     |  4  | dip-20              | 8-bit Register w/3-State
74HC590     |  3  | dip-16              | 8-bit Sync Counter
74HC670     |  2  | dip-16              | 4x4-bit Register
74HC4040    |  1  | dip-16              | 12-bit Ripple Counter
74HCT540    |  1  | dip-20              | 8-bit Buffer (Inverting)
82c54       |  1  | dip-24-wide/plcc-28 | Tripple Timer
62256       |  1  | dip-28-wide         | 32KiB Sram
39SF040     |  3  | plcc-32             | 512KiB Nor Flash
65c02       |  1  | plcc-44             | 8-bit CPU

### Sockets

Name        | Qty |
------------|-----|
dip-14      |  2  |
dip-16      | 17  |
dip-20      |  6  |
dip-24-wide*|  1  |
dip-28-wide |  1  |
plcc-28*    |  1  |
plcc-32     |  3  |
plcc-44     |  1  |

> *1 Use either dip-24w or plcc depending on chosen 82c54 package

### Passives

Type              | Value               | Qty |
------------------|---------------------|-----|
12Mhz Quartz      | HC49                |  1  |
Diode             | 1n4148              |  5  |
Led               | Rectangular 2mmx5mm |  1  |
Led Holder        | 15mm Holder         |  1  |
Ceramic Capacitor | 33pF                |  1  |
Ceramic Capacitor | 47pF                |  1  |
Ceramic Capacitor | 100nF               | 34  |
Polar   Capacitor | 4.7µF               |  1  |
Polar   Capacitor | 10µF                |  3  |
Resistor          | 75Ω                 |  2  |
Resistor          | 470Ω                |  1  |
Resistor          | 680Ω                |  1  |
Resistor          | 820Ω                |  2  |
Resistor          | 1.2KΩ               |  2  |
Resistor          | 3.3KΩ               | 12  |
Resistor          | 5.6KΩ               |  1  |
Resistor          | 10KΩ                |  6  |
Resistor          | 20KΩ                | 10  |
Resistor          | 27KΩ                |  2  |
Resistor          | 1MΩ                 |  1  |

#### Keyboard

Type              | Value               | Qty |
------------------|---------------------|-----|
Diode             | 1n4148              | 45  |

### Switches and Connectors

Type                                        | Qty | Function
--------------------------------------------|-----|-----------
5x2.1 DC Power Jack                         |  1  | Power In
SCART Female (no ears)                      |  1  | Audio/Video Out
PJ-325                                      |  1  | Audio Out
VGA Female Connector                        |  1  | Video Out
Right Angle 2.54mm 44Pin Edge Connector     |  2  | Cartridge Slot
Right Angle Tactile Switch                  |  1  | Reset Button
SS-12D11-G5 Slide Switch                    |  1  | Power Switch
8-pin 2.54mm JST Vertical                   |  1  | Keyboard Connector
5-pin 2.54mm JST Vertical                   |  1  | Keyboard Connector

#### Keyboard
Type                                        | Qty | Function
--------------------------------------------|-----|-----------
8-pin 2.54mm JST Horizontal                 |  1  | Keyboard Connector
5-pin 2.54mm JST Horizontal                 |  1  | Keyboard Connector
2.00U Stabilizer                            |  1  | Return Stabalizer
6.25U Stabilizer                            |  1  | Spacebar Stabalizer
MX Switch/Kailh Low-Profile                 | 40  | Keyboard Switches
1U KeyCap                                   | 32  | Letters, Arrows, Escape
1.25U KeyCap                                |  3  | BackSpace, Alt, Ctrl
1.5U KeyCap                                 |  1  | BackSlash
1.75U KeyCap                                |  2  | Shift, Math
2U KeyCap                                   |  1  | Enter
6.25U KeyCap                                |  1  | SpaceBar

Due to the uncommon layout of the keyboard, it is preferable to pick a set of keycaps using a profile of uniform height, such as:

* DSA
* XDA
* G20
* MOA
* KAT

## Assembly

This guide approachs assembling the KITTY through a series of steps where one subsystem is built, tested and debugged, before moving on to the next step. Hoping this way to both avoid mistakes, and give you a better understanding of how the system works.

### Step 1 - Power Input

Install Power Jack, Power Switch, Big Decap, Power LED & its resistor.

### Step 2 - Clock and Reset

Install '14 and the passives for the clock and reset

Pierce Oscillator circuit 

### Step 3 - Clock Dividers

Install '590 and '4040

### Step 4 - First "Video" Output

Install Sig ROM, '574, SCART and VGA Ports, Mode and Sync components

The signal ROM is controlled by the clock dividers built in the previous step, and is in charge of:

* generating the video sync signals
* determining the visible portion of the screen
* generating a CPU interrupt request when the very last character on a frame is rendered
* resetting the clock counters at the end of the frame.

Finally a '574 latch is used to buffer the output of the Sig ROM before sending it to the rest of the system (to avoid signal transition glitches)

Connecting a video cable to an appropriate known-working display, there will be no image yet, but the signal should now be recognized by the display as Progressive PAL 50fps (what your display calls may vary). If the display shows a "no signal" message then most likely a mistake was made somewhere in this building step.

### Step 5 - Random Colors

Coordination '138, BOXY palette buffers, BOXY color mixer, BOXY out buffer, Color DAC

### Step 6 - RAM, memory mapping, and Stable Colors

SRAM, '85, '00, '590, '590

###Step 7 - Random Characters

'165, FONT ROM

### Step 8 - Installing the CPU

'w65c02

### Step 9 - Adding the test rom

ROM, '138, '273

### Step 10 - The Keyboard

'541 + keyboard + headers

### Step 11 - Sound System

82c54, '670, '670, '153, Sound DAC, Sound Filters

### Step 12 - The Case