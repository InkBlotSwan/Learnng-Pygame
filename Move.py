# File Move.py

import pygame
pygame.init()
#colours
GREEN = (0,150,0)
BLACK = (0,0,0)

def square(screen,x,y):
	pygame.draw.rect(screen,GREEN,[x,y,50,50])

size =(1200,700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moving with mouse")

clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
end = False
while end == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			end = True
	# Logic code
	mouse_loc = pygame.mouse.get_pos()
	x = mouse_loc[0]
	y = mouse_loc[1]
	# Drawing code
	screen.fill(BLACK)
	square(screen,x,y)

	pygame.display.flip()
	clock.tick(30)
pygame.quit()