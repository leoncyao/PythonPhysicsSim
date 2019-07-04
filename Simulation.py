import pygame
import time
import random
from Tools import *
from Obj import *
# from Simulation import *
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 225)
white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
font = pygame.font.SysFont(None, 20)
g = 6.67 * 10 ** -11
class Simulation:
    def __init__(self, screen_dim: tuple):
        self.objects = []
        self.display_width = screen_dim[0]
        self.display_height = screen_dim[1]
        self.center_screen_x = self.display_width / 2
        self.center_screen_y = self.display_height / 2
        # self.Display = pygame.display.set_mode((self.display_width, self.display_height))

    def get_total_kinetic_energy(self):
        total_k = 0
        for object in self.objects:
            total_k += 0.5 * object.mass * math.pow(object.get_velocity(), 2)
        return total_k

    def get_gravitational_potential_energy(self):
        total_pe = 0
        pairs = self.get_pairs_of_objects()
        for pair in pairs:
            dist_x = abs(pair[0].pos_x - pair[1].pos_x)
            dist_y = abs(pair[0].pos_y - pair[1].pos_y)
            total_dist = math.sqrt(math.pow(dist_x, 2) + math.pow(dist_y, 2))  # * 1000 * 1000
            pe = pair[0].mass*pair[1].mass/total_dist  # * g
            total_pe += -1*2*pe
        return total_pe

    def check_collisions(self):
        pairs = self.get_pairs_of_objects()
        for pair in pairs:
            sum_radius = pair[0].rad + pair[1].rad
            # print(sum_radius)
            contact_angle = find_angle(pair[0].pos_x, pair[0].pos_y, pair[1].pos_x, pair[1].pos_y)
            dist_x = abs(pair[0].pos_x - pair[1].pos_x)
            dist_y = abs(pair[0].pos_y - pair[1].pos_y)
            print("distx {} dist y contact_angle {} ".format(contact_angle, dist_x, dist_y))

    def get_pairs_of_objects(self):
        pairs = []
        i = 0
        while i < len(self.objects) - 1:
            j = i + 1
            while j <= len(self.objects) - 1:
                pairs.append((self.objects[i], self.objects[j]))
                j += 1
            i += 1
        return pairs

    def test_system(self, num_particles):
        """testing example"""
        test_objects = []
        for i in range(num_particles):
            cx = random.randint(-200, 200)
            cy = random.randint(-200, 200)
            bx = random.randint(-2, 2)
            by = random.randint(-2, 2)
            # bx = 0
            # by = 0
            temp = Obj((255, 255, 255), 1, (int(self.center_screen_x + cx), int(self.center_screen_y + cy)), (bx, by), 5)
            test_objects.append(temp)
        big = Obj((0, 0, 255), 10, (int(self.center_screen_x), int(self.center_screen_y)), (0, 0), 5)
        # big.dynamic = False
        test_objects.append(big)
        return test_objects

    def run_simulation(self):
        """runs simulation"""

        Display = pygame.display.set_mode((self.display_width, self.display_height))
        prev_time = 0
        Running = True
        self.objects.extend(self.test_system(3))  # for testing
        while Running:
            stats = []
            Display.fill((0, 0, 0))
            ctime = time.clock()
            if ctime - prev_time > 0.01:
                prev_time = ctime
                for obj in self.objects:
                    obj.update_stats(self.objects)
                # self.check_collisions()
            # total_pe = self.get_gravitational_potential_energy()
            kinetic_energy = self.get_total_kinetic_energy()
            stats.append(("Time", int(ctime)))
            # stats.append(("Potential Energy", total_pe))
            stats.append(("Kinetic Energy", kinetic_energy))
            # stats.append(("K + U", kinetic_energy + total_pe))
            show_stats(Display, stats, font, [25, 50])
            # if t % 10 == 0:
            #     for obj in objects:
            #         obj.update_stats(objects)
            # t += 1

            for obj in self.objects:
                obj.draw(Display)

            # show_stat("acel", str(obj1.acel_x) + " " + str(obj1.acel_y), (center_screen_x, center_screen_y-50), (255, 255, 25))
            # show_stat("vel", str(obj1.vel_x) + " " + str(obj1.vel_y), (center_screen_x, center_screen_y+100), (255, 255, 25))
            # show_stat("pos", str(obj1.pos_x) + " " + str(obj1.pos_y), (center_screen_x, center_screen_y), (255, 255, 25))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        temp = spawn_obj(red, 3, pygame.mouse.get_pos(), (0, 0), 5)
                        self.objects.append(temp)
            pygame.display.update()

def show_stats(Display, stats, font, start_pos):
    i = 0
    for stat in stats:
        show_stat(Display, stat[0], font, stat[1], [start_pos[0], start_pos[1]+i*30], white)
        i += 1

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

if __name__ == "__main__":
    # game()
    test = Simulation((1080, 720))
    test.run_simulation()
