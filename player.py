import settings
from pgzero.builtins import Actor, sounds

class Player(Actor):
    def __init__(self, pos):
        super().__init__("player_idle_1", pos)
        self.images = {
            "idle": ["player_idle_1", "player_idle_2"],
            "walk": ["player_walk_1", "player_walk_2"]
        }
        self.frame_index = 0
        self.image_timer = 0
        self.vy = 0
        self.on_ground = False
        self.was_up = False
        try:
            self.scale = 0.5
        except AttributeError:
            pass

    def update(self, keys, platforms):
      dx = 0
      state = "idle"

      if keys.left:
          dx = -settings.PLAYER_SPEED
          state = "walk"
          self.flip_x = True
      elif keys.right:
          dx = settings.PLAYER_SPEED
          state = "walk"
          self.flip_x = False

    # move horizontally
      self.x += dx

    # apply gravity
      self.vy += settings.GRAVITY
      self.y += self.vy
      self.on_ground = False

    # check collision with platforms from top only
      for plat in platforms:
        if self.vy > 0 and self.colliderect(plat):
            if self.bottom - self.vy <= plat.top:
                self.bottom = plat.top
                self.vy = 0
                self.on_ground = True
                break

    # jump
      if keys.up and self.on_ground and not self.was_up:
        self.vy = settings.PLAYER_JUMP_SPEED
        sounds.jump.play()
      self.was_up = keys.up

    # animation
      self.image_timer += 1
      if self.image_timer > 10:
        self.image_timer = 0
        self.frame_index = (self.frame_index + 1) % len(self.images[state])
        self.image = self.images[state][self.frame_index]
