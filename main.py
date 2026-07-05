import pygame

TRI_LAYERS = 9
TRI_WIDTH = 500
TRI_OFFSET = 100
TRI_Y_OFFSET = 100
Y_RATIO = 0.866
def find_tri_pos(width: int, layers: int) -> tuple[int,list[tuple], list[int | float]]:
    unit = width/(layers+1)
    start = TRI_OFFSET+TRI_WIDTH/2
    ypos = 0
    ypos += TRI_Y_OFFSET
    res = []
    depth = []
    for i in range(layers):
        off = 0
        depth.append(ypos)
        for j in range(i+1):
            res.append((start+off,round(ypos)))
            off += unit
        start -= unit/2
        ypos += Y_RATIO*unit
    return((unit, res, depth))

def edit_background(bg,pin_pos: list[tuple]):
    for i in pin_pos:
        pygame.draw.circle(bg, "brown", i, 6)

def interpolate(screen,clk, sx,sy,tx,ty,delta=10,fps_wait=60):
    dx = tx-sx
    dy = ty-sy
    fps_wait *= delta
    for i in range(delta):
        sx += dx/delta
        sy += dy/delta
        pygame.draw.circle(screen, "white", (sx, sy), 8)
        pygame.display.flip()
        clk.tick(fps_wait)

def main():
    unit,pin_pos,depth_pos = find_tri_pos(TRI_WIDTH, TRI_LAYERS)
    depth_pos.append(depth_pos[-1]+unit*Y_RATIO)
    print(pin_pos)
    print("===")
    print(depth_pos)
    d_pos = [x-(6+8+2) for x in depth_pos]
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    edit_background(bg, pin_pos)
    screen.blit(bg,(0,0))
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(10)
    interpolate(screen,clock,100, 80, 400, 80, 100, 5)
    for y in d_pos:
        pass
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()

            