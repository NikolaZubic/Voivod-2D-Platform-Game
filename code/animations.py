# author: Nikola Zubic
import pygame

player_idle = [pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/idle/Idle (1).png"), (40, 40)),
               pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/idle/Idle (2).png"), (40, 40)),
               pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/idle/Idle (3).png"), (40, 40)),
               pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/idle/Idle (4).png"), (40, 40)),
               pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/idle/Idle (5).png"), (40, 40)),
               pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/idle/Idle (6).png"), (40, 40)),
               pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/idle/Idle (7).png"), (40, 40)),
               pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/idle/Idle (8).png"), (40, 40)),
               pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/idle/Idle (9).png"), (40, 40)),
               pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/idle/Idle (10).png"), (40, 40))]

player_running = [pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/run/Run (1).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/run/Run (2).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/run/Run (3).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/run/Run (4).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/run/Run (5).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/run/Run (6).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/run/Run (7).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/run/Run (8).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/run/Run (9).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/run/Run (10).png"), (40, 40))]

player_jumping = [pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/jump/Jump (1).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/jump/Jump (2).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/jump/Jump (3).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/jump/Jump (4).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/jump/Jump (5).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/jump/Jump (6).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/jump/Jump (7).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/jump/Jump (8).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/jump/Jump (9).png"), (40, 40)),
                  pygame.transform.scale(pygame.image.load("images/animations/playerAnimation/jump/Jump (10).png"), (40, 40))]

wraith_walking = [pygame.transform.scale(pygame.image.load(
    'images/animations/wraithAnimation/walk/Wraith_02_Moving Forward_000.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/wraithAnimation/walk/Wraith_02_Moving Forward_001.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/wraithAnimation/walk/Wraith_02_Moving Forward_002.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/wraithAnimation/walk/Wraith_02_Moving Forward_003.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/wraithAnimation/walk/Wraith_02_Moving Forward_004.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/wraithAnimation/walk/Wraith_02_Moving Forward_005.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/wraithAnimation/walk/Wraith_02_Moving Forward_006.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/wraithAnimation/walk/Wraith_02_Moving Forward_007.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/wraithAnimation/walk/Wraith_02_Moving Forward_008.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/wraithAnimation/walk/Wraith_02_Moving Forward_009.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/wraithAnimation/walk/Wraith_02_Moving Forward_010.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/wraithAnimation/walk/Wraith_02_Moving Forward_011.png'),
                                         (50, 50))]

wraith_idle = [pygame.transform.scale(pygame.image.load(
    'images/animations/wraithAnimation/idle/Wraith_02_Idle_000.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/idle/Wraith_02_Idle_001.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/idle/Wraith_02_Idle_002.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/idle/Wraith_02_Idle_003.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/idle/Wraith_02_Idle_004.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/idle/Wraith_02_Idle_005.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/idle/Wraith_02_Idle_006.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/idle/Wraith_02_Idle_007.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/idle/Wraith_02_Idle_008.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/idle/Wraith_02_Idle_009.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/idle/Wraith_02_Idle_010.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/idle/Wraith_02_Idle_011.png'), (50, 50))]

wraith_dead = [pygame.transform.scale(pygame.image.load(
    'images/animations/wraithAnimation/dying/Wraith_02_Dying_000.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/dying/Wraith_02_Dying_001.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/dying/Wraith_02_Dying_002.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/dying/Wraith_02_Dying_003.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/dying/Wraith_02_Dying_004.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/dying/Wraith_02_Dying_005.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/dying/Wraith_02_Dying_006.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/dying/Wraith_02_Dying_007.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/dying/Wraith_02_Dying_008.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/dying/Wraith_02_Dying_009.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/dying/Wraith_02_Dying_010.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/dying/Wraith_02_Dying_011.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/dying/Wraith_02_Dying_012.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/dying/Wraith_02_Dying_013.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/wraithAnimation/dying/Wraith_02_Dying_014.png'), (50, 50))]

fast_wraith_walking = [pygame.transform.scale(pygame.image.load(
    'images/animations/fastWraithAnimation/walk/Wraith_03_Moving Forward_000.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/fastWraithAnimation/walk/Wraith_03_Moving Forward_001.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/fastWraithAnimation/walk/Wraith_03_Moving Forward_002.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/fastWraithAnimation/walk/Wraith_03_Moving Forward_003.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/fastWraithAnimation/walk/Wraith_03_Moving Forward_004.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/fastWraithAnimation/walk/Wraith_03_Moving Forward_005.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/fastWraithAnimation/walk/Wraith_03_Moving Forward_006.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/fastWraithAnimation/walk/Wraith_03_Moving Forward_007.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/fastWraithAnimation/walk/Wraith_03_Moving Forward_008.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/fastWraithAnimation/walk/Wraith_03_Moving Forward_009.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/fastWraithAnimation/walk/Wraith_03_Moving Forward_010.png'),
                                         (50, 50)),
                  pygame.transform.scale(pygame.image.load(
                      'images/animations/fastWraithAnimation/walk/Wraith_03_Moving Forward_011.png'),
                                         (50, 50))]

fast_wraith_idle = [pygame.transform.scale(pygame.image.load(
    'images/animations/fastWraithAnimation/idle/Wraith_03_Idle_000.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/idle/Wraith_03_Idle_001.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/idle/Wraith_03_Idle_002.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/idle/Wraith_03_Idle_003.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/idle/Wraith_03_Idle_004.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/idle/Wraith_03_Idle_005.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/idle/Wraith_03_Idle_006.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/idle/Wraith_03_Idle_007.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/idle/Wraith_03_Idle_008.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/idle/Wraith_03_Idle_009.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/idle/Wraith_03_Idle_010.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/idle/Wraith_03_Idle_011.png'), (50, 50))]

fast_wraith_dead = [pygame.transform.scale(pygame.image.load(
    'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_000.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_001.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_002.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_003.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_004.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_005.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_006.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_007.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_008.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_009.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_010.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_011.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_012.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_013.png'), (50, 50)),
               pygame.transform.scale(pygame.image.load(
                   'images/animations/fastWraithAnimation/dying/Wraith_03_Dying_014.png'), (50, 50))]
