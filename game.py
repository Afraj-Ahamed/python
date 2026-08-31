import pygame
import random
import sys

# -------------------- SETUP --------------------
pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GRAY = (100, 100, 100)
RED = (200, 30, 30)
BLUE = (30, 30, 200)
YELLOW = (255, 220, 0)

# Road settings
ROAD_WIDTH = 300
ROAD_LEFT = (WIDTH - ROAD_WIDTH) // 2
ROAD_RIGHT = ROAD_LEFT + ROAD_WIDTH

LANE_COUNT = 3
LANE_WIDTH = ROAD_WIDTH // LANE_COUNT

CAR_WIDTH = 50
CAR_HEIGHT = 90

font = pygame.font.SysFont("arial", 28)
big_font = pygame.font.SysFont("arial", 48)


def lane_x(lane_index, car_width):
    """Return the x position (left edge) to center a car in a given lane."""
    lane_center = ROAD_LEFT + lane_index * LANE_WIDTH + LANE_WIDTH // 2
    return lane_center - car_width // 2


class PlayerCar:
    def __init__(self):
        self.lane = 1  # start in the middle lane
        self.width = CAR_WIDTH
        self.height = CAR_HEIGHT
        self.x = lane_x(self.lane, self.width)
        self.y = HEIGHT - self.height - 20
        self.speed = LANE_WIDTH  # how far one lane-change moves (for smooth slide)
        self.target_x = self.x

    def move_left(self):
        if self.lane > 0:
            self.lane -= 1
            self.target_x = lane_x(self.lane, self.width)

    def move_right(self):
        if self.lane < LANE_COUNT - 1:
            self.lane += 1
            self.target_x = lane_x(self.lane, self.width)

    def update(self):
        # smooth slide toward target lane
        if self.x < self.target_x:
            self.x = min(self.x + 10, self.target_x)
        elif self.x > self.target_x:
            self.x = max(self.x - 10, self.target_x)

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        draw_car(surface, self.x, self.y, self.width, self.height, BLUE)


class EnemyCar:
    def __init__(self, speed):
        self.width = CAR_WIDTH
        self.height = CAR_HEIGHT
        self.lane = random.randint(0, LANE_COUNT - 1)
        self.x = lane_x(self.lane, self.width)
        self.y = -self.height
        self.speed = speed
        self.color = random.choice([RED, YELLOW, GRAY])

    def update(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > HEIGHT

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        draw_car(surface, self.x, self.y, self.width, self.height, self.color)


def draw_car(surface, x, y, w, h, color):
    """Draw a simple car shape: body + windows."""
    body = pygame.Rect(x, y, w, h)
    pygame.draw.rect(surface, color, body, border_radius=10)
    # windshield
    pygame.draw.rect(surface, (200, 230, 255), (x + 8, y + 12, w - 16, 20), border_radius=4)
    # rear window
    pygame.draw.rect(surface, (200, 230, 255), (x + 8, y + h - 30, w - 16, 18), border_radius=4)
    # wheels
    pygame.draw.rect(surface, BLACK, (x - 4, y + 10, 6, 20))
    pygame.draw.rect(surface, BLACK, (x + w - 2, y + 10, 6, 20))
    pygame.draw.rect(surface, BLACK, (x - 4, y + h - 30, 6, 20))
    pygame.draw.rect(surface, BLACK, (x + w - 2, y + h - 30, 6, 20))


def draw_road(surface, scroll_y):
    surface.fill((50, 150, 50))  # grass
    pygame.draw.rect(surface, GRAY, (ROAD_LEFT, 0, ROAD_WIDTH, HEIGHT))

    # road edge lines
    pygame.draw.rect(surface, WHITE, (ROAD_LEFT - 5, 0, 5, HEIGHT))
    pygame.draw.rect(surface, WHITE, (ROAD_RIGHT, 0, 5, HEIGHT))

    # lane dashes that scroll to feel like movement
    dash_height = 30
    gap = 20
    for lane in range(1, LANE_COUNT):
        x = ROAD_LEFT + lane * LANE_WIDTH
        y = (scroll_y % (dash_height + gap)) - (dash_height + gap)
        while y < HEIGHT:
            pygame.draw.rect(surface, WHITE, (x - 2, y, 4, dash_height))
            y += dash_height + gap


def show_text_center(surface, text, font_obj, color, y):
    label = font_obj.render(text, True, color)
    rect = label.get_rect(center=(WIDTH // 2, y))
    surface.blit(label, rect)


def game_loop():
    player = PlayerCar()
    enemies = []

    score = 0
    scroll_y = 0
    base_speed = 5
    spawn_timer = 0
    spawn_delay = 60  # frames between spawns, gets smaller (harder) over time

    running = True
    game_over = False

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key in (pygame.K_LEFT, pygame.K_a):
                        player.move_left()
                    if event.key in (pygame.K_RIGHT, pygame.K_d):
                        player.move_right()
                else:
                    if event.key == pygame.K_r:
                        return game_loop()  # restart
                    if event.key == pygame.K_q:
                        running = False

        if not game_over:
            current_speed = base_speed + score // 100  # gets faster as score grows

            player.update()
            scroll_y += current_speed

            # spawn enemy cars
            spawn_timer += 1
            if spawn_timer >= max(20, spawn_delay - score // 20):
                spawn_timer = 0
                enemies.append(EnemyCar(current_speed))

            # update enemies
            for enemy in enemies[:]:
                enemy.update()
                if enemy.off_screen():
                    enemies.remove(enemy)
                    score += 10

            # collision check
            player_rect = player.rect()
            for enemy in enemies:
                if player_rect.colliderect(enemy.rect()):
                    game_over = True

        # -------------------- DRAW --------------------
        draw_road(screen, scroll_y)
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        score_label = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_label, (10, 10))

        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(180)
            overlay.fill(BLACK)
            screen.blit(overlay, (0, 0))
            show_text_center(screen, "GAME OVER", big_font, RED, HEIGHT // 2 - 40)
            show_text_center(screen, f"Final Score: {score}", font, WHITE, HEIGHT // 2 + 10)
            show_text_center(screen, "Press R to Restart or Q to Quit", font, WHITE, HEIGHT // 2 + 50)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_loop()