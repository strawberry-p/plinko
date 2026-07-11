class Button:
    def __init__(self,text:str, smol:str, file:str, width: int, height:int):
        self.text = text
        self.has_smol = False
        if len(smol) > 0: self.has_smol = True
        self.smol = smol
        self.has_icon = False
        if len(file) > 0: self.has_icon = True
        self.file = file
        self.width = width
        self.height = height
        self.w_off = 10
        self.h_off = 40
        self.true_off = 0
        self.o = -1
        if self.has_icon: self.w_off = self.w_off*2+48
        if self.has_smol: self.h_off = 10


class UI:
    def __init__(self,pg,screen,clk):
        self.pg = pg
        self.screen = screen
        self.clk = clk
        self.pad = 30
        self.h_pad = 150
        self.back = "#A0A000"
        self.border = "#000000"
        self.button = "#CC6600"
        self.button_hover = "#FF6600"
        self.text_color = "#000000"
    
    def exec(self,lst: list[Button]) -> int:
        true_off = 100
        i = 0
        for item in lst:
            item.o = i
            item.true_off = true_off
            true_off += item.height
            true_off += self.pad
            i += 1
        i = 0
        print([x.__dict__ for x in lst])
        clicked = -1
        hover = -1
        last_hover = 0
        running = True
        while running or clicked != -1:
            mx, my = self.pg.mouse.get_pos()
            for event in self.pg.event.get():
                if event.type == self.pg.QUIT:
                    print(f"quitting from menu")
                    self.clk.tick(10)
                    running = False
                    self.pg.quit()
                    exit()
                elif event.type == self.pg.MOUSEBUTTONDOWN:
                    mx, my = self.pg.mouse.get_pos()
                    for o in lst:
                        if o.true_off <= my <= o.true_off+o.height\
                        and self.h_pad <= mx <= self.h_pad+o.width:
                            clicked = o.o #yes, i chose this just to make the lil face
                            running = False
                            break
            
            hover = -1
            for o in lst:
                if o.true_off <= my <= o.true_off+o.height\
                and self.h_pad <= mx <= self.h_pad+o.width:
                    hover = o.o
                    break
            if last_hover != hover:
                last_hover = hover
                for o in lst:
                    if hover == o.o:
                        color = self.button_hover
                    else:
                        color = self.button
                    rect = self.pg.Rect(self.h_pad,o.true_off,o.width,o.height)
                    self.pg.draw.rect(self.screen,color,rect)
                    if True: self.pg.draw.rect(self.screen,self.border,rect,4)
            self.pg.display.flip()
            self.clk.tick(30)
        return clicked


class FakeClock:
    def __init__(self):
        import time
        self.time = time
    def tick(self,fps: int|float):
        self.time.sleep(1/fps)
if __name__ == "__main__" and False:
    lst = [Button("blah 1","","",400,100),
           Button("blah horse","","Horseyicon_smol.png",400,100),
           Button("blah mouse","im mouse","",400,100)]
    print([x.__dict__ for x in lst])
    ui = UI(0,0,FakeClock())
    ui.exec(lst)
    