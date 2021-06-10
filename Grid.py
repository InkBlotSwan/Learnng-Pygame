# File Grid.py

import pygame
pygame.init()
# Constant variables
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

SCREEN_WIDTH = 255
SCREEN_HEIGHT = 255

# grid cariables
width = 20
height = 20
margin = 5
colour = WHITE
# grid class

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption("Grid")

# Creating a two dimensional array
grid = []
for row in range(10):
	grid.append([])
	for column in range(10):
		grid[row].append(0)

done = False
clock = pygame.time.Clock()
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			row = int(pos[0] / (width + margin))
			column = int(pos[1] / (width + margin))
			if grid[column][row] == 0:
				grid[column][row] = 1
			else:
				grid[column][row] = 0
	# Drawing code
	screen.fill(BLACK)

	x = 0
	y = 0
	for row in range(10):
		x = 0
		y += margin
		for column in range(10):
			x += margin
			colour = WHITE
			if grid[row][column] == 1:
				colour = GREEN
			pygame.draw.rect(screen,colour,[x,y,width,height])
			x += width
		y += height

	pygame.display.flip()
	clock.tick(30)
pygame.quit()