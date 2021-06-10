# File HelloWorld.py

# Importing libraries
import pygame
pygame.init()

# Size of screen & settings
size=(500,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Hello World!")

# Simple colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN =(0,255,0)
BLUE = (0,0,255)

# Font type
font = pygame.font.Font(None,30)
text = font.render("Hello World!",True,BLACK)

# Game loop
flag = True
clock = pygame.time.Clock()
while flag == True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			flag = False

	screen.fill(WHITE)
	# Text
	screen.blit(text,[0,0])

	pygame.display.flip()

	# Speed
	clock.tick(30)
pygame.quit()