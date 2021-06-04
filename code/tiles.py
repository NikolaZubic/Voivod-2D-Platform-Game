# author: Nikola Zubic
import pygame


class TileClass(pygame.Rect):

	Group = []
	SolidGroup = []

	width, height = 40, 40

	total_tiles = 1

	H, V = 1, 26

	def __init__(self, x, y, Type, level=""):

		self.type = Type

		self.number = TileClass.total_tiles
		TileClass.total_tiles += 1

		self.walkable = True

		self.top = y
		self.bottom = y + 40
		self.left = x
		self.right = x + 40

		self.level = level

		if Type == 'empty':
			self.walkable = True
		else:
			self.walkable = False
			TileClass.SolidGroup.append(self)
			if self.level == "level1":
				self.image = pygame.image.load("img/tile_level1.png")
			elif self.level == "level2":
				self.image = pygame.image.load("img/tile_level2.png")
			elif self.level == "level3":
				self.image = pygame.image.load("img/tile_level3.png")
			else:
				self.image = pygame.image.load("img/tile_level1.png")

		pygame.Rect.__init__(self, (x, y), (TileClass.width, TileClass.height))

		self.rect = (x, y, TileClass.width, TileClass.height)
		TileClass.Group.append(self)

	@staticmethod
	def get_tile(number):
		for tile in TileClass.Group:
			if tile.number == number:
				return tile

	@staticmethod
	def empty_tiles():
		for tile in TileClass.Group:
			TileClass.Group.remove(tile)
		for tile in TileClass.SolidGroup:
			TileClass.SolidGroup.remove(tile)

	@staticmethod
	def draw_tiles(screen):
		for tile in TileClass.Group:
			if not(tile.type == 'empty'):
				screen.blit(tile.image, (tile.x, tile.y))

	@staticmethod
	def get_tile_at(x, y):
		for tile in TileClass.Group:
			if tile.left <= x <= tile.right and tile.top <= y <= tile.bottom:
				return tile
