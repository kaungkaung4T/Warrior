import pygame
import random
import warrior

w = warrior.Warrior(400, 200, 40, 64, 5)
class Enemy(object):
    def __init__(self, x, y, width, height, end, count):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.count = count
        self.path = [x, end]
        self.walkcount = 0
        self.speed = 2
        self.left = False
        self.right = False

        self.echar = pygame.image.load("warrior_image/F1.png")
        self.eright = [pygame.image.load("enemy_image/EER1.png"), pygame.image.load("enemy_image/EER2.png"),
                  pygame.image.load("enemy_image/EER3.png"), pygame.image.load("enemy_image/EER4.png"),
                  pygame.image.load("enemy_image/EER5.png"), pygame.image.load("enemy_image/EER6.png"),
                  pygame.image.load("enemy_image/EER7.png"), pygame.image.load("enemy_image/EER8.png"),
                  pygame.image.load("enemy_image/EER9.png")]


        self.eleft = [pygame.image.load("enemy_image/EEL1.png"), pygame.image.load("enemy_image/EEL2.png"),
                      pygame.image.load("enemy_image/EEL3.png"), pygame.image.load("enemy_image/EEL4.png"),
                      pygame.image.load("enemy_image/EEL5.png"), pygame.image.load("enemy_image/EEL6.png"),
                      pygame.image.load("enemy_image/EEL7.png"), pygame.image.load("enemy_image/EEL8.png"),
                      pygame.image.load("enemy_image/EEL9.png")]


        self.eright2 = [pygame.image.load("enemy_image/ER1.png"),pygame.image.load("enemy_image/ER2.png"),
                        pygame.image.load("enemy_image/ER3.png"),pygame.image.load("enemy_image/ER4.png"),
                        pygame.image.load("enemy_image/ER5.png"),pygame.image.load("enemy_image/ER6.png"),
                        pygame.image.load("enemy_image/ER7.png"),pygame.image.load("enemy_image/ER8.png"),
                        pygame.image.load("enemy_image/ER9.png")]

        self.eleft2 = [pygame.image.load("enemy_image/EL1.png"),pygame.image.load("enemy_image/EL2.png"),
                        pygame.image.load("enemy_image/EL3.png"),pygame.image.load("enemy_image/EL4.png"),
                        pygame.image.load("enemy_image/EL5.png"),pygame.image.load("enemy_image/EL6.png"),
                        pygame.image.load("enemy_image/EL7.png"),pygame.image.load("enemy_image/EL8.png"),
                        pygame.image.load("enemy_image/EL9.png")]

    # def move(self):
    #     if e.speed > 0:
    #         if e.x < e.path[1] + e.speed:
    #             e.x += e.speed
    #         else:
    #             e.speed = e.speed * -1
    #             e.x += e.speed
    #             e.walkcount = 0
    #     else:
    #         if e.x > e.path[0] - e.speed:
    #             e.x += e.speed
    #         else:
    #             e.speed = e.speed * -1
    #             e.x += e.speed
    #             e.walkcount = 0
