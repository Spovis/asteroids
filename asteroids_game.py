import pygame
pygame.init()
window_height = 500
window_width = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("asteroids")
running = True
class Character(object):
    def __init__(self,x,y, width,vertex1, vertex2, vertex3,height, vel,wideness):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.wideness = wideness
        self.vertex1 = (self.x, self.y - self.height)
        self.vertex2 = (int(self.x + (self.wideness/2)), self.y)
        self.vertex3 = (int(self.x - (self.wideness/2)), self.y)
        self.vel = vel
    def change_vertex(self, direction, amnt_change):
        if direction == "U":
            self.y -= amnt_change
            self.vertex1 = (self.x, self.y - self.height)
            self.vertex2 = (int(self.x + (self.wideness / 2)), self.y)
            self.vertex3 = (int(self.x - (self.wideness / 2)), self.y)
        elif direction == "D":
            self.y += amnt_change
            self.vertex1 = (self.x, self.y - self.height)
            self.vertex2 = (int(self.x + (self.wideness / 2)), self.y)
            self.vertex3 = (int(self.x - (self.wideness / 2)), self.y)
        elif direction == "L":
            self.x -= amnt_change
            self.vertex1 = (self.x, self.y - self.height)
            self.vertex2 = (int(self.x + (self.wideness / 2)), self.y)
            self.vertex3 = (int(self.x - (self.wideness / 2)), self.y)
        elif direction == "R":
            self.x += amnt_change
            self.vertex1 = (self.x, self.y - self.height)
            self.vertex2 = (self.x + (self.wideness // 2), self.y)
            self.vertex3 = (int(self.x - (self.wideness / 2)), self.y)
        else:
            pass

    def move_char(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if (self.x + (self.wideness/2)) + 1 < (window_width):
                self.x += self.vel
                self.change_vertex("R", self.vel)

        if keys[pygame.K_LEFT]:
            if self.x - (self.wideness/2) > 1:
                self.x -= self.vel
                self.change_vertex("L", self.vel)
        
        if keys[pygame.K_UP]:
            if self.y > self.height:
                self.y -= self.vel
                self.change_vertex("U", self.vel)

        if keys[pygame.K_DOWN]:
            if self.y < (window_height):
                self.y += self.vel
                self.change_vertex("D", self.vel)

bob = Character(200,200,1,(20,30),(22,20),(18,20),20, 1, 6)
bullets = []
class Bullet(object):
    def __init__(self, x, y, radius, color, width):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.width = width
    def show(self):
        pygame.draw.circle(window, self.color, (self.x,self.y),self.radius)
    def move(self):
        if self.y <= 0:
            bullets.pop(bullets.index(self))

        else:
            self.y -= 3

being_held = False
run = True
while run:
    pygame.time.delay(3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    bob.move_char()
    keys = pygame.key.get_pressed()
    if being_held ==  False:
        if keys[pygame.K_SPACE]:
            being_held = True
            bullets.append(Bullet(bob.x, (bob.y - bob.height), 5, (255,0,0 ), 1))
    else:
        if keys[pygame.K_SPACE]:
            being_held = True
        else:
            being_held = False


    window.fill((0,0,0))
    for bullet in bullets:
        bullet.show()
        bullet.move()
    pygame.draw.polygon(window, (200,200,200), [bob.vertex1, bob.vertex2, bob.vertex3], bob.width)
    pygame.display.update()

pygame.quit()