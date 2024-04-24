import random
import sys
import pygame
import game_object


def main():
    pygame.init()

    screen_width, screen_height = 1000, 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Rock Paper Scissors Simulator")

    clock = pygame.time.Clock()
    fps = 60

    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    gray = (128, 128, 128)

    darken_surface = pygame.Surface((screen_width, screen_height))
    darken_surface.set_alpha(128)
    darken_surface.fill((0, 0, 0))

    object_types = ["rock", "paper", "scissors"]
    game_objects = []
    game_over = False
    winner = None

    def draw_text(text, color, size, x, y, aligned="center"):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if aligned == "center":
            text_rect.center = (x, y)
        elif aligned == "topleft":
            text_rect.topleft = (x, y)
        screen.blit(text_surface, text_rect)

    for i in range(100):
        game_objects.append(game_object.GameObject(object_types[random.randint(0, 2)], (random.randint(0, screen_width-30),
                            random.randint(0, screen_height-30)), (random.randint(-7, 7), random.randint(-7, 7))))

    while True:
        screen.fill(black)
        delta_time = clock.tick(fps)
        # Main code here
        still_exists = set()
        for element in game_objects:
            still_exists.add(element.object_type)
            element.move(screen_width, screen_height)
            element.check_collisions(game_objects)
            element.load(screen)

        if len(still_exists) == 1:
            game_over = True
            for element in game_objects:
                element.velocity = (0, 0)
            if "rock" in still_exists:
                winner = "rock"
            elif "paper" in still_exists:
                winner = "paper"
            else:
                winner = "scissors"

        if game_over:
            screen.blit(darken_surface, (0, 0))
            if winner == "rock":
                draw_text("Rock wins!", gray, 150, screen_width / 2, screen_height / 2.7)
            elif winner == "paper":
                draw_text("Paper wins!", white, 150, screen_width / 2, screen_height / 2.7)
            else:
                draw_text("Scissors wins!", red, 150, screen_width / 2, screen_height / 2.7)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


if __name__ == "__main__":
    main()