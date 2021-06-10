# File Rooms.py

import pygame
pygame.init()

# Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Classes
class Wall(pygame.sprite.Sprite):
	def __init__(self, x_position, y_position, width, height,colour):
		super().__init__()
		self.image = pygame.Surface([width,height])
		self.image.fill(colour)
		self.rect = self.image.get_rect()
		self.rect.x = x_position
		self.rect.y = y_position

class Player(pygame.sprite.Sprite):
	velocity_x = 0
	velocity_y = 0
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.Surface([10,10])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def Velocity(self,x,y):
		self.velocity_x += x
		self.velocity_y += y

	def Move(self,wall):
		self.rect.x += self.velocity_x
		walls_hit = pygame.sprite.spritecollide(self,wall,False)
		for wall in walls_hit:
			# Moving right
			if self.velocity_x > 0:
				self.rect.right = wall.rect.left
			else:
				self.rect.left = wall.rect.right

		self.rect.y += self.velocity_y
		walls_hit = pygame.sprite.spritecollide(self,wall,False)
		for wall in walls_hit:
			# Moving right
			if self.velocity_y > 0:
				self.rect.right = wall.rect.left
			else:
				self.rect.left = wall.rect.right

class Room(object):
	wall_list = None
	def __init__(self):
		self.wall_list = pygame.sprite.Group()

class Room1(Room):
	def __init__(self):
		super().__init__()
		# List of walls
		walls = [[0, 0, 20, 250, RED],
				[0, 350, 20, 250, RED],
				[780, 0, 20, 250, RED],
				[780, 350, 20, 250, RED],
				[20, 0, 760, 20, RED],
				[20, 580, 760, 20, RED],
				[190, 50, 20, 500, GREEN],
				[590, 50, 20, 500, GREEN]
		]
 
		for i in walls:
			wall = Wall(i[0],i[1],i[2],i[3],i[4])
			self.wall_list.add(wall)

class Room2(Room):
	def __init__(self):
		# List of walls
		super().__init__()
		walls = [[0, 0, 20, 250, WHITE],
				[0, 350, 20, 250, WHITE],
				[780, 0, 20, 250, WHITE],
				[780, 350, 20, 250, WHITE],
				[20, 0, 760, 20, WHITE], 
				[20, 580, 760, 20, WHITE],
				[390, 50, 20, 500, BLUE]
		]
 
		for i in walls:
			wall = Wall(i[0],i[1],i[2],i[3],i[4])
			self.wall_list.add(wall)

# Screen 
width = 700
height = 400
size = [width,height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rooms")

moving_sprites = pygame.sprite.Group()
player = Player(20,20)
moving_sprites.add(player)

rooms = []
room = Room1()
rooms.append(room)
room = Room2()
rooms.append(room)

current_room_no = 0
current_room = rooms[current_room_no]

clock = pygame.time.Clock()
running = True
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				player.Velocity(-5,0)
			elif event.key == pygame.K_d:
				player.Velocity(5,0)
			elif event.key == pygame.K_w:
				player.Velocity(0,-5)
			elif event.key == pygame.K_s:
				player.Velocity(0,5)
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				player.Velocity(5,0)
			elif event.key == pygame.K_d:
				player.Velocity(-5,0)
			elif event.key == pygame.K_w:
				player.Velocity(0,5)
			elif event.key == pygame.K_s:
				player.Velocity(0,-5)

	# Logic code
	player.Move(current_room.wall_list)

	if player.rect.x < -15:
		if current_room_no == 0:
			current_room_no = 1
			current_room = rooms[current_room_no]
			player.rect.x = 690
		elif current_room_no == 1:
			current_room_no = 0
			current_room = rooms[current_room_no]
			player.rect.x = 690

	if player.rect.x > 710:
		if current_room_no == 0:
			current_room_no = 1
			current_room = rooms[current_room_no]
			player.rect.x = 10
		elif current_room_no == 1:
			current_room_no = 0
			current_room = rooms[current_room_no]
			player.rect.x = 10

	# Drawing code
	screen.fill(BLACK)
	moving_sprites.draw(screen)
	current_room.wall_list.draw(screen)
	pygame.display.flip()

	clock.tick(30)
pygame.quit()