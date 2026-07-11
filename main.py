import pygame, sys
import random as r
import ui
TRI_LAYERS = 9
TRI_WIDTH = 500
TRI_OFFSET = 100
TRI_Y_OFFSET = 100
Y_RATIO = 0.866
bucketlist = []
debug_speed = True
def find_tri_pos(width: int, layers: int) -> tuple[int | float,list[tuple], list[int | float]]:
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
    global bucketlist
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
    y_unit = unit*Y_RATIO/2
    size = (unit-2, unit*Y_RATIO/2)
    buckets_h = [0,0,0,0,0,0,0,0,0,0]
    for i in bucketlist:
        pos = (corners[1][0]+unit*i+1,corners[1][1]-y_unit*(buckets_h[i]+1)-1) #x is determined by bucket, y is determined by number of previous hits in it
        rect = pygame.Rect(pos, size)
        pygame.draw.rect(bg,"gray",rect)
        buckets_h[i] += 1
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

def icon_move(screen,clk,sx,sy,tx,ty,delta,fps_wait,icon: pygame.Surface,bg: pygame.Surface):
    dx = tx-sx
    dy = ty-sy
    fps_wait *= delta
    corr = [round(x/2) for x in icon.get_size()]
    for i in range(delta):
        sx += dx/delta
        sy += dy/delta
        screen.blit(bg,(0,0))
        screen.blit(icon,(sx-corr[0],sy-corr[1]))
        pygame.display.flip()
        clk.tick(fps_wait)

def main():
    global bucketlist
    horsing_around = False
    icon_target = "Horseyicon_smoler.png"
    next_is_icon = False
    for i in sys.argv:
        if i in ["--horse", "horse"]:
            horsing_around = True
        elif i in ["-i", "--img"]:
            next_is_icon = True
        else:
            if next_is_icon:
                horsing_around = True
                icon_target = i
                break
    unit,pin_pos,depth_pos = find_tri_pos(TRI_WIDTH, TRI_LAYERS)
    if debug_speed:
        print("tripos")
    depth_pos.append(depth_pos[-1]+unit*Y_RATIO)
    if False:
        print(pin_pos)
        print("===")
        print(depth_pos)
    d_pos = [x-(6+7+12) for x in depth_pos]
    pygame.init()
    sizing = TRI_WIDTH+TRI_OFFSET*2
    screen = pygame.display.set_mode((sizing, sizing-TRI_OFFSET/2))
    if debug_speed:
        print("pygame screen")
    clock = pygame.time.Clock()
    clock.tick(10)
    if True:
        lst = [ui.Button("blah 1","","",400,120),
           ui.Button("blah horse","","Horseyicon_smol.png",400,120),
           ui.Button("blah mouse","im mouse","",400,120)]
        UIobj = ui.UI(pygame,screen,clock)
        if debug_speed:
            print("UI obj created")
        clicked = UIobj.exec(lst)
    if horsing_around:
        iconic = pygame.image.load(icon_target)
    else:
        iconic = pygame.Surface((10,10))
        iconic.fill("white")
    iconic = iconic.convert_alpha()
    #interpolate(screen,clock,100, 80, 400, 70, 100, 5)
    start_y = d_pos.pop(0)
    tracer = []
    tracer.append([])
    for roll in range(6):
        bg = pygame.Surface(screen.get_size())
        bg = bg.convert()
        edit_background(bg, pin_pos)
        screen.blit(bg,(0,0))
        pygame.display.flip()
        ly = 0
        ly += start_y
        lx = TRI_OFFSET+TRI_WIDTH/2
        bucket = 9
        for y in d_pos:
            c = r.randint(0,1)
            if c == 0: c = -1
            bucket += c
            tracer[-1].append(c)
            tx = lx+c*unit/2
            if horsing_around:
                icon_move(screen, clock, lx, ly, tx, y, 10, 4, iconic,bg)
            else:
                interpolate(screen,clock,lx,ly,tx,y,10,5)
            ly = y
            lx = tx
        bucket /= 2
        bucket = round(bucket)
        bucketlist.append(bucket)
        print(f"reached {bucket}")
        if not horsing_around:
            interpolate(screen, clock, lx, ly, lx, ly+unit*Y_RATIO,10,4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"quitting after {len(bucketlist)} rolls")
                clock.tick(10)
                running = False
                pygame.quit()
                exit()
        clock.tick(0.5)
    edit_background(bg, pin_pos)
    screen.blit(bg,(0,0))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()

            