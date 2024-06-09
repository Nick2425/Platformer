import pygame, os, cl, manager

tick = manager.tick
pygame.init()
pygame.display.init()

win = pygame.display.set_mode((1000, 1000))

player = cl.Player()
p1 = cl.Floor(0, 800)
p2 = cl.Floor(700, 300)
p3 = cl.Floor(100, 500)



while True:
    delay = int(tick*1000)
    pygame.time.delay(delay)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.update()
    win.fill((0,0,0))
    for x in manager.gameObjects:
        x.move()

