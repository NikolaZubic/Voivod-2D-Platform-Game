# author: Nikola Zubic
from characters_classes import *
from game_logic import *
from tiles import *
import utils

pygame.init()
pygame.font.init()
pygame.mixer.init()

TILE_SIZE = 40
display_width = 26  # 1040
display_height = 16  # 640

level = 0
game_display = pygame.display.set_mode((display_width * TILE_SIZE, display_height * TILE_SIZE))
pygame.display.set_caption('Voivod (2D Platform Game)')

clock = pygame.time.Clock()
fps = 30
total_number_of_frames = 0
paused = False
music = False
dead = False
complete = False

# Game Loop
while True:
    if level != 0 and level < 4:
        if paused is False and dead is False and complete is False:
            game_dynamics(player)
            game_collisions(player)
            player_animation_states(player)
            keys = pygame.key.get_pressed()

            if player.health <= 0:
                dead = True
            if len(Enemy.Group) <= 0 and len(FastEnemy.Group) <= 0 and len(Boss.Group) <= 0:
                complete = True

            player.calc_grav()
            player.motion(display_width * TILE_SIZE)
            PlayerProjectile.movement()
            EnemyProjectile.movement()
            Enemy.update_all(display_width * TILE_SIZE)
            FastEnemy.update_all(display_width * TILE_SIZE)
            if len(Boss.Group) > 0:
                Boss.move()
            total_number_of_frames += 1

            # draw to display
            game_display.blit(background, (0, 0))
            BaseClass.all_game_sprites.draw(game_display)
            TileClass.draw_tiles(game_display)
            if len(Boss.Group) > 0:
                Boss.move()
                Boss.Group.draw(game_display)
            utils.health_bar(game_display, player)
            utils.score(game_display, fps, total_number_of_frames)

            # update display
            pygame.display.update()

            if keys[pygame.K_ESCAPE]:
                paused = True
        # pause logic
        elif paused:

            resume = MenuItem(382, 120, 276, 100, "images/buttons/button_continue.png")
            main_menu = MenuItem(382, 240, 276, 100, "images/buttons/button_exit.png")
            BaseClass.all_game_sprites.draw(game_display)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = pygame.mouse.get_pos()
                    if resume.is_mouse_selection(mousex, mousey):
                        for item in MenuItem.Group:
                            item.destroy(MenuItem)
                        paused = False

                    elif main_menu.is_mouse_selection(mousex, mousey):
                        for item in MenuItem.Group:
                            item.destroy(MenuItem)
                            for sprite in BaseClass.all_game_sprites:
                                BaseClass.destroy(sprite, sprite.type)
                                TileClass.empty_tiles()
                        paused = False

                        pygame.mixer.music.load("sounds/game_music/Metroid Main Menu Theme.ogg")
                        pygame.mixer.music.play(-1)

                        level = 0

        # Player dead logic
        elif dead:

            restart = MenuItem(382, 120, 276, 100, "images/buttons/button_restart.png")
            main_menu = MenuItem(382, 240, 276, 100, "images/buttons/button_exit.png")
            BaseClass.all_game_sprites.draw(game_display)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = pygame.mouse.get_pos()

                    if restart.is_mouse_selection(mousex, mousey):
                        for item in MenuItem.Group:
                            item.destroy(MenuItem)
                        for sprite in BaseClass.all_game_sprites:
                            BaseClass.destroy(sprite, sprite.type)
                            TileClass.empty_tiles()
                        dead = False
                        pygame.mixer.music.load("sounds/game_music/Metroid Main Menu Theme.ogg")
                        pygame.mixer.music.play(-1)
                        level = 0

                    elif main_menu.is_mouse_selection(mousex, mousey):
                        for item in MenuItem.Group:
                            item.destroy(MenuItem)
                            for sprite in BaseClass.all_game_sprites:
                                BaseClass.destroy(sprite, sprite.type)
                                TileClass.empty_tiles()
                        dead = False
                        pygame.mixer.music.load("sounds/game_music/Metroid Main Menu Theme.ogg")
                        pygame.mixer.music.play(-1)

                        level = 0
            pygame.display.update()

        # level complete logic
        elif complete:
            grade = ''
            final_score = int(120 - ((int(total_number_of_frames / fps) * .1) * 2) - (100 - player.health))
            if final_score >= 100:
                final_score = 100
                grade = 'A+'
            elif final_score >= 90:
                grade = 'A'
            elif final_score >= 80:
                grade = 'B'
            elif final_score >= 70:
                grade = 'C'
            elif final_score >= 60:
                grade = 'D'
            else:
                grade = 'E'

            if final_score <= 0:
                final_score = 0

            utils.game_text(game_display, "Final score: " + str(final_score) + ", Grade: " + grade, 320, 120, 40,
                            (255, 0, 0))
            continue_game = MenuItem(382, 180, 276, 100, "images/buttons/button_continue.png")
            main_menu = MenuItem(382, 300, 276, 100, "images/buttons/button_exit.png")
            BaseClass.all_game_sprites.draw(game_display)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = pygame.mouse.get_pos()
                    if continue_game.is_mouse_selection(mousex, mousey):
                        for item in MenuItem.Group:
                            item.destroy(MenuItem)
                            for sprite in BaseClass.all_game_sprites:
                                BaseClass.destroy(sprite, sprite.type)
                                TileClass.empty_tiles()
                        complete = False

                        pygame.mixer.music.load("sounds/game_music/Metroid Main Menu Theme.ogg")
                        pygame.mixer.music.play(-1)

                        level = 0

                    elif main_menu.is_mouse_selection(mousex, mousey):
                        for item in MenuItem.Group:
                            item.destroy(MenuItem)
                            for sprite in BaseClass.all_game_sprites:
                                BaseClass.destroy(sprite, sprite.type)
                                TileClass.empty_tiles()
                        complete = False

                        pygame.mixer.music.load("sounds/game_music/Metroid Main Menu Theme.ogg")
                        pygame.mixer.music.play(-1)

                        level = 0

    # level select
    elif level == 4:
        game_display.blit(background, (0, 0))
        BaseClass.all_game_sprites.draw(game_display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if back.is_mouse_selection(mousex, mousey):
                    for item in MenuItem.Group:
                        item.destroy(MenuItem)
                        for sprite in BaseClass.all_game_sprites:
                            BaseClass.destroy(sprite, sprite.type)
                            TileClass.empty_tiles()
                    level = 0

                if level1.is_mouse_selection(mousex, mousey):
                    for item in MenuItem.Group:
                        item.destroy(MenuItem)
                        for sprite in BaseClass.all_game_sprites:
                            BaseClass.destroy(sprite, sprite.type)
                            TileClass.empty_tiles()

                    pygame.mixer.music.load("sounds/game_music/Voivod - Brain Scan (8 Bit).ogg")
                    pygame.mixer.music.play(-1)
                    invalids = (360, 334, 308, 282, 256, 230, 204, 205, 206, 207, 208, 232, 258, 284, 310, 336, 362,
                                338, 257, 258, 259, 309, 310, 311, 361, 362, 329, 330, 331, 332, 371, 372, 373, 347,
                                348, 374, 327, 370, 386, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402,
                                403, 404, 405, 406, 407, 260, 312, 363, 364, 388, 390, 286, 234, 408, 409, 410, 411,
                                412, 413, 414, 415, 416, 417, 328, 333, 194, 195, 196, 197, 198, 235, 1, 79, 105, 131,
                                157, 280, 281, 255, 263, 262, 264, 57, 58, 59, 60, 117, 118, 119, 120, 261, 186, 106,
                                161, 132, 53, 27, 265, 266, 72, 73, 182)

                    background = pygame.image.load("images/levels/first_level.jpg")

                    player = Player(0, display_height * TILE_SIZE - 80, 40, 40, "images/tiles/tile_level1.png")
                    e1 = Enemy(600, 440, 40, 40, "images/tiles/tile_level1.png", 2)
                    e2 = Enemy(620, 560, 40, 40, "images/tiles/tile_level1.png", 3)
                    e3 = Enemy(740, 440, 40, 40, "images/tiles/tile_level1.png", 1)
                    e4 = Enemy(2, 320, 40, 40, "images/tiles/tile_level1.png", 0)
                    e5 = Enemy(880, 260, 40, 40, "images/tiles/tile_level1.png", 1)
                    e6 = Enemy(480, 260, 40, 40, "images/tiles/tile_level1.png", 1)
                    e7 = Enemy(160, 80, 40, 40, "images/tiles/tile_level1.png", 2)
                    e8 = Enemy(520, 160, 40, 40, "images/tiles/tile_level1.png", 3)
                    e9 = Enemy(800, 40, 40, 40, "images/tiles/tile_level1.png", 1)

                    tiles.TileClass.total_tiles = 1
                    characters_classes.Enemy.score = 0
                    characters_classes.FastEnemy.score = 0
                    total_number_of_frames = 0

                    for y in range(0, game_display.get_height(), TILE_SIZE):
                        for x in range(0, game_display.get_width(), TILE_SIZE):
                            if TileClass.total_tiles in invalids:
                                TileClass(x, y, 'solid', 'level1')
                            else:
                                TileClass(x, y, 'empty')
                    level = 1

                if level2.is_mouse_selection(mousex, mousey):
                    for item in MenuItem.Group:
                        item.destroy(MenuItem)
                        for sprite in BaseClass.all_game_sprites:
                            BaseClass.destroy(sprite, sprite.type)
                            TileClass.empty_tiles()
                    pygame.mixer.music.load("sounds/game_music/Voivod - Ravenous Machine 8 Bit.ogg")
                    pygame.mixer.music.play(-1)

                    invalids = (391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407,
                                408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 339, 340, 341, 342, 343,
                                344, 345, 346, 347, 348, 273, 299, 325, 351, 377, 288, 390, 267, 246, 247, 65, 91, 117,
                                143, 169, 195, 221, 247, 189, 183, 184, 157, 106, 111, 112, 113, 114, 115, 116, 60, 61,
                                62, 8, 15, 41, 67, 9, 10, 11, 12, 13, 14, 144, 145, 146, 147, 148, 149, 150, 151, 152,
                                153, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 104, 130, 156, 182, 208, 234, 260, 286,
                                312, 338, 364, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 248, 249, 250, 251,
                                252, 255, 256, 257, 258, 259, 303, 304, 305, 306, 307, 308, 309, 329, 354, 355, 356,
                                357, 358, 359, 360, 361, 313)

                    background = pygame.image.load("images/levels/second_level.jpg")
                    player = Player(0, display_height * TILE_SIZE - 80, 40, 40, "images/tiles/tile_level1.png")
                    e1 = FastEnemy(160, 480, 40, 40, "images/tiles/tile_level1.png", 6)
                    e2 = Enemy(0, 200, 40, 40, "images/tiles/tile_level1.png", 0)
                    e3 = Enemy(40, 240, 40, 40, "images/tiles/tile_level1.png", 0)
                    e4 = Enemy(280, 120, 40, 40, "images/tiles/tile_level1.png", 3)
                    e5 = Enemy(280, 40, 40, 40, "images/tiles/tile_level1.png", 0)
                    e6 = FastEnemy(600, 160, 40, 40, "images/tiles/tile_level1.png", 6)
                    e7 = FastEnemy(680, 240, 40, 40, "images/tiles/tile_level1.png", 6)
                    e8 = Enemy(600, 320, 40, 40, "images/tiles/tile_level1.png", 1)
                    e9 = Enemy(880, 320, 40, 40, "images/tiles/tile_level1.png", 1)

                    e10 = FastEnemy(760, 400, 40, 40, "images/tiles/tile_level1.png", 6)
                    e11 = Enemy(680, 480, 40, 40, "images/tiles/tile_level1.png", 1)
                    e12 = Enemy(760, 560, 40, 40, "images/tiles/tile_level1.png", 2)
                    e13 = Enemy(840, 560, 40, 40, "images/tiles/tile_level1.png", 3)

                    tiles.TileClass.total_tiles = 1
                    characters_classes.Enemy.score = 0
                    characters_classes.FastEnemy.score = 0
                    total_number_of_frames = 0

                    for y in range(0, game_display.get_height(), TILE_SIZE):
                        for x in range(0, game_display.get_width(), TILE_SIZE):
                            if TileClass.total_tiles in invalids:
                                TileClass(x, y, 'solid', 'level2')
                            else:
                                TileClass(x, y, 'empty')
                    level = 2

                if level3.is_mouse_selection(mousex, mousey):
                    for item in MenuItem.Group:
                        item.destroy(MenuItem)
                        for sprite in BaseClass.all_game_sprites:
                            BaseClass.destroy(sprite, sprite.type)
                            TileClass.empty_tiles()
                    pygame.mixer.music.load("sounds/game_music/Ensiferum - Battle Song 8 bit.ogg")
                    pygame.mixer.music.play(-1)

                    invalids = (391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407,
                                408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 365, 366, 367, 368, 369,
                                370, 371, 372, 339, 340, 341, 342, 343, 344, 313, 314, 315, 316, 287, 288, 289, 261,
                                262, 235, 383, 384, 385, 386, 387, 388, 389, 390, 359, 360, 361, 362, 363, 364, 335,
                                336, 337, 338, 310, 311, 312, 285, 286, 288, 260)

                    background = pygame.image.load("images/levels/third_level.jpg")

                    player = Player(360, 680, 40, 40, "images/tiles/tile_level1.png")
                    b1 = Boss(600, 360, 300, 128, "images/animations/bossAnimation/boss.png")

                    tiles.TileClass.total_tiles = 1
                    characters_classes.Enemy.score = 0
                    characters_classes.FastEnemy.score = 0
                    total_number_of_frames = 0

                    for y in range(0, game_display.get_height(), TILE_SIZE):
                        for x in range(0, game_display.get_width(), TILE_SIZE):
                            if TileClass.total_tiles in invalids:
                                TileClass(x, y, 'solid', 'level3')
                            else:
                                TileClass(x, y, 'empty')

                    level = 3

        pygame.display.update()

    # controls page
    elif level == 5:
        game_display.blit(background, (0, 0))
        BaseClass.all_game_sprites.draw(game_display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if back.is_mouse_selection(mousex, mousey):
                    for item in MenuItem.Group:
                        item.destroy(MenuItem)
                        for sprite in BaseClass.all_game_sprites:
                            BaseClass.destroy(sprite, sprite.type)
                            TileClass.empty_tiles()
                    level = 0

        utils.help_menu_text(game_display, "Eliminate all enemies", 382, 60, 30,
                             (255, 0, 0))
        utils.help_menu_text(game_display, "to complete each level.", 382, 80, 30,
                             (255, 0, 0))

        utils.help_menu_text(game_display, "A, D", 382, 160, 50, (255, 255, 255))
        utils.help_menu_text(game_display, "Movement: left & right", 382, 200, 30, (255, 255, 255))

        utils.help_menu_text(game_display, "MOUSE CLICK", 382, 280, 50, (255, 255, 255))
        utils.help_menu_text(game_display, "Shooting", 382, 320, 26, (255, 255, 255))

        utils.help_menu_text(game_display, "SPACE BAR", 382, 400, 50, (255, 255, 255))
        utils.help_menu_text(game_display, "Jumping", 382, 440, 26, (255, 255, 255))

        back = MenuItem(382, 480, 276, 100, "images/buttons/button_return.png")

        pygame.display.update()

    # title screen
    elif level == 0:
        if not music:
            # pygame.mixer.music.load("menu.ogg")
            # pygame.mixer.music.play(-1)
            music = True
        background = pygame.image.load("images/menu/main_menu.jpg")
        player = Player(-10000, -10000, 40, 40, "images/tiles/tile_level1.png")
        voivod_logo_1 = MenuItem(53, 240, 276, 276, "images/menu/voivod_logo.png")
        voivod_logo_2 = MenuItem(711, 240, 276, 276, "images/menu/voivod_logo.png")
        start = MenuItem(382, 120, 276, 100, "images/buttons/button_start.png")
        levels = MenuItem(382, 240, 276, 100, "images/buttons/button_levels.png")
        controls = MenuItem(382, 360, 276, 100, "images/buttons/button_help.png")
        quit_game = MenuItem(382, 480, 276, 100, "images/buttons/button_exit.png")

        game_display.blit(background, (0, 0))
        BaseClass.all_game_sprites.draw(game_display)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if start.is_mouse_selection(mousex, mousey):
                    pygame.mixer.music.load("sounds/game_music/Voivod - Brain Scan (8 Bit).ogg")
                    pygame.mixer.music.play(-1)
                    for item in MenuItem.Group:
                        item.destroy(MenuItem)

                    invalids = (360, 334, 308, 282, 256, 230, 204, 205, 206, 207, 208, 232, 258, 284, 310, 336, 362,
                                338, 257, 258, 259, 309, 310, 311, 361, 362, 329, 330, 331, 332, 371, 372, 373, 347,
                                348, 374, 327, 370, 386, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402,
                                403, 404, 405, 406, 407, 260, 312, 363, 364, 388, 390, 286, 234, 408, 409, 410, 411,
                                412, 413, 414, 415, 416, 417, 328, 333, 194, 195, 196, 197, 198, 235, 1, 79, 105, 131,
                                157, 280, 281, 255, 263, 262, 264, 57, 58, 59, 60, 117, 118, 119, 120, 261, 186, 106,
                                161, 132, 53, 27, 265, 266, 72, 73, 182)

                    background = pygame.image.load("images/levels/first_level.jpg")

                    player = Player(0, display_height * TILE_SIZE - 80, 40, 40, "images/tiles/tile_level1.png")
                    e1 = Enemy(600, 440, 40, 40, "images/tiles/tile_level1.png", 2)
                    e2 = Enemy(620, 560, 40, 40, "images/tiles/tile_level1.png", 3)
                    e3 = Enemy(740, 440, 40, 40, "images/tiles/tile_level1.png", 1)
                    e4 = Enemy(2, 320, 40, 40, "images/tiles/tile_level1.png", 0)
                    e5 = Enemy(880, 260, 40, 40, "images/tiles/tile_level1.png", 1)
                    e6 = Enemy(480, 260, 40, 40, "images/tiles/tile_level1.png", 1)
                    e7 = Enemy(160, 80, 40, 40, "images/tiles/tile_level1.png", 2)
                    e8 = Enemy(520, 160, 40, 40, "images/tiles/tile_level1.png", 3)
                    e9 = Enemy(800, 40, 40, 40, "images/tiles/tile_level1.png", 1)

                    tiles.TileClass.total_tiles = 1
                    characters_classes.Enemy.score = 0
                    characters_classes.FastEnemy.score = 0
                    total_number_of_frames = 0

                    for y in range(0, game_display.get_height(), TILE_SIZE):
                        for x in range(0, game_display.get_width(), TILE_SIZE):
                            if TileClass.total_tiles in invalids:
                                TileClass(x, y, 'solid')
                            else:
                                TileClass(x, y, 'empty')
                    level = 1

                if levels.is_mouse_selection(mousex, mousey):
                    for item in MenuItem.Group:
                        item.destroy(MenuItem)
                    voivod_logo_1 = MenuItem(53, 240, 276, 276, "images/menu/voivod_logo.png")
                    voivod_logo_2 = MenuItem(711, 240, 276, 276, "images/menu/voivod_logo.png")

                    level1 = MenuItem(382, 120, 276, 100, "images/buttons/button_level1.png")
                    level2 = MenuItem(382, 240, 276, 100, "images/buttons/button_level2.png")
                    level3 = MenuItem(382, 360, 276, 100, "images/buttons/button_level3.png")
                    back = MenuItem(382, 480, 276, 100, "images/buttons/button_return.png")

                    level = 4

                if controls.is_mouse_selection(mousex, mousey):
                    for item in MenuItem.Group:
                        item.destroy(MenuItem)
                    back = MenuItem(382, 480, 276, 100, "images/buttons/button_return.png")

                    level = 5

                if quit_game.is_mouse_selection(mousex, mousey):
                    pygame.quit()
                    sys.exit()

    clock.tick(fps)
