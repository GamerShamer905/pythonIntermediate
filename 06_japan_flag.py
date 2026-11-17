import pygame

pygame.init()
height = 400
width = 600
display_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Pygame Window")

white = (255,255,255)
red = (188, 0, 45)
running = True

while running == True : 

    display_surface.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    pygame.draw.circle(display_surface, red, ((width//2),(height//2)), ((height/5)*(3/2)))
    pygame.display.update()
pygame.quit()