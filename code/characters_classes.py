# author: Nikola Zubic
import pygame
import tiles
import animations
from time import time
from tiles import TileClass


class BaseClass(pygame.sprite.Sprite):
    all_game_sprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, initial_image_path):
        pygame.sprite.Sprite.__init__(self)

        BaseClass.all_game_sprites.add(self)

        self.image = pygame.image.load(initial_image_path)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity_x = 0
        self.velocity_y = 0

        self.width = width
        self.height = height

    def destroy(self, name):
        name.Group.remove(self)
        BaseClass.all_game_sprites.remove(self)
        del self

    def __str__(self):
        return str(self.get_number())

    def get_number(self):
        return int((self.rect.x / self.width) + 1) + ((self.rect.y / self.height) * 26)

    def get_tile(self):
        return TileClass.get_tile(self.get_number())


class Player(BaseClass):
    Group = pygame.sprite.Group()
    moving_right = True

    def __init__(self, x, y, width, height, initial_image_path):
        BaseClass.__init__(self, x, y, width, height, initial_image_path)

        Player.Group.add(self)

        self.currently_jumping = False

        self.go_down = False
        self.up = False

        self.shooting_reload = .3

        self.last_shoot = time()
        self.health = 100

        self.i = 0
        self.ji = 0

        self.flip = 0
        self.flipI = 0

        self.is_running = False
        self.type = Player

    # applies gravity to the player
    def calc_grav(self):
        if self.velocity_y == 0:
            self.velocity_y = 1
        else:
            self.velocity_y += .55

        if self.rect.y >= 640 - 80 and self.velocity_y >= 0:
            self.velocity_y = 0
            self.rect.y = 640 - 80

    def motion(self, display_width):
        predicted = self.rect.x + self.velocity_x

        if predicted < 0:
            self.velocity_x = 0
        elif predicted + self.width > display_width:
            self.velocity_x = 0

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x + self.width > display_width:
            self.rect.x = display_width - self.width

        self.rect.x += self.velocity_x

    # defines properties of a jump
    def jump(self):
        self.rect.y += 2
        tile_hit_list = pygame.sprite.spritecollide(self, tiles.TileClass.SolidGroup, False)
        self.rect.y -= 2

        if len(tile_hit_list) > 0 or self.rect.y + 40 >= 640:
            self.velocity_y = -10
            self.currently_jumping = False


class Enemy(BaseClass):
    Group = pygame.sprite.Group()
    score = 0

    def __init__(self, x, y, width, height, initial_image_path, vel):
        BaseClass.__init__(self, x, y, width, height, initial_image_path)
        Enemy.Group.add(self)
        self.velocity_x = vel
        self.health = 2
        self.moving_right = True
        self.is_running = False
        self.i = 1
        self.last_shoot = time()
        self.shooting_reload = .8
        self.type = Enemy

    # applies gravity
    def calc_grav(self):
        if self.velocity_y == 0:
            self.velocity_y = 1
        else:
            self.velocity_y += .55

        if self.rect.y >= 640 - 80 and self.velocity_y >= 0:
            self.velocity_y = 0
            self.rect.y = 640 - 80

    # defines movement
    def move(self, display_width):
        if self.is_running > 0:
            self.is_running = True
        if self.rect.x + self.width > display_width or self.rect.x < 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.velocity_x = -self.velocity_x

        self.rect.x += self.velocity_x

        if self.velocity_x > 0:
            self.moving_right = True
            if self.i >= len(animations.wraith_walking):
                self.i = 1
            self.image = animations.wraith_walking[self.i - 1]
            self.i += 1
        elif self.velocity_x < 0:
            self.moving_right = False
            if self.i >= len(animations.wraith_walking):
                self.i = 1
            self.image = pygame.transform.flip(animations.wraith_walking[self.i - 1], True, False)
            self.i += 1
        else:
            if self.i >= len(animations.wraith_idle):
                self.i = 1
            self.image = animations.wraith_idle[self.i - 1]
            self.i += 1

    @staticmethod
    def update_all(display_width):
        for enemy in Enemy.Group:
            i = 0
            enemy.calc_grav()
            enemy.move(display_width)
            if enemy.health <= 0:
                enemy.velocity_x = 0
                enemy.image = animations.wraith_dead[14]

                enemy.destroy(enemy)
                Enemy.score += 10


class FastEnemy(BaseClass):
    Group = pygame.sprite.Group()
    score = 0

    def __init__(self, x, y, width, height, initial_image_path, vel):
        BaseClass.__init__(self, x, y, width, height, initial_image_path)
        FastEnemy.Group.add(self)
        self.velocity_x = vel
        self.health = 4
        self.moving_right = True
        self.is_running = False
        self.i = 1
        self.type = FastEnemy

    # applies gravity
    def calc_grav(self):
        if self.velocity_y == 0:
            self.velocity_y = 1
        else:
            self.velocity_y += .55

        if self.rect.y >= 640 - 80 and self.velocity_y >= 0:
            self.velocity_y = 0
            self.rect.y = 640 - 80

    # defines movement
    def move(self, display_width):
        if self.is_running > 0:
            self.is_running = True
        if self.rect.x + self.width > display_width or self.rect.x < 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.velocity_x = -self.velocity_x

        self.rect.x += self.velocity_x

        if self.velocity_x > 0:
            self.moving_right = True
            if self.i >= len(animations.fast_wraith_walking):
                self.i = 1
            self.image = animations.fast_wraith_walking[self.i - 1]
            self.i += 1
        elif self.velocity_x < 0:
            self.moving_right = False
            if self.i >= len(animations.fast_wraith_walking):
                self.i = 1
            self.image = pygame.transform.flip(animations.fast_wraith_walking[self.i - 1], True, False)
            self.i += 1
        else:
            if self.i >= len(animations.fast_wraith_idle):
                self.i = 1
            self.image = animations.fast_wraith_idle[self.i - 1]
            self.i += 1

    @staticmethod
    def update_all(display_width):
        for enemy in FastEnemy.Group:
            i = 0
            enemy.calc_grav()
            enemy.move(display_width)
            if enemy.health <= 0:
                enemy.velocity_x = 0
                enemy.image = animations.fast_wraith_dead[14]

                enemy.destroy(enemy)
                FastEnemy.score += 10


class Boss(BaseClass):
    Group = pygame.sprite.Group()

    def __init__(self, x, y, width, height, initial_image_path):
        BaseClass.__init__(self, x, y, width, height, initial_image_path)
        Boss.Group.add(self)

        self.velocity_x = 1.4
        self.velocity_y = 1.4

        self.shooting_reload = 1
        self.last_shoot = time()

        self.type = Boss

        self.health = 25

    @staticmethod
    def move():
        for boss in Boss.Group:
            boss.rect.x += boss.velocity_x
            boss.rect.y += boss.velocity_y

            if boss.rect.x <= 0:
                boss.velocity_x = -boss.velocity_x

            elif boss.rect.x + 300 >= 1200:
                boss.velocity_x = -boss.velocity_x

            if boss.rect.y <= 280:
                boss.velocity_y = -boss.velocity_y

            if boss.rect.y >= 420:
                boss.velocity_y = -boss.velocity_y

            if boss.health <= 0:
                boss.velocity_x = 0
                boss.destroy(boss)
                Enemy.score += 100


class PlayerProjectile(BaseClass):
    Group = pygame.sprite.Group()

    def __init__(self, x, y, width, height, initial_image_path):
        BaseClass.__init__(self, x, y, width, height, initial_image_path)
        PlayerProjectile.Group.add(self)

        self.velocity_x = 0
        self.type = PlayerProjectile

    @staticmethod
    def movement():
        for projectile in PlayerProjectile.Group:
            projectile.rect.x += projectile.velocity_x
            projectile.rect.y += projectile.velocity_y

        for projectile in PlayerProjectile.Group:
            if projectile.rect.x + projectile.width > 1040 or projectile.rect.x < 0:
                projectile.destroy(projectile)


class EnemyProjectile(BaseClass):
    Group = pygame.sprite.Group()

    def __init__(self, x, y, width, height, initial_image_path):
        BaseClass.__init__(self, x, y, width, height, initial_image_path)
        EnemyProjectile.Group.add(self)

        self.velocity_x = 0
        self.type = EnemyProjectile

    @staticmethod
    def movement():
        for projectile in EnemyProjectile.Group:
            projectile.rect.x += projectile.velocity_x
            projectile.rect.y += projectile.velocity_y

        for projectile in EnemyProjectile.Group:
            if projectile.rect.x + projectile.width > 1040 or projectile.rect.x < 0:
                projectile.destroy(projectile)


class MenuItem(BaseClass):
    Group = pygame.sprite.Group()

    def __init__(self, x, y, width, height, initial_image_path):
        BaseClass.__init__(self, x, y, width, height, initial_image_path)
        MenuItem.Group.add(self)

        self.type = MenuItem

    def is_mouse_selection(self, pos_x, pos_y):
        if (self.rect.x <= pos_x <= self.rect.x + self.width) and \
                (self.rect.y <= pos_y <= self.rect.y + self.height):
            return True
        return False
