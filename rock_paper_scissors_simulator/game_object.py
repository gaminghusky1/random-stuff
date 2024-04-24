import pygame


class GameObject:
    def __init__(self, object_type, location, velocity, size=(30, 30)):
        self.object_type = object_type
        self.velocity = velocity
        self.rect = pygame.rect.Rect(location, size)
        self.size = size
        self.image = pygame.image.load("sprites/" + self.object_type + ".png")
        self.image = pygame.transform.scale(self.image, size)

        self.killers = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
        self.targets = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
        self.killer = self.killers[object_type]

    def load(self, SCREEN):
        self.image = pygame.image.load("sprites/" + self.object_type + ".png")
        self.image = pygame.transform.scale(self.image, self.size)
        SCREEN.blit(self.image, self.rect)

    def move(self, screen_width, screen_height):
        self.rect.centerx += self.velocity[0]
        self.rect.centery += self.velocity[1]
        if self.rect.x < 0:
            self.rect.x = 0
            self.velocity = (-self.velocity[0], self.velocity[1])
        elif self.rect.x + self.rect.width > screen_width:
            self.rect.x = screen_width - self.rect.width
            self.velocity = (-self.velocity[0], self.velocity[1])
        elif self.rect.y < 0:
            self.rect.y = 0
            self.velocity = (self.velocity[0], -self.velocity[1])
        elif self.rect.y + self.rect.height > screen_height:
            self.rect.y = screen_height - self.rect.height
            self.velocity = (self.velocity[0], -self.velocity[1])

    def check_collisions(self, other_game_objects):
        for other_game_object in other_game_objects:
            if other_game_object != self and other_game_object.object_type == self.killer:
                if self.rect.colliderect(other_game_object.rect):
                    self.killer = self.killers[self.object_type]
                    self.object_type = other_game_object.object_type
