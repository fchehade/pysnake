import pygame
import settings
from scoreboard import Scoreboard
from apple import Apple
from snake import Snake
from enemy import Enemy, XMovingEnemy, YMovingEnemy


class Game:
    def __init__(
        self,
        width: int = settings.WIDTH,
        height: int = settings.HEIGHT,
        fps: int = settings.FRAME_RATE,
    ) -> None:
        self.width = width
        self.height = height
        self.screen = None
        self.running = True
        self.fps = fps
        self.scoreboard = Scoreboard()
        self.enemy_list = [Enemy()]
        self.xmoving_enemy_list: list[XMovingEnemy] = []
        self.ymoving_enemy_list: list[YMovingEnemy] = []
        self.apple = Apple()
        self.snake = Snake()

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.apple._generate_new_position()
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.snake.move_up()
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.snake.move_down()
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.snake.move_left()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.snake.move_right()

    def on_apple_collected(self):
        self.apple._generate_new_position()
        self.scoreboard.add_score()
        self.scoreboard.update_score_text()
        if self.scoreboard.score % 2 == 0:
            self.enemy_list.append(Enemy())
        if self.scoreboard.score % 3 == 0:
            self.xmoving_enemy_list.append(XMovingEnemy())
        if self.scoreboard.score % 5 == 0:
            self.ymoving_enemy_list.append(YMovingEnemy())
        for enemy in self.enemy_list:
            enemy._generate_new_position()
        if not self.xmoving_enemy_list:
            return
        if not self.xmoving_enemy_list:
            return
        for moving_enemy in self.xmoving_enemy_list:
            moving_enemy._generate_new_position()
        for moving_enemy in self.ymoving_enemy_list:
            moving_enemy._generate_new_position()

    def render(self):
        self.screen.blits(
            [
                (self.scoreboard.score_text, self.scoreboard.position),
                (self.apple.surface, self.apple.position),
                (self.snake.surface, self.snake.head),
            ]
        )
        for enemy in self.enemy_list:
            self.screen.blit(enemy.surface, enemy.position)
        for moving_enemy in self.xmoving_enemy_list:
            self.screen.blit(moving_enemy.surface, moving_enemy.position)
        for moving_enemy in self.ymoving_enemy_list:
            self.screen.blit(moving_enemy.surface, moving_enemy.position)

    def update_enemies(self):
        for moving_enemy in self.xmoving_enemy_list:
            moving_enemy.move_sideways()
            if moving_enemy.out_of_bounds_left_right(self.left, self.right):
                moving_enemy.direction = not moving_enemy.direction
        for moving_enemy in self.ymoving_enemy_list:
            moving_enemy.move_up_and_down()
            if moving_enemy.out_of_bounds_top_bottom(self.top, self.bottom):
                moving_enemy.direction = not moving_enemy.direction

    def run(self):
        pygame.init()
        pygame.display.set_caption("PySnake")
        clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        screen_rect = self.screen.get_rect()
        self.left, self.right, self.top, self.bottom = (
            screen_rect.left,
            screen_rect.right,
            screen_rect.top,
            screen_rect.bottom,
        )
        while self.running:
            self.screen.fill(settings.BLACK)
            self.check_input()
            self.snake.update_position()
            self.update_enemies()
            if self.snake.collided(self.apple.position):
                self.on_apple_collected()
            if self.snake.out_of_bounds(self.left, self.right, self.top, self.bottom):
                self.running = False
            for enemy_type in [
                self.enemy_list,
                self.xmoving_enemy_list,
                self.ymoving_enemy_list,
            ]:
                for enemy in enemy_type:
                    if self.snake.collided(enemy.position):
                        self.running = False
            self.render()
            pygame.display.flip()
            clock.tick(self.fps)

        pygame.quit()
