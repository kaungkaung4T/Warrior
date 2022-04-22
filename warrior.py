import pygame


class Warrior(object):
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.walkcount = 0

        self.attack = False
        self.attack_animation = 0
        self.attack_counter = 0
        self.attack_range = pygame.Rect(0,0,0,0)

        self.spell = False
        self.spell_animation = 0
        self.spell_range = pygame.Rect(0,0,0,0)

        self.wchar = pygame.image.load("warrior_image/F1.png")
        self.s = [pygame.image.load("warrior_image/F1.png"), pygame.image.load("warrior_image/F2.png"),
                  pygame.image.load("warrior_image/F3.png"), pygame.image.load("warrior_image/F4.png"),
                  pygame.image.load("warrior_image/F5.png"), pygame.image.load("warrior_image/F6.png"),
                  pygame.image.load("warrior_image/F7.png"), pygame.image.load("warrior_image/F8.png"),
                  pygame.image.load("warrior_image/F9.png")]

        self.w = [pygame.image.load("warrior_image/W1.png"), pygame.image.load("warrior_image/W2.png"),
                  pygame.image.load("warrior_image/W3.png"), pygame.image.load("warrior_image/W4.png"),
                  pygame.image.load("warrior_image/W5.png"), pygame.image.load("warrior_image/W6.png"),
                  pygame.image.load("warrior_image/W7.png"), pygame.image.load("warrior_image/W8.png"),
                  pygame.image.load("warrior_image/W9.png")]

        self.wright = [pygame.image.load("warrior_image/R1.png"), pygame.image.load("warrior_image/R2.png"),
                  pygame.image.load("warrior_image/R3.png"), pygame.image.load("warrior_image/R4.png"),
                  pygame.image.load("warrior_image/R5.png"), pygame.image.load("warrior_image/R6.png"),
                  pygame.image.load("warrior_image/R7.png"), pygame.image.load("warrior_image/R8.png"),
                  pygame.image.load("warrior_image/R9.png")]
        self.wleft = [pygame.image.load("warrior_image/L1.png"), pygame.image.load("warrior_image/L2.png"),
                 pygame.image.load("warrior_image/L3.png"), pygame.image.load("warrior_image/L4.png"),
                 pygame.image.load("warrior_image/L5.png"), pygame.image.load("warrior_image/L6.png"),
                 pygame.image.load("warrior_image/L7.png"), pygame.image.load("warrior_image/L8.png"),
                 pygame.image.load("warrior_image/L9.png")]



        # attack animation
        self.aright = [pygame.image.load("warrior_image/AR1.png"), pygame.image.load("warrior_image/AR2.png"),
                  pygame.image.load("warrior_image/AR3.png"),
                  pygame.image.load("warrior_image/AR5.png"), pygame.image.load("warrior_image/AR6.png"), pygame.image.load("warrior_image/AR6.png"),
                  pygame.image.load("warrior_image/AR6.png"), pygame.image.load("warrior_image/AR7.png"),
                        pygame.image.load("warrior_image/AR8.png")]

        self.aleft = [pygame.image.load("warrior_image/AL1.png"), pygame.image.load("warrior_image/AL2.png"),
                 pygame.image.load("warrior_image/AL3.png"),
                 pygame.image.load("warrior_image/AL5.png"), pygame.image.load("warrior_image/AL6.png"), pygame.image.load("warrior_image/AL6.png"),
                 pygame.image.load("warrior_image/AL6.png"), pygame.image.load("warrior_image/AL7.png"),
                        pygame.image.load("warrior_image/AL8.png")]

        self.AS = [pygame.image.load("warrior_image/AS1.png"), pygame.image.load("warrior_image/AS2.png"),
                 pygame.image.load("warrior_image/AS3.png"),
                 pygame.image.load("warrior_image/AS4.png"), pygame.image.load("warrior_image/AS5.png"), pygame.image.load("warrior_image/AS6.png"),
                 pygame.image.load("warrior_image/AS6.png"), pygame.image.load("warrior_image/AS7.png"),
                        pygame.image.load("warrior_image/AS8.png")]

        self.AW = [pygame.image.load("warrior_image/AW1.png"), pygame.image.load("warrior_image/AW2.png"),
                   pygame.image.load("warrior_image/AW3.png"),
                   pygame.image.load("warrior_image/AW4.png"), pygame.image.load("warrior_image/AW5.png"),
                   pygame.image.load("warrior_image/AW6.png"),
                   pygame.image.load("warrior_image/AW6.png"), pygame.image.load("warrior_image/AW7.png"),
                        pygame.image.load("warrior_image/AW8.png")]



        # spell animation
        self.sright = [pygame.image.load("warrior_image/spell/SR1.png"), pygame.image.load("warrior_image/spell/SR2.png"),
                    pygame.image.load("warrior_image/spell/SR3.png"), pygame.image.load("warrior_image/spell/SR4.png"),
                    pygame.image.load("warrior_image/spell/SR5.png"), pygame.image.load("warrior_image/spell/SR6.png"),
                    pygame.image.load("warrior_image/spell/SR7.png"), pygame.image.load("warrior_image/spell/SR8.png"),
                    pygame.image.load("warrior_image/spell/SR9.png")]

        self.sleft = [pygame.image.load("warrior_image/spell/SL1.png"), pygame.image.load("warrior_image/spell/SL2.png"),
                    pygame.image.load("warrior_image/spell/SL3.png"), pygame.image.load("warrior_image/spell/SL4.png"),
                    pygame.image.load("warrior_image/spell/SL5.png"), pygame.image.load("warrior_image/spell/SL6.png"),
                    pygame.image.load("warrior_image/spell/SL7.png"), pygame.image.load("warrior_image/spell/SL8.png"),
                    pygame.image.load("warrior_image/spell/SL9.png")]

        self.sright2 = [pygame.image.load("warrior_image/SSR1.png"), pygame.image.load("warrior_image/SSR2.png"),
                       pygame.image.load("warrior_image/SSR3.png"), pygame.image.load("warrior_image/SSR4.png"),
                       pygame.image.load("warrior_image/SSR5.png"), pygame.image.load("warrior_image/SSR5.png"),
                       pygame.image.load("warrior_image/SSR6.png"), pygame.image.load("warrior_image/SSR6.png"),
                       pygame.image.load("warrior_image/SSR7.png")]

        self.sleft2 = [pygame.image.load("warrior_image/SSL1.png"), pygame.image.load("warrior_image/SSL2.png"),
                      pygame.image.load("warrior_image/SSL3.png"), pygame.image.load("warrior_image/SSL4.png"),
                      pygame.image.load("warrior_image/SSL5.png"), pygame.image.load("warrior_image/SSL5.png"),
                      pygame.image.load("warrior_image/SSL6.png"), pygame.image.load("warrior_image/SSL6.png"),
                      pygame.image.load("warrior_image/SSL7.png")]

        self.SS = [pygame.image.load("warrior_image/spell/SF1.png"), pygame.image.load("warrior_image/spell/SF2.png"),
                        pygame.image.load("warrior_image/spell/SF3.png"), pygame.image.load("warrior_image/spell/SF4.png"),
                        pygame.image.load("warrior_image/spell/SF5.png"), pygame.image.load("warrior_image/spell/SF5.png"),
                        pygame.image.load("warrior_image/spell/SF6.png"), pygame.image.load("warrior_image/spell/SF6.png"),
                        pygame.image.load("warrior_image/spell/SF7.png")]

        self.SW = [pygame.image.load("warrior_image/spell/SW1.png"), pygame.image.load("warrior_image/spell/SW2.png"),
                       pygame.image.load("warrior_image/spell/SW3.png"), pygame.image.load("warrior_image/spell/SW4.png"),
                       pygame.image.load("warrior_image/spell/SW5.png"), pygame.image.load("warrior_image/spell/SW5.png"),
                       pygame.image.load("warrior_image/spell/SW6.png"), pygame.image.load("warrior_image/spell/SW6.png"),
                       pygame.image.load("warrior_image/spell/SW7.png")]

        self.SW2 = [pygame.image.load("warrior_image/SSW1.png"), pygame.image.load("warrior_image/SSW2.png"),
                       pygame.image.load("warrior_image/SSW3.png"), pygame.image.load("warrior_image/SSW4.png"),
                       pygame.image.load("warrior_image/SSW5.png"), pygame.image.load("warrior_image/SSW5.png"),
                       pygame.image.load("warrior_image/SSW6.png"), pygame.image.load("warrior_image/SSW6.png"),
                       pygame.image.load("warrior_image/SSW7.png")]


        self.SF2 = [pygame.image.load("warrior_image/SSF1.png"), pygame.image.load("warrior_image/SSF2.png"),
                       pygame.image.load("warrior_image/SSF3.png"), pygame.image.load("warrior_image/SSF4.png"),
                       pygame.image.load("warrior_image/SSF5.png"), pygame.image.load("warrior_image/SSF5.png"),
                       pygame.image.load("warrior_image/SSF6.png"), pygame.image.load("warrior_image/SSF6.png"),
                       pygame.image.load("warrior_image/SSF7.png")]