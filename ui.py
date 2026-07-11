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

