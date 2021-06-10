# File MoveKey.py

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

x = 200
y = 200
x_velocity = 0
y_velocity = 0
while end == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			end = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				x_velocity -= 1
			if event.key == pygame.K_d:
				x_velocity += 1
			if event.key == pygame.K_w:
				y_velocity -= 1
			if event.key == pygame.K_s:
				y_velocity += 1

	# Logic code
	x += x_velocity
	y += y_velocity
	if x > 1149 or x < 0:
		x_velocity *= -1
	if y > 649 or y < 0:
		y_velocity *= -1
	# Drawing code
	screen.fill(BLACK)
	square(screen,x,y)

	pygame.display.flip()
	clock.tick(30)
pygame.quit()