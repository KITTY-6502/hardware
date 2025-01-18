# Rom Size in KB
rom_size = 512 * 1024

class Dot():
    def __init__(self):
        self.reset  = False
        self.pixel  = False
        self.pixel_early = False
        self.irq    = False
        self.fxtick = False
        self.sync   = False
        self.hsync = False
        self.vsync = False
        
    def to_byte(self):
        byte = 0
        if self.reset:
            byte += 0b0000_0001
        if self.fxtick:
            byte += 0b0000_0010
        if self.pixel:
            byte += 0b0000_0100
        if not self.hsync:
            byte += 0b0000_1000
        
        if not self.reset:
            byte += 0b0001_0000
        if not self.sync:
            byte += 0b0010_0000
        if not self.vsync:
            byte += 0b0100_0000
        if not self.irq:
            byte += 0b1000_0000
            
        return byte

def rom_pal(master_clock):
    rom = []
    for i in range(0x10000):
        rom.append(Dot())
    
    print("\nSpeed:",master_clock)
    
    columns = int(master_clock/16/15625)
    full_clocks = ( columns *4*56)*50
    slow_clocks = ( (16+(columns-32)) *4*256)*50
    
    print("Visible Area:", int(columns*0.825), "Border:", int(columns*0.825)-32)
    print("Bus Speed:",(master_clock/4/1_000_000))
    print("AVERAGE CPU:",(full_clocks+slow_clocks)/1_000_000)
    print("Half-Cycle ns:", 1000/2/((master_clock/4/1_000_000)))
    
    
    print("Columns:",columns)
    rom[columns*320-1].reset = True
    for line in range(320):
        if line%39 == 0:
            rom[columns*line].fxtick = True
        for column in range(columns):
            # HSYNC 
            rom[columns*line].hsync = True
            rom[columns*line+1].hsync = True
            # VSYNC
            if line > 304 and line <= 306:
                for r in range(columns):
                    rom[columns*line+r].vsync = True
            # H CSYNC
            if line < 312:
                for i in range(3):
                    rom[columns*line+1].sync = True
            # V CSYNC
            for i in range(8):
                for u in range(2):
                    y = i*2+u
                    p = (i+304)*columns + u * int(columns/2)
                    rom[p].sync = True
                    if y >= 6 and y <= 10:
                        for dot in range(p,p+int(columns/2)-3):
                            rom[dot].sync = True
            # Visible area
            start_line = 24
            if line >= start_line and line < start_line + 32*8:
                screen_start = int(1-columns*0.825)
                visible_start = screen_start + int( ( (columns*0.825)-32 ) / 2 )
                for column in range(visible_start, visible_start+32):
                    rom[columns*line + column].pixel = True
                    rom[columns*line + column].pixel_early = True
            # IRQ
            if line == start_line + 32*8:
                for column in range(columns):
                    rom[columns*line+column].irq = True
    return rom
def rom_ntsc(master_clock):
    rom = []
    for i in range(0x10000):
        rom.append(Dot())
    
    print("\nSpeed:",master_clock)
    
    columns = int(master_clock/16/15625)
    full_clocks = ( columns *4*56)*50
    slow_clocks = ( (16+(columns-32)) *4*256)*50
    
    print("Visible Area:", int(columns*0.825), "Border:", int(columns*0.825)-32)
    print("Bus Speed:",(master_clock/4/1_000_000))
    print("AVERAGE CPU:",(full_clocks+slow_clocks)/1_000_000)
    print("Half-Cycle ns:", 1000/2/((master_clock/4/1_000_000)))
    
    
    print("Columns:",columns)
    rom[columns*262].reset = True
    for line in range(262):
        for column in range(columns):
            # HSYNC 
            rom[columns*line].hsync = True
            rom[columns*line+1].hsync = True
            # VSYNC
            if line > 244 and line <= 246:
                for r in range(columns):
                    rom[columns*line+r].vsync = True
            # H CSYNC
            if line < 254:
                for i in range(3):
                    rom[columns*line+1].sync = True
            # V CSYNC
            for i in range(8):
                for u in range(2):
                    y = i*2+u
                    p = (i+244)*columns + u * int(columns/2)
                    rom[p].sync = True
                    if y >= 6 and y <= 10:
                        for dot in range(p,p+int(columns/2)-3):
                            rom[dot].sync = True
            # Visible area
            start_line = 8
            if line >= start_line and line < start_line + 24*8:
                screen_start = int(1-columns*0.825)
                visible_start = screen_start + int( ( (columns*0.825)-32 ) / 2 )
                for column in range(visible_start, visible_start+32):
                    rom[columns*line + column].pixel = True
                    rom[columns*line + column].pixel_early = True
            # IRQ
            if line == start_line + 24*8:
                for column in range(columns):
                    rom[columns*line+column].irq = True
    return rom

rom = rom_pal(14_750_000) + rom_ntsc(14_750_000)
print(len(rom))

with open("video.bin","wb") as f:
    data = []
    for i in range(len(rom)):
        data.append(rom[i].to_byte())
    
    for i in range(int(rom_size/len(rom))):
        f.write(bytes(data))