# File Platform.py

import pygame

# CONSTANT VARIABLES

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

SCREEN_WIDTH = (1200)
SCREEN_HEIGHT = (600)

# CLASSES
class Player(pygame.sprite.Sprite):
	velocity_x = 0
	velocity_y = 0
	level = None

	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([30,30])
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = (SCREEN_WIDTH / 2) - 15
		self.rect.y = (SCREEN_HEIGHT / 2) - 15

	def update(self):
		self.gravity()
		
		self.rect.x += self.velocity_x
		pos = self.rect.x
		blocks_hit = pygame.sprite.spritecollide(self,platform_hit,False)
		for i in blocks_hit:
			if self.velocity_x < 0:
				self.rect.right = i.rect.left
			else:
				self.rect.left = i.rect.right

		self.rect.y += self.velocity_y
		blocks_hit = pygame.sprite.spritecollide(self,platform_hit,False)
		for i in blocks_hit:
			if self.velocity_y > 0:
				self.rect.bottom = i.rect.top
			else:
				self.rect.top = i.rect.bottom

	def gravity(self):
		if self.velocity_y == 0:
			self.velocity_y = 1
		else:
			self.velocity_y += .45

		if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.velocity_y >= 0:
			self.velocity_y = 0
			self.rect.y = SCREEN_HEIGHT - self.rect.height

	def jump(self):
		self.rect.y += 2
		platform_hit = pygame.sprite.spritecollide(self,self.level.platform_list,False)
		self.rect.y -= 2

		if len(platform_hit) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
			self.velocity_y = -8

	def left(self):
		self.velocity_x = -4
	def right(self):
		self.velocity_x = 4
	def stop(self):
		self.velocity_x = 0

class Platform(pygame.sprite.Sprite):
	def __init__(self,width,height):
		super().__init__()
		self.image = pygame.Surface([width,height])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()

class Level():
	platform_list = None
	background = None

	def __init__(self,player):
		self.platform_list = pygame.sprite.Group()
		self.player = player

	def update(self):
		self.platform_list.update()

	def draw(self,screen):
		screen.fill(BLACK)
		self.platform_list.draw(screen)

class Level_1(Level):
	def __init__(self,player):
		super().__init__()
		platform = [
			[210,70,500,500],
			[210,70,200,400],
			[210,70,600,300]
		]

		for i in platform:
			block = Platform(i[0],i[1])
			block.rect.x = i[2]
			block.rect.y = i[3]
			block.player = player
			self.platform_list.add(block)

def main():
	pygame.init()

	size = [SCREEN_WIDTH,SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Platforms")

	player = Player()

	level_list = []
	level_list.append(Level_1(player))
	current_level_no = 0
	current_level = level_list[current_level_no]

	active_sprites = pygame.sprite.Group()
	player.level = current_level

	player.rect.x = 350
	player.rect.y = SCREEN_HEIGHT - player.rect.height
	active_sprites.add(player)

	done = False
	clock = pygame.time.Clock()

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.KEYDOWN:
				if event.key == K_a:
					player.left()
				elif event.key == K_d:
					player.right()
				elif event.key == K_SPACE:
					player.jump()
			elif event.type == pygame.KEYUP:
				if event.key == K_a:
					player.stop()
				elif event.type == K_d:
					player.stop()
			# Drawing code
		active_sprites.update()

		current_level.update()

			# Moving camera
		if player.rect.right > SCREEN_WIDTH:
			player.rect.right = SCREEN_WIDTH
		if player.rect.left < 0:
			player.rect.left = 0

		current_level.draw(screen)
		active_sprites.draw(screen)

		pygame.display.flip()
		clock.tick(60)
	pygame.quit()
if __name__ == "__main__":
	main()