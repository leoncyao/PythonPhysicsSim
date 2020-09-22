import pygame
import time
import random
from Obj import *
# from Simulation import *
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 225)
white = (255, 255, 255)
black = (0, 0, 0)


def show_stat(Display, title, font, stat, pos, color):
    screen_title = font.render(title, True, color)
    screen_text = font.render(str(stat), True, color)
    Display.blit(screen_title, [pos[0], pos[1]])
    Display.blit(screen_text, [pos[0], pos[1]+15])

def spawn_obj(colour, mass, pos, vel, rad):
    """
    spawns Obj
    """
    temp = Obj(colour, mass, pos, vel, rad)
    return temp

def game():
    display_width = 1080
    display_height = 720
    center_screen_x = display_width / 2
    center_screen_y = display_height / 2

    pygame.init()
    font = pygame.font.SysFont(None, 20)

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 225)

    Display = pygame.display.set_mode((display_width, display_height))

    Running = True
    objects = []
    for i in range(2):
        cx = random.randint(-100, 100)
        cy = random.randint(-100, 100)
        bx = random.randint(-2, 2)/10
        by = random.randint(-2, 2)/10
        temp = Obj((255, 255, 255), 0.1, (int(center_screen_x + cx), int(center_screen_y + cy)), (bx, by), 5)
        objects.append(temp)
    # big = Obj((0, 0, 255), 1, (int(center_screen_x), int(center_screen_y)), (0, 0), 5)
    # big.dynamic = False
    # objects.append(big)
    # obj1 = Obj((255, 255, 255), 1, int(center_screen_x+100), int(center_screen_y+100), -1, 0)
    # obj2 = Obj((255, 255, 255), 3, int(center_screen_x), int(center_screen_y), 0, 0)
    # t = 0
    prev_time = 0
    while Running:
        Display.fill((0, 0, 0))
        ctime = time.perf_counter()
        if ctime - prev_time > 0.01:
            prev_time = ctime
            for obj in objects:
                obj.update_stats(objects)
        show_stat(Display, "Time", font, int(ctime), [25, 50], white)

        # if t % 10 == 0:
        #     for obj in objects:
        #         obj.update_stats(objects)
        # t += 1

        for obj in objects:
            obj.draw(Display)

        # show_stat("acel", str(obj1.acel_x) + " " + str(obj1.acel_y), (center_screen_x, center_screen_y-50), (255, 255, 25))
        # show_stat("vel", str(obj1.vel_x) + " " + str(obj1.vel_y), (center_screen_x, center_screen_y+100), (255, 255, 25))
        # show_stat("pos", str(obj1.pos_x) + " " + str(obj1.pos_y), (center_screen_x, center_screen_y), (255, 255, 25))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    temp = spawn_obj(red, 1, pygame.mouse.get_pos(), (0, 0), 5)
                    objects.append(temp)
        pygame.display.update()


if __name__ == "__main__":
    game()
