from pygame import *
screen = display.set_mode((1200, 800))
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    if mb[0] == 1:
        draw.circle(screen, (30, 125, 200), (mx, my), 10)
    display.flip()
quit()
