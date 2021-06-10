# File Snake.py

import pygame

# Constants

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

BODY_SEGMENT_WIDTH = 15
BODY_SEGMENT_HEIGHT = 15
SEGMENT_MARGIN = 3

class Body_segment(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.Surface([BODY_SEGMENT_WIDTH,BODY_SEGMENT_HEIGHT])
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption("Snake")

all_sprites = pygame.sprite.Group()

# Generating a snake
snake_list = []
for i in range(10):
	x = 250 - (BODY_SEGMENT_WIDTH - SEGMENT_MARGIN) * i
	y = 30
	segment = Body_segment(x,y)
	snake_list.append(segment)
	all_sprites.add(segment)

clock = pygame.time.Clock()
running = True

x_velocity = 0
y_velocity = 0
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runing = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				x_velocity = (BODY_SEGMENT_WIDTH + SEGMENT_MARGIN) * -1
			elif event.key == pygame.K_d:
				x_velocity = (BODY_SEGMENT_WIDTH + SEGMENT_MARGIN)
			elif event.key == pygame.K_w:
				y_velocity = (BODY_SEGMENT_HEIGHT + SEGMENT_MARGIN) * -1
			elif event.key == pygame.K_s:
				y_velocity = (BODY_SEGMENT_HEIGHT + SEGMENT_MARGIN)

		old_segment = snake_list.pop()
		all_sprites.remove(old_segment)

		x = snake_list[0].rect.x + x_velocity
		y = snake_list[0].rect.y + y_velocity
		segment = Body_segment(x,y)
		snake_list.insert(0,segment)
		all_sprites.add(segment)
		# Drawing code
		screen.fill(BLACK)

		all_sprites.draw(screen)

		pygame.display.flip()

	clock.tick(15)
pygame.quit()