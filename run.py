import sys

import pygame
import warrior
import enemy
import random
pygame.init()

screen = pygame.display.set_mode((900, 700))
clock = pygame.time.Clock()

w = warrior.Warrior(200, 200, 40, 64, 5)

a = random.randint(0, 100)
b = random.randint(600, 700)
e = enemy.Enemy(random.randint(220, 900), random.choice([a,b]), 40, 64, 600, 0)
e2 = enemy.Enemy(random.randint(220, 900), random.choice([a,b]), 40, 64, 600, 0)
class change:
    def __init__(self):
        self.enemyLis = []
        self.enemyLis2 = []
        self.count = 0
    def kaung(self):
        a = random.randint(0, 100)
        b = random.randint(600, 700)
        for row in range(random.randint(-18, self.count)):
            e = enemy.Enemy(random.randint(220, 900), random.choice([a,b]), 40, 64, 600, 0)
            e2 = enemy.Enemy(random.randint(220, 900), random.choice([a,b]), 40, 64, 600, 0)
            self.enemyLis.append(e)
            self.enemyLis2.append(e2)
c = change()
c.kaung()



icon = pygame.image.load("enemy_image/ER1.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Warrior")
run = True
left = False
right = False
current = False
undirect = False
direct = False
prun = True
pa = False

def player():
    global left, right, current

    if w.attack is False and w.spell is False:
        if w.walkcount + 1 >= 27:
            w.walkcount = 0

        if left:
            screen.blit(w.wleft[w.walkcount//3], (w.x, w.y))
            w.walkcount += 1
        elif right:
            screen.blit(w.wright[w.walkcount//3], (w.x, w.y))
            w.walkcount += 1
        elif direct:
            screen.blit(w.s[w.walkcount//3], (w.x, w.y))
            w.walkcount += 1
        elif undirect:
            screen.blit(w.w[w.walkcount//3], (w.x, w.y))
            w.walkcount += 1
        else:
            if left and not right:
                screen.blit(w.wleft[0], (w.x, w.y))
            elif right and not left:
                screen.blit(w.wright[0], (w.x, w.y))
            else:
                screen.blit(w.wchar, (w.x, w.y))
                current = True
def attack():
    global left, right
    if w.attack_animation >= 27:
        w.attack_animation = 0
        w.attack_range = pygame.Rect(0,0,0,0)
        w.attack = False
        if left and not right:
            screen.blit(w.wleft[0], (w.x, w.y))
        if right and not left:
            screen.blit(w.wright[0], (w.x, w.y))
        if undirect:
            screen.blit(w.w[0], (w.x, w.y))
        if direct:
            screen.blit(w.s[0], (w.x, w.y))
        return

    if left and w.attack:
        w.attack_range = pygame.Rect(w.x-15, w.y, 30, w.height)
        screen.blit(w.aleft[w.attack_animation//3], (w.x, w.y))

    elif right and w.attack:
        w.attack_range = pygame.Rect(w.x+w.width, w.y, 30, w.height)
        screen.blit(w.aright[w.attack_animation//3], (w.x, w.y))

    elif undirect and w.attack:
        w.attack_range = pygame.Rect(w.x, w.y-15, 30, w.height)
        screen.blit(w.AW[w.attack_animation//3], (w.x, w.y))

    elif direct and w.attack:
        w.attack_range = pygame.Rect(w.x, w.y+15, 30, w.height)
        screen.blit(w.AS[w.attack_animation//3], (w.x, w.y))

    # w.attack_counter += 1
    # if w.attack_counter > 1:
    #     w.attack_animation += 1
    #     w.attack_counter = 0
    w.attack_animation += 1


def spell():
    global left, right
    if w.spell_animation >= 27:
        w.spell_animation = 0
        w.spell_range = pygame.Rect(0, 0, 0, 0)
        w.spell = False
        if left and not right:
            screen.blit(w.wleft[0], (w.x, w.y))
        if right and not left:
            screen.blit(w.wright[0], (w.x, w.y))
        return

    if left and w.spell:
        w.spell_range = pygame.Rect(w.x - 130, w.y, 30, w.height)
        screen.blit(w.sleft2[w.spell_animation // 3], (w.x, w.y))
        screen.blit(w.sleft[w.spell_animation // 3], (w.x-50, w.y))

    elif right and w.spell:
        w.spell_range = pygame.Rect(w.x + w.width + 100, w.y, 30, w.height)
        screen.blit(w.sright2[w.spell_animation // 3], (w.x, w.y))
        screen.blit(w.sright[w.spell_animation // 3], (w.x+38, w.y))

    elif direct and w.spell:
        w.spell_range = pygame.Rect(w.x, w.y+100+w.width, 37, w.height)
        screen.blit(w.SF2[w.spell_animation // 3], (w.x-3, w.y))
        screen.blit(w.SS[w.spell_animation // 3], (w.x-9, w.y+38))

    elif undirect and w.spell:
        w.spell_range = pygame.Rect(w.x, w.y-100-w.width, 37, w.height)
        screen.blit(w.SW2[w.spell_animation // 3], (w.x-4, w.y))
        screen.blit(w.SW[w.spell_animation // 3], (w.x-9, w.y-38))

    w.spell_animation += 1

class Enemy(object):
    @staticmethod
    def enemy():
        global pa
        e1_hit = False
        e2_hit = False
        if e.walkcount + 1 >= 27:
            e.walkcount = 0

        for ee in c.enemyLis[:]:  #if dont copy it will make flashimage
            if ee.walkcount + 1 >= 27:
                ee.walkcount = 0
            if ee.right is True:
                screen.blit(ee.eright[ee.walkcount // 3], (ee.x, ee.y))
                ee.walkcount += 1

            elif ee.left is True:
                screen.blit(ee.eleft[ee.walkcount // 3], (ee.x, ee.y))
                ee.walkcount += 1

            if ee.x > w.x + 20:
                ee.left = True
                ee.right = False
                ee.x -= ee.speed
            elif ee.x < w.x - 20:
                ee.right = True
                ee.left = False
                ee.x += ee.speed
                # Movement along y direction
            if ee.y < w.y:
                ee.y += ee.speed
            elif ee.y > w.y:
                ee.y -= ee.speed

            if ee.x < w.x+30 and ee.x > w.x-30 and ee.y < w.y+30 and ee.y > w.y-30:
                print("player was hit")
                e1_hit = True
                e2_hit = True

            if w.attack:
                if ee.x < w.attack_range.x+20 and ee.x > w.attack_range.x-20 and ee.y < w.attack_range.y+30 and ee.y > w.attack_range.y-30:
                    c.enemyLis.remove(ee)
            if w.spell:
                if left:
                    if ee.x < w.x and ee.x > w.spell_range.x-20 and ee.y < w.spell_range.y+30 and ee.y > w.spell_range.y-30:
                        if ee.right:
                            ee.x = ee.x - random.randint(200, 400)
                            ee.count += 1
                            if ee.count > 1:
                                c.enemyLis.remove(ee)
                elif right:
                    if ee.x < w.spell_range.x+20 and ee.x > w.x and ee.y < w.spell_range.y+30 and ee.y > w.spell_range.y-30:
                        if ee.left:
                            ee.x = ee.x + random.randint(200, 400)
                            ee.count += 1
                            if ee.count > 1:
                                c.enemyLis.remove(ee)
                elif direct:
                    if ee.x < w.spell_range.x+30 and ee.x > w.spell_range.x-30 and ee.y > w.y and ee.y < w.spell_range.y+30:
                        ee.y = ee.y + random.randint(200, 400)
                        ee.count += 1
                        if ee.count > 1:
                            c.enemyLis.remove(ee)
                elif undirect:
                    if ee.x < w.spell_range.x+30 and ee.x > w.spell_range.x-30 and ee.y < w.y and ee.y > w.spell_range.y-30:
                        ee.y = ee.y - random.randint(200, 400)
                        ee.count += 1
                        if ee.count > 1:
                            c.enemyLis.remove(ee)

        # enemy2
        for ee in c.enemyLis2[:]:  # if dont copy it will make flashimage
            if ee.walkcount + 1 >= 27:
                ee.walkcount = 0
            if ee.right is True:
                screen.blit(ee.eright2[ee.walkcount // 3], (ee.x, ee.y))
                ee.walkcount += 1

            elif ee.left is True:
                screen.blit(ee.eleft2[ee.walkcount // 3], (ee.x, ee.y))
                ee.walkcount += 1

            if ee.x > w.x + 20:
                ee.left = True
                ee.right = False
                ee.x -= ee.speed
            elif ee.x < w.x - 20:
                ee.right = True
                ee.left = False
                ee.x += ee.speed
                # Movement along y direction
            if ee.y < w.y:
                ee.y += ee.speed
            elif ee.y > w.y:
                ee.y -= ee.speed

            if ee.x < w.x + 30 and ee.x > w.x - 30 and ee.y < w.y + 30 and ee.y > w.y - 30:
                print("player was hit")
                e2_hit = True
                e1_hit = True

            if w.attack:
                if ee.x < w.attack_range.x + 20 and ee.x > w.attack_range.x - 20 and ee.y < w.attack_range.y + 30 and ee.y > w.attack_range.y - 30:
                    c.enemyLis2.remove(ee)
            if w.spell:
                if left:
                    if ee.x < w.x and ee.x > w.spell_range.x - 20 and ee.y < w.spell_range.y + 30 and ee.y > w.spell_range.y - 30:
                        if ee.right:
                            ee.x = ee.x - random.randint(200, 400)
                            ee.count += 1
                            if ee.count > 1:
                                c.enemyLis2.remove(ee)
                elif right:
                    if ee.x < w.spell_range.x + 20 and ee.x > w.x and ee.y < w.spell_range.y + 30 and ee.y > w.spell_range.y - 30:
                        if ee.left:
                            ee.x = ee.x + random.randint(200, 400)
                            ee.count += 1
                            if ee.count > 1:
                                c.enemyLis2.remove(ee)
                elif direct:
                    if ee.x < w.spell_range.x + 30 and ee.x > w.spell_range.x - 30 and ee.y > w.y and ee.y < w.spell_range.y + 30:
                        ee.y = ee.y + random.randint(200, 400)
                        ee.count += 1
                        if ee.count > 1:
                            c.enemyLis2.remove(ee)
                elif undirect:
                    if ee.x < w.spell_range.x + 30 and ee.x > w.spell_range.x - 30 and ee.y < w.y and ee.y > w.spell_range.y - 30:
                        ee.y = ee.y - random.randint(200, 400)
                        ee.count += 1
                        if ee.count > 1:
                            c.enemyLis2.remove(ee)
        if c.count >= 1:
            c.count = 0
        else:
            c.count += 1
            c.kaung()

        if e1_hit or e2_hit:
            pa = True
        if pa:
            c.enemyLis.clear()
            c.enemyLis2.clear()
            lose()

def display():
    player()
    # pygame.draw.rect(screen, (255, 0, 0), w.attack_range)
    # pygame.draw.rect(screen, (255, 0, 0), w.spell_range)
    attack()
    spell()
    Enemy.enemy()
    pygame.display.update()

font = pygame.font.SysFont(None, 60)
font2 = pygame.font.SysFont(None, 40)
font5 = pygame.font.SysFont(None, 28)
def text(text, font, color, surface, x, y):
    obj = font.render(text, 1, color)
    rect = obj.get_rect()
    rect.midtop = (x,y)
    surface.blit(obj, rect)
def menu():
    global prun
    run = True
    click = False

    while run:
        image = pygame.image.load("warrior_image/background_image.jpg")

        screen.blit(image, (0, 0))

        text("Warrior", font, (255,255,255), screen, 450, 110)

        mx, my = pygame.mouse.get_pos()
        b1 = pygame.Rect(350, 210, 210, 50)
        pygame.draw.rect(screen, (4, 146, 194), b1)
        text("Start", font2, (255, 255, 255), screen, 450, 222)

        b2 = pygame.Rect(350, 290, 210, 50)
        pygame.draw.rect(screen, (4, 146, 194), b2)
        text("Quit", font2, (255, 255, 255), screen, 450, 301)

        text("Enter to use spell", font5, (4, 146, 194), screen, 100, 70)
        text("Space to attack", font5, (4, 146, 194), screen, 100, 101)

        if b1.collidepoint((mx, my)):
            if click:
                play()
        if b2.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()

font3 = pygame.font.SysFont(None, 30)
def play():
    global current, direct, undirect, right, left, prun
    prun = True
    click = False
    time = 0
    time2 = 0
    count = 20

    while prun:
        background = pygame.image.load("warrior_image/terrain.jpg")
        background = pygame.transform.scale(background, (900, 700))
        screen.fill((0,0,0))
        screen.blit(background, (0,0))

        mx, my = pygame.mouse.get_pos()
        b1 = pygame.Rect(410, 0, 80, 20)
        pygame.draw.rect(screen, (4, 146, 194), b1)
        text("Menu", font3, (255,255,255), screen, 450, 0)

        time = str(time)
        # score = pygame.Rect(410, 680, 80, 20)
        # pygame.draw.rect(screen, (255,0,0), score)
        text(f"Score: {time}", font3, (255,255,255), screen, 450, 677)
        time = int(time)

        time2 += 1
        if time2 == count:
            time += 1
            count += 20

        if b1.collidepoint(mx,my):
            if click:
                c.enemyLis.clear()
                c.enemyLis2.clear()
                w.x = 200
                w.y =200
                current = True
                left = False
                right = False
                direct = False
                undirect = False
                w.attack = False
                w.spell = False
                prun = False

        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click =True
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:
            #         run = False
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and w.y > 0:
            w.y -= w.speed
            undirect = True
            direct = False
            w.attack = False
            current = False
            w.spell = False
            right = False
            left = False
            if key[pygame.K_LEFT] and w.x > 0:
                w.x -= w.speed
                left = True
                right = False
                w.attack = False
                current = False
                w.spell = False
                direct = False
                undirect = False
            if key[pygame.K_RIGHT] and w.x < 900 - w.width:
                w.x += w.speed
                right = True
                left = False
                w.attack = False
                current = False
                w.spell = False
                direct = False
                undirect = False

        elif key[pygame.K_DOWN] and w.y < 700 - w.height:
            w.y += w.speed
            direct = True
            undirect = False
            w.attack = False
            current = False
            w.spell = False
            right = False
            left = False
            if key[pygame.K_RIGHT] and w.x < 900 - w.width:
                w.x += w.speed
                right = True
                left = False
                w.attack = False
                current = False
                w.spell = False
                direct = False
                undirect = False
            if key[pygame.K_LEFT] and w.x > 0:
                w.x -= w.speed
                left = True
                right = False
                w.attack = False
                current = False
                w.spell = False
                direct = False
                undirect = False

        elif key[pygame.K_LEFT] and w.x > 0:
            w.x -= w.speed
            left = True
            right = False
            w.attack = False
            current = False
            w.spell = False
            direct = False
            undirect = False

        elif key[pygame.K_RIGHT] and w.x < 900 - w.width:
            w.x += w.speed
            right = True
            left = False
            w.attack = False
            current = False
            w.spell = False
            direct = False
            undirect = False

        else:
            # right = False
            # left = False
            w.walkcount = 0

        if not current:
            if key[pygame.K_SPACE]:
                w.attack = True
                w.spell = False

        if not current:
            if key[pygame.K_RETURN]:
                w.spell = True
                w.attack = False
        display()

font4 = pygame.font.SysFont(None, 20)
def lose():
    global pa, current, left, right, direct, undirect
    run = True
    click = False
    while run:
        screen.fill((0, 0, 0))
        text("Player was hit ", font3, (255, 255, 255), screen, 450, 250)
        text("Press Enter to restart to play", font4, (255, 255, 255), screen, 450, 320)

        mx, my = pygame.mouse.get_pos()
        m = pygame.Rect(410, 0, 80, 20)
        pygame.draw.rect(screen, (4, 146, 194), m)
        text("Menu", font3, (255,255,255), screen, 450, 0)

        if m.collidepoint(mx, my):
            if click:
                pa = False
                w.x = 200
                w.y = 200
                current = True
                left = False
                right = False
                direct = False
                undirect = False
                w.attack = False
                w.spell = False
                run = False
                menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_RETURN:
                    pa = False
                    w.x = 200
                    w.y = 200
                    current = True
                    left = False
                    right = False
                    direct = False
                    undirect = False
                    w.attack = False
                    w.spell = False
                    play()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

menu()
pygame.quit()