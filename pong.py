#pong powered by PyGame Zero
from turtle import screensize
import pgzrun
from random import randint, choice

#Definiujemy klasę dla paletek
class Palette:
    def __init__(self, palette, position, width=140, ball_widht=10): 
        """Paletka i jej właściwości"""
        self.palette = palette
        self.palette.x = position[0]
        self.palette.y = position[1]
        self.palette.speed = 5
        self.palette.pcenter = width // 2
        self.palette.ball_width = ball_widht


    def drawing(self):
        """Wywołujemy metodę obiektu"""
        self.palette.draw()

    def move(self, direction):
        """Aktualizujemy o pozycję w osi X"""
        if direction == "left":
            self.palette.x -= self.palette.speed
            if self.palette.x < 70:
                self.palette.x = 75
        elif direction == "right":
            self.palette.x += self.palette.speed
            if self.palette.x > (WIDTH - 70):
                self.palette.x = WIDTH - 70
    
    def bouce(self):
        """Sprawdzamy, czy piłeczka odbiłą się od paletki"""
        #Jeśli środek paletki jest zbyt daleko od środka piłeczki, to nie odbijemy
        if (
            self.palette.distance_to(ball) > self.palette.pcenter + self.palette.ball_width
            ):
            return False
        #Jeżeli środek paletki jest dalej niż 20 pikseli od środka piłeczki w osi X, to nie odbijamy
        if abs(self.palette.y - ball.y) > self.palette.ball.width * 2:
            return False
        #Dodatkowo zmieniamy kierunki lewo/prawo dla piłeczki
        if self.palette.x > ball.x and ball.direction_x == 'left':
            ball.direction_x = 'right'
        elif self.palette.x < ball.x and ball.direction_x == 'right':
            ball.direction_x = 'left'
        # i odbijamy piłeczkę
        return True

#Definiujemu funkcje dodatkowe i klasy
def update_ball_position():
    # aktualizujemy pozycję w osi X
    if ball.direction_x == "left":
        ball.x -= ball.speed
    elif ball.direction_x == "right":
        ball.x += ball.speed

    #aktualizujemy pozycję w osi Y
    if ball.direction_y == 'up':
        ball.y -= ball.speed
    elif ball.direction_y == 'down':
        ball.y += ball.speed

    # sprawdzamy, czy piłeczka odbija się
    # od lewej lub prawej krawędzi okna
    if ball.x < 5:
        ball.direction_x = "right"
    elif ball.x > WIDTH - 5:
        ball.direction_x = "left"

    #spawdzamy, czy ktoś wygrał
    if ball.y < 5:
        ball.winner = "GRACZ B"
    elif ball.y > HEIGHT - 5:
        ball.winner = "GRACZ A"

#Start programu

WIDTH = 1200
HEIGHT = 800
TITLE = "Pong - najlepsza gra ever!"

#Definiujemy wyświetlane obiekty i ich współrzędne Y

palette_a = Palette(Actor("palette.png"), (randint(70, 1210), 10))
palette_b = Palette(Actor("palette.png"), (randint(70, 1210), 790))
ball = Actor("ball.png")
ball.y = HEIGHT // 2
ball.x = WIDTH // 2

#Dodajemy własne właściwości
ball.direction_x = choice(("left", "right"))
ball.direction_y = choice(("up", "down"))
ball.speed = 2
ball.winner = None

def update_palettes():
    #Gracz_A
    if keyboard.a:
        palette_a.move('left')
    elif keyboard.s:
        palette_a.move('right')
    #Gracz_B
    if keyboard.k:
        palette_b.move('left')
    elif keyboard.l:
        palette_b.move('right')

def check_bouce():
    if palette_a.bouce():
        ball.direction_y = 'down'
    if palette_b.bouce():
        ball.direction_y = 'up'
#Najważniejsze funkcje sterujące

def update():
    update_ball_position()
    update_palettes()
    check_bouce()

def check_winner():
    if ball.winner:
        winner_txt = f"And the winner is: {ball.winner}"
        screen.draw.text(
            winner_txt, (WIDTH // 3, HEIGHT // 2), color = "red", fontsize = 60
        )

def draw():
    screen.blit("soccer.jpg", (0, 0))
    palette_a.drawing()
    palette_b.drawing()
    ball.draw()
    check_winner()


# Uruchomienie modułu PyGame Zero
pgzrun.go()