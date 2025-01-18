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
          

def rom_pal():
    rom = []
    for i in range(0x4000):
        rom.append(Dot())

    rom[48*312].reset = True

    welp = 0
    for line in range(320):
        rom[48*line].hsync = True
        rom[48*line+1].hsync = True
        if line > 304 and line <= 306:
            for r in range(48):
                rom[48*line+r].vsync = True
    for line in range(312):
        rom[48*line].sync = True
        rom[48*line+1].sync = True
        
        if line%39 == 0:
            print(line)
            rom[48*line].fxtick = True
            print("TICK",line)
        
        if line > 23+10 and line < 280+10:
            welp += 1
            for dot in range(48*line+11,48*(line+1)-5):
                rom[dot].pixel = True
            for dot in range(48*line+11,48*(line+1)-5):
                rom[dot].pixel_early = True
                
        if line == 280+10-1:
            rom[48*line+42].irq = True
                
    print(welp)
    for i in range(8):
        for u in range(2):
            y = i*2+u
            p = (i+304)*48 + u * 24
            rom[p].sync = True
            if y >= 6 and y <= 10:
                for dot in range(p,p+21):
                    rom[dot].sync = True
    return rom
def rom_ntsc():
    rom = []
    for i in range(0x4000):
        rom.append(Dot())

    rom[48*262].reset = True

    welp = 0
    for line in range(262):
        rom[48*line].hsync = True
        rom[48*line+1].hsync = True
        if line > 262-8 and line <= 262-6:
            for r in range(48):
                rom[48*line+r].vsync = True
    for line in range(262):
        rom[48*line].sync = True
        rom[48*line+1].sync = True
        
        if line%39 == 0:
            rom[48*line].fxtick = True
        
        if line > 23+10 and line < 216+10:
            welp += 1
            for dot in range(48*line+11,48*(line+1)-5):
                rom[dot].pixel = True
                rom[dot].pixel_early = True
                
        if line == 216+10-1:
            rom[48*line+42].irq = True
                
    print(welp)
    for i in range(8):
        for u in range(2):
            y = i*2+u
            p = (i+262-8)*48 + u * 24
            rom[p].sync = True
            if y >= 6 and y <= 10:
                for dot in range(p,p+21):
                    rom[dot].sync = True
    return rom

rom = rom_pal() + rom_ntsc()
print(len(rom))

with open("video.bin","wb") as f:
    data = []
    for i in range(len(rom)):
        data.append(rom[i].to_byte())
    
    for i in range(int(rom_size/len(rom))):
        f.write(bytes(data))