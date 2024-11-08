import pygame #A library has a set or collection of functions or properties for you to use it properly

pygame.init() #Helps us to initialize all the modules (functions and properties) from the pygame library that we will use 
screen = pygame.display.set_mode((600,600))
screen.fill((50,205,50))
blue = (0,0,255)
red = (255,0,0)
pink = (239,0,255)
yellow = (239,255,0)
orange = (255,171,0)
pygame.display.update()

class Circle:
    def __init__(self, clr, pos, radius, width):
        self.circle_colour = clr
        self.circle_radius = radius
        self.circle_pos = pos
        self.circle_width = width
        self.circle_surface = screen
    
    def draw(self):
        self.draw_circle = pygame.draw.circle( #Function for rectangle is pygame.draw.rect
            self.circle_surface,
            self.circle_colour,
            self.circle_pos,
            self.circle_radius,
            self.circle_width,
        )

    def grow(self, r):
        self.circle_radius = self.circle_radius + r
        self.draw_circle = pygame.draw.circle
        (
            self.circle_surface,
            self.circle_colour,
            self.circle_pos,
            self.circle_radius,
            self.circle_width,
        )

circle = Circle(blue, (300, 300), 100, 0)
circle2 = Circle(red, (300, 300), 80, 0)
circle3 = Circle(pink, (300, 300), 60, 0)
circle4 = Circle(yellow, (300, 300), 40, 0)
circle5 = Circle(orange, (300, 300), 20, 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((50, 205, 50))
            circle.draw()
            circle2.draw()
            circle3.draw()
            circle4.draw()
            circle5.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((50, 205, 50))
            circle.grow(10)
            circle2.grow(10)
            circle3.grow(10)
            circle4.grow(10)
            circle5.grow(10)
            pygame.display.update()