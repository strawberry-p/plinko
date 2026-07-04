import pygame

TRI_LAYERS = 9
TRI_WIDTH = 800
TRI_OFFSET = 200
TRI_Y_OFFSET = 200
Y_RATIO = 0.866
def find_tri_pos(width: int, layers: int) -> tuple[int,list]:
    unit = width/(layers+1)
    start = TRI_OFFSET+TRI_WIDTH/2
    ypos = 0
    ypos += TRI_Y_OFFSET
    res = []
    for i in range(layers):
        for j in range(i+1):
            off = 0
            res.append(start+off)
            off += unit
        start -= unit/2
        ypos += Y_RATIO*unit
    return((unit, res))

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 360))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()

            