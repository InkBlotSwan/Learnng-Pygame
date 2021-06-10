# File Snow.py

import random
import pygame
pygame.init()
# Size of screen and settings
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow")

# Colour variables
WHITE = (255,255,255)
BLACK = (0,0,0)

snow_list = []
for i in range(500):
	snow_x = random.randint(0,700)
	snow_y = random.randint(0,500)
	snow_list.append([snow_x,snow_y])

# Main loop + variables
end = False
clock = pygame.time.Clock()
while end == False:
	# User interaction
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			end = True
	# Logic code
	# Drawing code
	screen.fill(BLACK)
	for i in snow_list:
		i[0] += random.randint(-1,1)
		i[1] += random.randint(1,2)
		if i[1] > 500:
			i[1] = random.randint(-18,-1)
			i[0] = random.randint(0,700)
		pygame.draw.circle(screen, WHITE,i,2)
	# Flip to screen
	pygame.display.flip()
	clock.tick(30)
pygame.quit()