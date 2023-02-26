import pygame
from helper import constants
import time
from game.Round import Round
import sys


clock = pygame.time.Clock()
pygame.display.set_caption("Curling")
pygame.init()


class Match:
    """Main class for game loop."""
    def __init__(self, screen, parameters):
        """
        Parameterized constructor.
        :param screen: Surface where game is drawn.
        :param parameters: Object of Parameters class with wanted values.
        """
        self.screen = screen
        self.set_parameters(parameters)
        self.no_rounds = parameters.rounds
        self.rounds = []
        self.current_round = 0
        for i in range(self.no_rounds):
            game_round = Round(i, self.screen, parameters.no_stones*2)
            game_round.add_stones()
            self.rounds.append(game_round)
        self.score = self.init_score()

    def set_parameters(self, parameters):
        """
        Method assignes values to parameters.
        :param parameters: Wanted parameters.
        """
        constants.mass = parameters.mass
        constants.mi = parameters.mi

    def init_score(self):
        score = []
        for i in range(self.no_rounds):
            d = {"home": 0, "away": 0}
            score.append(d)
        return score

    def calculate_score(self):
        """
        Method calculates score after every round.
        :return: (tuple) Home's and away's score.
        """
        home, away = 0, 0
        for i in range(self.current_round):
            home += self.score[i]["home"]
            away += self.score[i]["away"]
        return home, away

    def run(self):
        """
        Method for running all rounds in match.
        After every round is done, window shows match score at the moment.
        When all rounds are ran, proceeds to determine the winner.
        """
        for i in range(self.no_rounds):
            pygame.mixer.music.play(-1)
            self.rounds[i].match_score = self.calculate_score()
            self.rounds[i].run()
            home, away = self.rounds[i].score.values()
            self.score[self.current_round]["home"], self.score[self.current_round]["away"] = home, away
            start = time.time()
            while True:
                pygame.mixer.music.stop()
                if time.time() - start > 4:  # window will be shown for 4s before the next round begins.
                    self.current_round += 1
                    break
                self.screen.fill((0, 0, 0))
                self.match_score_text()
                self.match_score()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.update()
        self.winner()

    def match_score(self):
        """
        Method for showing a window with current result in match by rounds.
        """
        coef = 240/self.no_rounds
        x = 250
        for i in range(self.no_rounds):
            if self.current_round < i:
                home_score, away_score = ["/"]*2
            else:
                home_score = str(self.score[i]["home"])
                away_score = str(self.score[i]["away"])
            text_home_score = constants.font.render(home_score, True, constants.white)
            text_rect_home_score = text_home_score.get_rect(center=(x + (i+0.5) * coef, constants.round_score_h_y))
            text_away_score = constants.font.render(away_score, True, constants.white)
            text_rect_away_score = text_away_score.get_rect(center=(x + (i+0.5) * coef, constants.round_score_a_y))

            self.screen.blit(text_home_score, text_rect_home_score)
            self.screen.blit(text_away_score, text_rect_away_score)

    def match_score_text(self):
        """
        Method for displaying a text after the round is finished.
        Shows which round is finished.
        """
        text_round = constants.font_start.render("ROUND " + str(self.current_round + 1) + " DONE", True, constants.white)
        text_rect_round = text_round.get_rect(center=(250, 400))
        text_home = constants.font.render("HOME", True, constants.white)
        text_rect_home = text_home.get_rect(center=(constants.round_score_x, constants.round_score_h_y))
        text_away = constants.font.render("AWAY", True, constants.white)
        text_rect_away = text_away.get_rect(center=(constants.round_score_x, constants.round_score_a_y))

        self.screen.blit(text_home, text_rect_home)
        self.screen.blit(text_away, text_rect_away)
        self.screen.blit(text_round, text_rect_round)

    def winner(self):
        """
        Method for drawing end window.
        Depending on final score, text is being initialized.
        Shows the final score and winner.
        Last window in the application.
        """
        home, away = self.calculate_score()
        image = constants.winner_image
        if home > away:
            text = "HOME TEAM WON!"
        elif away > home:
            text = "AWAY TEAM WON!"
        else:
            text = "GAME IS TIED!"
            image = constants.tied_image
        result = "HOME " + str(home) + " : " + str(away) + " AWAY"

        text_winner = constants.font.render(text, True, constants.white)
        text_rect_winner = text_winner.get_rect(center=(250, 450))
        text_result = constants.font_start.render(result, True, constants.white)
        text_rect_result = text_result.get_rect(center=(250, 500))
        image_rect = image.get_rect(center=(250, 250))

        while True:
            self.screen.fill((0, 0, 0))
            self.screen.blit(text_winner, text_rect_winner)
            self.screen.blit(text_result, text_rect_result)
            self.screen.blit(image, image_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
