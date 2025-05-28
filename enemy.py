import random
import settings
from pgzero.builtins import Actor

class Enemy(Actor):
    def __init__(self, pos, x_min, x_max):
        super().__init__("enemy_idle_1", pos)
        self.images = {
            "idle": ["enemy_idle_1", "enemy_idle_2"],
            "walk": ["enemy_walk_1", "enemy_walk_2"]
        }
        self.frame_index = 0
        self.image_timer = 0
        self.direction = random.choice([-1, 1])
        self.x_min = x_min
        self.x_max = x_max
        self.flip_x = self.direction < 0

    def update(self):
        # patrol logic
        self.x += self.direction * settings.ENEMY_SPEED
        if self.x < self.x_min or self.x > self.x_max:
            self.direction *= -1
            self.flip_x = self.direction < 0

        # sprite animation
        self.image_timer += 1
        if self.image_timer > 15:
            self.image_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.images["walk"])
            self.image = self.images["walk"][self.frame_index]