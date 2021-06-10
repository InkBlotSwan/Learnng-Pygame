# File Animate.py

import pygame
pygame.init()
# Size of screen and settings
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Learning to animate")

# Colours
BLACK = (0,0,0)
GREEN = (0,150,0)


# Variables for main loop
end = False
clock = pygame.time.Clock()

r_x = 100
r_y = 100

x_velocity = 3
y_velocity = 1
#Main loop start
while end == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			end = True
	# Drawing code
	screen.fill(BLACK)

	pygame.draw.rect(screen,GREEN,[r_x,r_y,50,50])

	pygame.display.flip()
	# Logic code
	r_x += x_velocity
	r_y += y_velocity
	if r_x > 649 or r_x < 0:
		x_velocity *= -1
	if r_y > 449 or r_y < 0:
		y_velocity *= -1
	# Program speed
	clock.tick(60)
pygame.quit()