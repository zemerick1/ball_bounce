import sys, pygame, random as r
from pygame.locals import *

# Constants
WHITE = pygame.Color("white")
GRAVITY = pygame.math.Vector2(0, .2)
FRICTION = 0.8
COLORS = [
    pygame.Color("white"),
    pygame.Color("green"),
    pygame.Color("blue"),
    pygame.Color("yellow"),
    pygame.Color("red")
]
class Ball():
    def __init__(self, win):
        self.win = win
        self.win_width, self.win_height = self.win.get_size()
        # Set position vector to a random X position, and a set Y position
        self.position = pygame.math.Vector2(r.randint(50, self.win_width-50), self.win_height-550)
        self.velocity = pygame.math.Vector2()
        self.accel = pygame.math.Vector2()
        # Set radius of balls to a random integer between 5, 20
        self.r = r.randint(5, 20)
        # Set mass equal to radius
        self.mass = self.r
        self.color = r.choice(COLORS)
    
    def applyForce(self, force):
        self.accel += force

    def changeColor(self):
        self.color = r.choice(COLORS)

    def applyFriction(self):
        diff = self.win_height - (self.position.y + (self.r*2))
        ''' If difference between ball and floor is <= 1 pixel, apply friction.
            Not the best strategy as vel will never be zero, but it is close enough.
        '''
        if diff <= 1:
            self.velocity *= 0.95

    def update(self): 
        # Border collisions
        if self.position.y <= 0:
            self.position.y = 0
            self.velocity.y = self.velocity.y * -1
            self.changeColor()
            self.applyFriction()
        if self.position.y >= (self.win_height-(self.r*2)):
            ''' If ball's outer edge hits Window Height (the bottom), reset position, reverse velocity, add friction.
                we normalize mass to effect velocity
            '''
            self.position.y = self.win_height-(self.r*2)
            self.velocity.y = (self.velocity.y - self.mass/100) * -1
            self.changeColor()
            self.applyFriction()

        # Handle right border. No Friction here.
        if self.position.x >= (self.win_width-(self.r*2)):
            self.position.x = self.win_width-(self.r*2)
            self.velocity.x = self.velocity.x * -1
            self.changeColor()
        
        elif self.position.x <= 0:
            # Since the ellipse.x is top left, we don't need to do the radius math.
            self.position.x = 0
            self.velocity.x = self.velocity.x * -1
            self.changeColor()
        
        print(f"VELOCITY: {self.velocity}")
        # Apply cumulative force. Velocity + Gravity
        self.applyForce(GRAVITY)
        self.velocity += self.accel
        self.position += self.velocity
        self.accel *= 0

    def draw(self):
        pygame.draw.ellipse(self.win, self.color, (self.position.x, self.position.y, self.r*2, self.r*2))