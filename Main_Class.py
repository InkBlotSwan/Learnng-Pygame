# File Main_Class.py

import pygame
import random

# GLOBAL CONSTANTS

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# CLASSES IE THE REST OF THE PROGRAM
class Block(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([5,20])
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()

	def reset_block(self):
		self.rect.x = random.randrange(SCREEN_WIDTH)
		self.rect.y = random.randint(-150,-20)

	def update(self):
		self.rect.y += 1
		if self.rect.y > SCREEN_HEIGHT + self.rect.height:
			self.reset_block()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([15,15])
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()

	def update(self):
		self.pos = pygame.mouse.get_pos()
		self.rect.x = self.pos[0]
		self.rect.y = self.pos[1]

class Game():
	block_list = None
	all_sprites = None
	player = None
	game_over = False
	score = 0

	def __init__(self):
		self.score = 0
		self.game_over = False

		self.block_list = pygame.sprite.Group()
		self.all_sprites = pygame.sprite.Group()

		for i in range(50):
			block = Block()

			block.rect.x = random.randrange(SCREEN_WIDTH)
			block.rect.y = random.randrange(SCREEN_HEIGHT)

			self.block_list.add(block)
			self.all_sprites.add(block)

		self.player = Player()
		self.all_sprites.add(self.player)

	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if self.game_over:
					self.__init__()
			elif event.type == pygame.K_a:
				player.pos[0] -= 4
			elif event.type == pygame.K_d:
				player.pos[0] -= 4
			elif event.type == pygame.K_w:
				player.pos[1] -= 4
			elif event.type == pygame.K_s:
				player.pos[1] += 4
		return False

	def run_logic(self):
		if not self.game_over:
			self.all_sprites.update()

			self.blocks_hit = pygame.sprite.spritecollide(self.player,self.block_list,True)
			for i in self.blocks_hit:
				self.score += 1
				print("score: " + str(self.score))

				if len(self.block_list) == 0:
					self.game_over = True

	def draw_frame(self, screen):
		screen.fill(BLACK)

		if self.game_over:
			font = pygame.font.SysFont("serif", 50)
			text = font.render("GAME FINISHED. CLICK TO RESTART.", True, RED)

			x = (SCREEN_WIDTH / 2) - (text.get_width() / 2)
			y = (SCREEN_HEIGHT / 2) - (text.get_height() / 2)

			screen.blit(text, [x,y])
		else:
			self.all_sprites.draw(screen)
			pygame.display.flip()

	def main():
		pygame.init()

		size = [SCREEN_WIDTH,SCREEN_HEIGHT]
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("Game Classes")

		pygame.mouse.set_visible(False)

		finished = False
		clock = pygame.time.Clock()
		game = Game()

		while finished == False:
			finished = game.process_events()

			game.run_logic()

			game.draw_frame(screen)

			clock.tick(60)
		pygame.quit()

if __name__ == '__main__':
	Game.main()