# author: Nikola Zubic
import pygame
import sys
import characters_classes
import tiles
import animations
from time import time


def game_dynamics(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # player shooting
        if event.type == pygame.MOUSEBUTTONDOWN:
            now = time()
            if now - player.last_shoot >= player.shooting_reload:
                player.last_shoot = now
                p = characters_classes.PlayerProjectile(player.rect.x, player.rect.y, 25, 11,
                                                        "img/playerAnimation/player_weapon.png")

                laser = pygame.mixer.Sound("sword swing.ogg")
                pygame.mixer.Sound.play(laser)

                if characters_classes.Player.moving_right:
                    p.velocity_x = 10
                else:
                    p.velocity_x = -10
                    p.image = pygame.transform.flip(pygame.image.load("img/playerAnimation/player_weapon.png"), True, False)

    keys = pygame.key.get_pressed()

    # player's movement
    if keys[pygame.K_d]:
        player.is_running = True
        player.velocity_x = 5
        characters_classes.Player.moving_right = True
        if player.i >= len(animations.player_running):
            player.i = 0
        player.image = animations.player_running[player.i]

        player.i += 1

    elif keys[pygame.K_a]:
        player.is_running = True
        characters_classes.Player.moving_right = False
        player.velocity_x = -5
        if player.i >= len(animations.player_running):
            player.i = 0
        player.image = pygame.transform.flip(animations.player_running[player.i], True, False)
        player.i += 1

    else:
        player.velocity_x = 0
        player.is_running = False

    # player jumping action
    if keys[pygame.K_SPACE]:
        try:
            x = player.rect.x
            x2 = player.rect.x + 40
            y = player.rect.y - 20
            tile = tiles.TileClass.get_tile_at(x, y)
            tile2 = tiles.TileClass.get_tile_at(x2, y)
            if tile.type == 'empty' and tile2.type == 'empty':
                if not player.currently_jumping:
                    player.jump()
                    player.ji = 0
                    player.currently_jumping = True
        except:
            pass

    # boss attack logic
    if len(characters_classes.Boss.Group) > 0:
        for boss in characters_classes.Boss.Group:
            now = time()

            if now - boss.last_shoot >= boss.shooting_reload:
                boss.last_shoot = now
                laser = pygame.mixer.Sound("RetroLaser1.wav")
                pygame.mixer.Sound.play(laser)

                p = characters_classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y + 64, 3, 3,
                                                       "img/bossAnimation/fires/fire_1.png")
                p.velocity_x = -8

                p = characters_classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y + 64, 3, 3,
                                                       "img/bossAnimation/fires/fire_2.png")
                p.velocity_x = 8

                p = characters_classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y + 64, 3, 3,
                                                       "img/bossAnimation/fires/fire_3.png")
                p.velocity_y = 8

                p = characters_classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y + 64, 3, 3,
                                                       "img/bossAnimation/fires/fire_4.png")
                p.velocity_y = -8

                p = characters_classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y + 64, 3, 3,
                                                       "img/bossAnimation/fires/fire_5.png")
                p.velocity_x = 8
                p.velocity_y = 8

                p = characters_classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y + 64, 3, 3,
                                                       "img/bossAnimation/fires/fire_6.png")
                p.velocity_x = -8
                p.velocity_y = -8

                p = characters_classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y + 64, 3, 3,
                                                       "img/bossAnimation/fires/fire_7.png")
                p.velocity_x = 8
                p.velocity_y = -8

                p = characters_classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y + 64, 3, 3,
                                                       "img/bossAnimation/fires/fire_8.png")
                p.velocity_x = -8
                p.velocity_y = 8

    # enemies attack logic
    for enemy in characters_classes.Enemy.Group:
        if enemy.velocity_x < 0:
            if (enemy.rect.x - 400 < player.rect.x < enemy.rect.x) and (
                    enemy.rect.y + 60 > player.rect.y > enemy.rect.y - 20):

                now = time()

                if now - enemy.last_shoot >= enemy.shooting_reload:
                    enemy.last_shoot = now

                    p = characters_classes.EnemyProjectile(enemy.rect.x, enemy.rect.y, 25, 11, "img/arcane.png")
                    p.image = pygame.transform.flip(pygame.image.load("img/arcane.png"), True, False)
                    laser = pygame.mixer.Sound("RetroLaser1.wav")
                    pygame.mixer.Sound.play(laser)
                    p.velocity_x = -8

        elif enemy.velocity_x > 0:
            if (enemy.rect.x + 400 > player.rect.x > enemy.rect.x) and (
                    enemy.rect.y + 60 > player.rect.y > enemy.rect.y - 20):
                now = time()

                if now - enemy.last_shoot >= enemy.shooting_reload:
                    enemy.last_shoot = now
                    p = characters_classes.EnemyProjectile(enemy.rect.x, enemy.rect.y, 25, 11, "img/arcane.png")
                    laser = pygame.mixer.Sound("RetroLaser1.wav")
                    pygame.mixer.Sound.play(laser)
                    p.velocity_x = 8

        elif enemy.velocity_x == 0:
            if (enemy.rect.y + 60 > player.rect.y > enemy.rect.y - 20) and (
                    player.rect.x < enemy.rect.x - 400 or (
                    enemy.rect.x < player.rect.x < enemy.rect.x + 400)):
                now = time()

                if now - enemy.last_shoot >= enemy.shooting_reload:
                    enemy.last_shoot = now
                    p = characters_classes.EnemyProjectile(enemy.rect.x, enemy.rect.y, 25, 11, "img/arcane.png")
                    laser = pygame.mixer.Sound("RetroLaser1.wav")
                    pygame.mixer.Sound.play(laser)
                    p.velocity_x = +8


def game_collisions(player):
    for enemy in characters_classes.Enemy.Group:
        enemy_proj = pygame.sprite.spritecollide(enemy, characters_classes.PlayerProjectile.Group, True)
        if len(enemy_proj) > 0:
            for _ in enemy_proj:
                enemy.health -= 1

    for boss in characters_classes.Boss.Group:
        enemy_proj = pygame.sprite.spritecollide(boss, characters_classes.PlayerProjectile.Group, True)
        if len(enemy_proj) > 0:
            for _ in enemy_proj:
                boss.health -= 1

    player_dead = pygame.sprite.spritecollide(player, characters_classes.Enemy.Group, True)
    if len(player_dead) > 0:
        player.health = 0

    player_dead = pygame.sprite.spritecollide(player, characters_classes.Boss.Group, True)
    if len(player_dead) > 0:
        player.health = 0

    player_hit = pygame.sprite.spritecollide(player, characters_classes.EnemyProjectile.Group, True)
    if len(player_hit) > 0:
        for _ in player_hit:
            player.health -= 25

    for proj in characters_classes.PlayerProjectile.Group:
        projectile_hit_wall = pygame.sprite.spritecollide(proj, tiles.TileClass.SolidGroup, False)
        if len(projectile_hit_wall) > 0:
            for _ in projectile_hit_wall:
                characters_classes.PlayerProjectile.destroy(proj, characters_classes.PlayerProjectile)

    for proj in characters_classes.EnemyProjectile.Group:
        projectile_hit_wall = pygame.sprite.spritecollide(proj, tiles.TileClass.SolidGroup, False)
        if len(projectile_hit_wall) > 0:
            for _ in projectile_hit_wall:
                characters_classes.EnemyProjectile.destroy(proj, characters_classes.EnemyProjectile)

    # Player-Walls Collisions
    try:
        if player.moving_right:
            predicted = player.rect.x + 40 + player.velocity_x
            if tiles.TileClass.get_tile_at(predicted, player.rect.y + 2).type == 'solid' or tiles.TileClass.get_tile_at(
                    predicted, player.rect.y + 38).type == 'solid':
                player.velocity_x = 0
        elif not player.moving_right:
            predicted = player.rect.x + player.velocity_x
            if tiles.TileClass.get_tile_at(predicted, player.rect.y + 2).type == 'solid' or tiles.TileClass.get_tile_at(
                    predicted, player.rect.y + 38).type == 'solid':
                player.velocity_x = 0
    except:
        pass

    player.rect.y += player.velocity_y

    tile_hit_list = pygame.sprite.spritecollide(player, tiles.TileClass.SolidGroup, False)
    for tile in tile_hit_list:
        if player.velocity_y > 0:
            player.rect.y = tile.top - 40
            player.currently_jumping = False
        elif player.velocity_y < 0:
            player.rect.y = tile.top + 40
        player.velocity_y = 0

    # Enemy-Walls Collisions
    for enemy in characters_classes.Enemy.Group:
        tile_hit_list = pygame.sprite.spritecollide(enemy, tiles.TileClass.SolidGroup, False)
        for _ in tile_hit_list:

            if enemy.moving_right:
                enemy.rect.x = enemy.rect.x - 10
                enemy.velocity_x = -enemy.velocity_x
                enemy.image = pygame.transform.flip(enemy.image, True, False)
            elif not enemy.moving_right:
                enemy.rect.x = enemy.rect.x + 10
                enemy.velocity_x = -enemy.velocity_x
                enemy.image = pygame.transform.flip(enemy.image, True, False)

        enemy.rect.y += enemy.velocity_y

        tile_hit_list = pygame.sprite.spritecollide(enemy, tiles.TileClass.SolidGroup, False)
        for tile in tile_hit_list:
            if enemy.velocity_y > 0:
                enemy.rect.y = tile.top - 40
            elif enemy.velocity_y < 0:
                enemy.rect.y = tile.top + 40
            enemy.velocity_y = 0

    # Re-routing for enemies
    for enemy in characters_classes.Enemy.Group:
        if enemy.velocity_x < 0:
            x = enemy.rect.x - 0
            y = enemy.rect.y + 60
            tile = tiles.TileClass.get_tile_at(x, y)
            if tile.type == 'empty':
                enemy.velocity_x = -enemy.velocity_x
        if enemy.velocity_x > 0:
            x = enemy.rect.x + 60
            y = enemy.rect.y + 60
            tile = tiles.TileClass.get_tile_at(x, y)
            if tile.type == 'empty':
                enemy.velocity_x = -enemy.velocity_x


def player_animation_states(player):
    if player.currently_jumping:
        if player.ji >= len(animations.player_jumping):
            player.ji = len(animations.player_jumping) - 1

        if player.moving_right:
            player.image = animations.player_jumping[player.ji]

        if not player.moving_right:
            player.image = pygame.transform.flip(animations.player_jumping[player.ji], True, False)
        player.ji += 1

    elif not player.is_running:
        if player.i >= len(animations.player_idle):
            player.i = 0

        if player.moving_right:
            player.image = animations.player_idle[player.i]

        if not player.moving_right:
            player.image = pygame.transform.flip(animations.player_idle[player.i], True, False)
        player.i += 1
