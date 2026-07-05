import pygame
import random as r
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
    unit = TRI_WIDTH/(TRI_LAYERS+1)
    width = round(TRI_WIDTH)
    height = round((width+2*unit)*Y_RATIO,1)
    startx = TRI_OFFSET
    starty = TRI_Y_OFFSET-unit*Y_RATIO
    corners = [(startx,starty), (startx,starty+height), (startx+width,starty+height), (startx+width, starty)]
    pos = [corners[1][0]+unit,corners[1][1]]
    tar = [pos[0],pos[1]-Y_RATIO*unit*2]
    for i in range(9):
        pygame.draw.line(bg,"brown",pos,tar,3)
        pos[0] += unit
        tar[0] += unit
    for i in range(4):
        pygame.draw.line(bg,"brown",corners[3-i],corners[2-i],4)
    for i in pin_pos:
        pygame.draw.circle(bg, "brown", i, 6)

def interpolate(screen,clk, sx,sy,tx,ty,delta=10,fps_wait=60):
    dx = tx-sx
    dy = ty-sy
    fps_wait *= delta
    for i in range(delta):
        sx += dx/delta
        sy += dy/delta
        pygame.draw.circle(screen, "white", (sx, sy), 7)
        pygame.display.flip()
        clk.tick(fps_wait)

def main():
    unit,pin_pos,depth_pos = find_tri_pos(TRI_WIDTH, TRI_LAYERS)
    depth_pos.append(depth_pos[-1]+unit*Y_RATIO)
    print(pin_pos)
    print("===")
    print(depth_pos)
    d_pos = [x-(6+7+12) for x in depth_pos]
    pygame.init()
    sizing = TRI_WIDTH+TRI_OFFSET*2
    screen = pygame.display.set_mode((sizing, sizing-TRI_OFFSET/2))
    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    edit_background(bg, pin_pos)
    screen.blit(bg,(0,0))
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(10)
    #interpolate(screen,clock,100, 80, 400, 70, 100, 5)
    start_y = d_pos.pop(0)
    ly = 0
    ly += start_y
    lx = TRI_OFFSET+TRI_WIDTH/2
    bucket = 5
    for y in d_pos:
        c = r.randint(0,1)
        if c == 0: c = -1
        bucket += c
        tx = lx+c*unit/2
        interpolate(screen,clock,lx,ly,tx,y,10,5)
        ly = y
        lx = tx
    bucket /= 2
    print(f"reached {bucket}")
    interpolate(screen, clock, lx, ly, lx, ly+unit*Y_RATIO,10,5)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()

            