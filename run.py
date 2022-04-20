import pygame
import warrior
import enemy
import random
pygame.init()

screen = pygame.display.set_mode((900, 700))
clock = pygame.time.Clock()

w = warrior.Warrior(200, 200, 40, 64, 5)
e = enemy.Enemy(random.randint(220, 900), random.randint(0, 700), 40, 64, 600, 0)
e2 = enemy.Enemy(random.randint(220, 900), random.randint(0, 700), 40, 64, 600, 0)
class change:
    def __init__(self):
        self.enemyLis = []
        self.enemyLis2 = []
        self.count = 0
    def kaung(self):
        for row in range(random.randint(-18, self.count)):
            e = enemy.Enemy(random.randint(220, 900), random.randint(0, 700), 40, 64, 600, 0)
            e2 = enemy.Enemy(random.randint(220, 900), random.randint(0, 700), 40, 64, 600, 0)
            self.enemyLis.append(e)
            self.enemyLis2.append(e2)
c = change()
c.kaung()





pygame.display.set_caption("Warrior")
run = True
left = False
right = False
current = False
undirect = False
direct = False

def player():
    global left, right, current
    background = pygame.image.load("warrior_image/terrain.jpg")
    background = pygame.transform.scale(background, (900, 700))
    screen.fill((0,0,0))
    screen.blit(background, (0,0))


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

class e2(object):
    @staticmethod
    def enemy():
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


def display():
    player()
    pygame.draw.rect(screen, (255, 0, 0), w.attack_range)
    pygame.draw.rect(screen, (255, 0, 0), w.spell_range)
    attack()
    spell()
    e2.enemy()
    pygame.display.update()


while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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


pygame.quit()