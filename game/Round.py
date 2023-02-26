from game import collisions
import sys
from gui.Slider import display
from game.Stone import *

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Curling")


class Round:
    """Class manages all aspects of one round in game."""
    def __init__(self, no, screen, no_stones):
        """
        Parameterized constructor.
        :param no: Round's number.
        :param screen: Surface where game is drawn.
        :param no_stones: Number of stones to play with.
        """
        self.no = no
        self.screen = screen
        self.no_stones = no_stones
        self.current_round = 0
        self.stones = []
        self.match_score = []
        self.score = {"home": 0, "away": 0}

    def add_stones(self):
        for i in range(self.no_stones):
            if i % 2 == 0:
                color = constants.green
            else:
                color = constants.yellow
            stone = Stone(self.screen, color)
            self.stones.append(stone)

    def all_stones_shot(self):
        """
        Method checks if all stones are shot.
        Helps to determine if round is finished.
        :return: (bool) True if all stones are shot, False if not
        """
        for stone in self.stones:
            if not stone.shot:
                return False
        return True

    def stones_shot(self):
        """
        Method for collecting stone that have been shot.
        Only stone that have been shot should be checked for possible collision.
        :return: (tuple) Shot stone.
        """
        stones = []
        for stone in self.stones:
            if stone.shot:
                stones.append(stone)
        return stones

    def not_moving(self):
        for stone in self.stones:
            if np.count_nonzero(stone.velocity) > 0:
                return False
        return True

    def update(self):
        for stone in self.stones:
            stone.update()

    def run(self):
        """
        Main method in Round class.
        Draws the curling's field.
        Draws stones. Calls methods for stones' motion.
        Checks collisions. Draws current score.
        Runs the loop while until all the stones have been shot.
        :return: (bool) True when round is done.
        """
        clicked = 0  # variable for solving problem between pyqt and pygame
        current = 0
        help = []
        while True:
            self.screen.fill((0, 0, 0))
            # drawing home's circles
            pygame.draw.rect(self.screen, (0, 0, 255), (100, 0, 300, 730), 6)
            pygame.draw.circle(self.screen, (0, 0, 255), (250, 150), 120, 0)
            pygame.draw.circle(self.screen, (255, 255, 255), (250, 150), 80, 0)
            pygame.draw.circle(self.screen, (255, 0, 0), (250, 150), 40, 0)
            pygame.draw.circle(self.screen, (255, 255, 255), (250, 150), 10, 0)
            i = 0
            while i < current + 1:  # drawing shot stones
                self.stones[i].draw()
                i += 1
            pygame.draw.line(self.screen, (134, 144, 144), (250, 650),
                             (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))  # drawing line for aiming the shot
            for event in pygame.event.get():
                position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and self.not_moving():
                    if not (clicked == 0 and self.no == 0):
                        angle = math.atan2(position[1] - constants.start_y, position[0] - constants.start_x)  # angle of the hit
                        velocity = display()
                        self.stones[current].initial_force(angle, velocity)  # starting the stone's motion
                        self.stones[current].shot = True
                        help.append("shot")
                    else:
                        clicked += 1
            self.update()
            collisions.wall_collision(self.stones)
            collisions.collision(self.stones_shot())
            if self.not_moving() and len(help) > 0:
                current += 1
                if current >= len(self.stones):
                    current = len(self.stones) - 1
                self.stones[current].draw()  # draws new stone and increases no of stones
                help = []
            self.show_score()  # drawing current match score
            if self.check_end():  # if round is done, call function and return true
                return True
            pygame.display.update()
            clock.tick(60)

    def show_score(self):
        """
        Method displays score of both teams on game's main display.
        """
        text_home = constants.font_start.render("HOME", True, constants.white)
        text_rect_home = text_home.get_rect(center=(50, 650))
        text_home_score = constants.font_start.render(str(self.match_score[0]), True, constants.white)
        text_rect_home_score = text_home_score.get_rect(center=(50,680))

        text_away = constants.font_start.render("AWAY", True, constants.white)
        text_rect_away = text_away.get_rect(center=(450, 650))
        text_away_score = constants.font_start.render(str(self.match_score[1]), True, constants.white)
        text_rect_away_score = text_away_score.get_rect(center=(450, 680))

        self.screen.blit(text_home, text_rect_home)
        self.screen.blit(text_home_score, text_rect_home_score)
        self.screen.blit(text_away, text_rect_away)
        self.screen.blit(text_away_score, text_rect_away_score)

    def check_end(self):
        """
        Method check if stone are not moving and if all of them have been shot.
        If True, proceeds to next method.
        :return: (bool) True if round is finished, False if not.
        """
        if self.not_moving() and self.all_stones_shot():
            self.end()
            return True
        return False

    def end(self):
        """
        Method gets tuple of stone sorted by the distance between their center and home's center.
        Calculates the score and update score attribute.
        """
        sorted_stone = sorted(self.stones, key=lambda x: x.center_distance(), reverse=False)
        color = sorted_stone[0].color
        self.score[constants.color_player[color]] = 1
        for i in range(1, len(sorted_stone)):
            if sorted_stone[i].color == color:
                self.score[constants.color_player[color]] += 1
            else:
                break
