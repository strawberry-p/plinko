import pygame

TRI_LAYERS = 9
TRI_WIDTH = 500
TRI_OFFSET = 100
TRI_Y_OFFSET = 100
Y_RATIO = 0.866
def find_tri_pos(width: int, layers: int) -> tuple[int,list[tuple]]:
    unit = width/(layers+1)
    start = TRI_OFFSET+TRI_WIDTH/2
    ypos = 0
    ypos += TRI_Y_OFFSET
    res = []
    for i in range(layers):
        off = 0
        for j in range(i+1):
            res.append((start+off,round(ypos)))
            off += unit
        start -= unit/2
        ypos += Y_RATIO*unit
    return((unit, res))

def edit_background(bg,pin_pos: list[tuple]):
    for i in pin_pos:
        pygame.draw.circle(bg, "brown", i, 6)

def main():
    unit,pin_pos = find_tri_pos(TRI_WIDTH, TRI_LAYERS)
    print(pin_pos)
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    edit_background(bg, pin_pos)
    screen.blit(bg,(0,0))
    pygame.display.flip()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()

            