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
        if self.has_icon: self.w_off = self.w_off*2+48
        if self.has_smol: self.h_off = 10


class UI:
    def __init__(self,pg,screen,clk):
        self.pg = pg
        self.screen = screen
        self.clk = clk
        self.back = "#A0A000"
        self.border = "#000000"
        self.button = "#CC6600"
        self.button_hover = "#FF6600"
        self.text_color = "#000000"
    
    def exec(self,lst: list[Button]):
        running = True
        while running:
            mx, my = self.pg.mouse.get_pos()
            for event in self.pg.event.get():
                if event.type == self.pg.QUIT:
                    print(f"quitting from menu")
                    self.clk.tick(10)
                    running = False
                    self.pg.quit()
                    exit()
            self.clk.tick(30)

