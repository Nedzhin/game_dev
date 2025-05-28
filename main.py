import random
import settings
from pygame import Rect
from menu import Menu
from player import Player
from enemy import Enemy
from pgzero import music
from pgzero.builtins import sounds

# window settings
TITLE = settings.TITLE
WIDTH = settings.WIDTH
HEIGHT = settings.HEIGHT

state = "menu"
menu = Menu()

# audio
music_on = True
music.set_volume(0.5)
music.play("background")

def on_music_end():
    if music_on and state != "menu":
        music.play("background")

# entities
PLAYER_START_POS = (100, 526)  
# Player starts at x=100, y=518 (with scale 0.5, bottom=550)
player = Player(PLAYER_START_POS)
try:
    player.scale = 0.5
except AttributeError:
    pass

enemies = [
    Enemy((400, 538), 300, 700),   # Enemy 1, ground, patrols middle-right
    Enemy((700, 538), 600, 780)    # Enemy 2, ground, patrols far right
]
for e in enemies:
    try:
        e.scale = 0.5
    except AttributeError:
        pass

platforms = [
    Rect((0, 550), (800, 24)),       # Ground
    Rect((250, 420), (180, 18)),     # Middle platform
    Rect((500, 300), (140, 16)),     # Higher platform
    Rect((250, 300), (100, 16)),
]


def reset_game():
    global player, enemies
    player = Player((100, 0))  # y doesn't matter
    player.scale = 0.5
    player.bottom = 550  # land on ground

    enemies = [
        Enemy((400, 538), 300, 700),
        Enemy((700, 538), 600, 780)
    ]
    for e in enemies:
        try:
            e.scale = 0.5
        except AttributeError:
            pass


def draw():
    if state == "menu":
        menu.draw(screen, music_on)
    else:
        screen.clear()
        for plat in platforms:
            screen.draw.filled_rect(plat, "brown")
        player.draw()
        for e in enemies:
            e.draw()

def update():
    global state
    if state == "menu":
        return
    player.update(keyboard, platforms)
    for e in enemies:
        e.update()
    # Check for collision: if player touches enemy, player dies
    for e in enemies:
        if player.colliderect(e):
            sounds.hit.play()
            state = "menu"
            break


def on_mouse_down(pos):
    global state, music_on
    if state == "menu":
        choice = menu.click(pos)
        if choice == "start":
            reset_game()
            state = "play"
            if music_on:
                music.play("background")
        elif choice == "music":
            music_on = not music_on
            if music_on:
                music.set_volume(0.5)
                music.play("background")
            else:
                music.set_volume(0)
                music.stop()
        elif choice == "exit":
            exit()