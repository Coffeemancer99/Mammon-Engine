import pygame
"""
Keyset configurations for controls, to be imported into a Player Object
"""
singleplayer = {
    'up': pygame.K_w,
    'down': pygame.K_s,
    'left': pygame.K_a,
    'right': pygame.K_d,
    'space': pygame.K_SPACE,
    'action':pygame.K_j,
    'special':pygame.K_k
}
twoPlayer = [ # fits two players on the keyboard
    {
        'up': pygame.K_w,
        'down': pygame.K_s,
        'left': pygame.K_a,
        'right': pygame.K_d,
        'space': pygame.K_c,
        'action': pygame.K_v,
        'special': pygame.K_b
    },
    {
        'up': pygame.K_UP,
        'down': pygame.K_DOWN,
        'left': pygame.K_LEFT,
        'right': pygame.K_RIGHT,
        'space': pygame.K_l,
        'action': pygame.K_k,
        'special': pygame.K_j
    }
]