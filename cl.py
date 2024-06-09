import pygame, manager, math
tick = manager.tick

def horizontal():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        return -1
    elif keys[pygame.K_d]:
        return 1
    return 0

def vertical():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        return 1
    if keys[pygame.K_s]:
        return -1
    return 0

class Player():
    def __init__(self):
        manager.gameObjects.append(self)


        self.p = pygame.math.Vector2(30,30)
        # Motion (Y coordinates mirrored)
        self.a = pygame.math.Vector2(0, 4.9) # Acceleration vector
        self.v = pygame.math.Vector2(10, 0) # Velocity vector 
        self.i = pygame.math.Vector2(0, 0) # Impulse vector

        self.dir = 0

        self.hitbox = (self.p.x, self.p.x + 60, self.p.y, self.p.y + 60)
        self.solid = True
        self.jump = False
    def move(self):
        #? Define Direction 
        if horizontal() == 1:
            self.dir = 1
        elif horizontal() == -1:
            self.dir = -1


        self.a += self.i # Impulse being applied forces.

        # X MOTION
        self.p.x += self.v.x*horizontal() + self.a.x

        # Y MOTION
        if abs(self.a.y) > 0.02:
            self.a.y /= 2
        else:
            self.a.y = 0

        if self.col() != True:
            self.v.y += self.a.y
            self.v.y += 9.8*tick*1.5
            self.p.y += self.v.y
            print(1)
        else:            
            if self.col() == True and self.v.y == 0:
                self.jump = False
            if self.col() == True and self.p.y + self.v.y > self.p.y:
                self.v.y = 0
            elif self.p.y + self.v.y < self.p.y:
                self.v.y += self.a.y
                self.v.y += 9.8*tick*1.5
                self.p.y += self.v.y


        #print(self.p, self.v, self.a, self.i)

        self.impulse()
        self.draw()
        
    def impulse(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.jump != True:
            self.v.y -= 15
            self.jump = True
 
    def draw(self):
        pygame.draw.rect(pygame.display.get_surface(), (0, 255, 0), (self.p.x, self.p.y, 60, 60))

    def get_other(self):
        for x in manager.gameObjects:
            if x.solid == True:
                if self.p.x > x.hitbox[0] and self.p.x < x.hitbox[1]:
                    if self.p.y > x.hitbox[2] and self.p.y < x.hitbox[3]:
                        return x

    def col(self):
        for x in manager.gameObjects:
            try:
                if x.solid == True:
                    if self.p.x > x.hitbox[0] and self.p.x < x.hitbox[1]:
                        if self.p.y > x.hitbox[2] and self.p.y < x.hitbox[3]:
                            return True
                else:
                    return False
            except:
                print("---bloop")






class Floor():
    def __init__(self, x, y):
        manager.gameObjects.append(self)
        self.x = x
        self.y = y
        self.solid = True
        self.w = 600
        self.h = 30
        self.hitbox = (self.x, self.x + self.w, self.y-60, self.y + self.h)
    def move(self):
        pygame.draw.rect(pygame.display.get_surface(), (0, 0, 255), (self.x, self.y, self.w, self.h))
