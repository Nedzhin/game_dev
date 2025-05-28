from pygame import Rect

class Menu:
    def __init__(self):
        self.buttons = {
            "start": Rect(300, 200, 200, 50),
            "music": Rect(300, 270, 200, 50),
            "exit":  Rect(300, 340, 200, 50)
        }

    def draw(self, screen, music_on):
        screen.clear()
        screen.draw.text("Tutor Platformer", center=(400, 100), fontsize=60, color="white")
        screen.draw.filled_rect(self.buttons["start"], "green")
        screen.draw.text("Start Game", center=self.buttons["start"].center, fontsize=30)
        screen.draw.filled_rect(self.buttons["music"], "blue")
        screen.draw.text(f"Music: {'On' if music_on else 'Off'}", center=self.buttons["music"].center, fontsize=30)
        screen.draw.filled_rect(self.buttons["exit"], "red")
        screen.draw.text("Exit", center=self.buttons["exit"].center, fontsize=30)

    def click(self, pos):
        for name, rect in self.buttons.items():
            if rect.collidepoint(pos):
                return name
        return None