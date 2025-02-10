import pygame
import math
import random
import asyncio

pygame.init()
pygame.mixer.init()

HEIGHT, WIDTH = 1000, 1000
FPS = 240
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
GOLF_GREEN = (89, 146, 68)
MAROON = (128, 0, 0)
GREY = (169,169,169)
MARINE_BLUE = (30, 63, 90)
YELLOW = (255, 255, 0)
pygame.display.set_caption("Mini_golf")

pygame.font.init()

my_font = pygame.font.SysFont('Arial', 30, bold=True, italic=False)
font_100 = pygame.font.SysFont('Arial', 100, bold=True, italic=False)

Plate_start = pygame.image.load('Assets/sprites/Plate.png')
Wall_texture = pygame.image.load('Assets/sprites/darkwood5_0.jpg')
grass_texture = pygame.image.load('Assets/sprites/grass.png')
Background = pygame.image.load('Assets/sprites/Background.png')
flag_sprite = pygame.image.load('Assets/sprites/flag.png')

Golf_swing_sound = pygame.mixer.Sound('Assets/soundEffect/golf_swing.ogg')
Wall_hit_sound = pygame.mixer.Sound('Assets/soundEffect/hit_wall.ogg')
in_hole = pygame.mixer.Sound('Assets/soundEffect/in_hole.ogg')

Music = 'Assets/music/MidsummerGarden.ogg'

class current_map:
    def __init__(self, screen): 
        self.Goal_radius = 15
        self.fall_in_goal = 9

        self.Player_start_posx = 0
        self.Player_start_posy = 0

        self.screen = screen
        self.map_counter = 0
        self.New_map = True
        self.map_rect = []
        self.map_background_rect = []
        self.map_moving_block = [] # array inside array is [firstx, firsty, width, height, finalx, finaly, directionx, directiony, movex, movey]
        self.map_moving_block_rect = []
        self.goalpos = (0,0)
        self.fall_in_rect = pygame.draw.circle(self.screen, GREEN, self.goalpos, self.fall_in_goal)
        self.mapname = ""

    def change_of_map(self):
        self.map_moving_block = []
        self.map_moving_block_rect = []
        if self.map_counter == 0:
            self.Player_start_posx = 500
            self.Player_start_posy = 700
            
            self.map_rect = [
                pygame.Rect(300, 100, 400, 30),
                pygame.Rect(300, 100, 30, 700),
                pygame.Rect(300, 780, 400, 30),
                pygame.Rect(680, 100, 30, 710)
            ]
            
            self.map_background_rect = [
                pygame.Rect(300, 100, 400, 700)
            ]

            self.goalpos = (500, 250)
            self.mapname = "1. Standard"
        if self.map_counter == 1:

            self.Player_start_posx = 500
            self.Player_start_posy = 700

            self.map_rect = [
                pygame.Rect(300, 100, 400, 30),
                pygame.Rect(300, 100, 30, 700),
                pygame.Rect(300, 780, 400, 30),
                pygame.Rect(680, 100, 30, 710),
                
                pygame.Rect(300, 350, 210, 30),
                pygame.Rect(490, 550, 200, 30) 
            ]
            
            self.map_background_rect = [
                pygame.Rect(300, 100, 400, 700)
            ]

            self.goalpos = (500, 250)

            self.mapname = "2. Standard Obstacle"

        if self.map_counter == 2:
            self.Player_start_posx = 200
            self.Player_start_posy = 700
            
            self.map_rect = [
                pygame.Rect(50, 100, 800, 30),
                pygame.Rect(50, 100, 30, 700),
                
                pygame.Rect(320 ,430, 30, 370),
                pygame.Rect(320 ,400, 530, 30),

                pygame.Rect(820, 100, 30, 300),
                pygame.Rect(50, 780, 300, 30)
            ]
            
            self.map_background_rect = [
                pygame.Rect(50, 100, 270, 700),
                pygame.Rect(320, 100, 500, 300)
            ]

            self.goalpos = (700, 260)
            self.mapname = "3. Right Turn"
        if self.map_counter == 3:
            self.Player_start_posx = 200
            self.Player_start_posy = 700
            
            self.map_rect = [
                pygame.Rect(50, 100, 800, 30),
                pygame.Rect(50, 100, 30, 700),
                
                pygame.Rect(320 ,430, 30, 370),
                pygame.Rect(320 ,400, 230, 30),

                pygame.Rect(820, 100, 30, 700),
                pygame.Rect(50, 780, 300, 30),

                pygame.Rect(550,400,30,400),
                pygame.Rect(550,780,300,30)
            ]
            
            self.map_background_rect = [
                pygame.Rect(50, 100, 270, 700),
                pygame.Rect(320, 100, 500, 300),
                pygame.Rect(550, 400, 300, 400)
            ]

            self.goalpos = (700, 700)
            self.mapname = "4. Upside U"

        if self.map_counter == 4:
            self.Player_start_posx = 500
            self.Player_start_posy = 800
            
            self.map_rect = [
                pygame.Rect(380, 500, 30, 400),
                pygame.Rect(600, 360, 30, 510),
                pygame.Rect(380, 870, 250, 30),

                pygame.Rect(120, 500, 260, 30),
                pygame.Rect(360, 330, 270, 30),

                pygame.Rect(120, 100, 30, 400),
                pygame.Rect(120, 100, 800, 30),

                pygame.Rect(360, 280, 370, 30),
                pygame.Rect(330, 280, 30, 80),

                pygame.Rect(730, 280, 30, 620),
                pygame.Rect(900, 100, 30, 800),

                pygame.Rect(750, 870, 150, 30)

            ]
            
            self.map_background_rect = [
                pygame.Rect(400, 350, 220, 550),
                pygame.Rect(120, 100, 230, 400),
                pygame.Rect(120, 350, 330, 150),
                pygame.Rect(120, 100, 800, 200),
                pygame.Rect(750, 100, 150, 800)

            ]

            self.goalpos = (830, 800)

            self.mapname = "5. Snake"

        if self.map_counter == 5:
            self.Player_start_posx = 310
            self.Player_start_posy = 750
            
            self.map_rect = [
                pygame.Rect(620, 150, 30, 300),
                pygame.Rect(620, 150, 200, 30),
                pygame.Rect(200, 820, 220, 30),
                pygame.Rect(600, 820, 220, 30),
                pygame.Rect(800, 150, 30, 700),

                pygame.Rect(420, 620, 150, 30),
                pygame.Rect(390, 620, 30, 200),
                pygame.Rect(570, 620, 30, 230),

                pygame.Rect(620, 250, 30, 200),
                pygame.Rect(200, 420, 420, 30),
                pygame.Rect(200, 420, 30, 400)

            ]
            
            self.map_background_rect = [
                pygame.Rect(200, 450, 600, 200),
                pygame.Rect(200, 650, 200, 200),
                pygame.Rect(600, 650, 200, 200),
                pygame.Rect(650, 150, 150, 300),
            ]

            self.map_moving_block = [
            ]  # array inside array is [firstx, firsty, width, height, finalx, finaly, directionx, directiony, movex, movey]

            self.map_moving_block_rect = [None] * len(self.map_moving_block)

            self.goalpos = (750, 220)

            self.mapname = "6. Horse"

        if self.map_counter == 6:
            self.Player_start_posx = 500
            self.Player_start_posy = 700
            
            self.map_rect = [
                pygame.Rect(300, 100, 400, 30),
                pygame.Rect(300, 100, 30, 700),
                pygame.Rect(300, 780, 400, 30),
                pygame.Rect(680, 100, 30, 710)
            ]
            
            self.map_background_rect = [
                pygame.Rect(300, 100, 400, 700)
            ]

            self.map_moving_block = [
                [370, 350, 70, 30, 565, 350, 1, 1, 0, 0],
                [370, 500, 70, 30, 565, 500, 1, 1, 130, 0]
            ]  # array inside array is [firstx, firsty, width, height, finalx, finaly, directionx, directiony, movex, movey]

            self.map_moving_block_rect = [None] * len(self.map_moving_block)

            self.goalpos = (500, 250)

            self.mapname = "7. Moving stones"

        if self.map_counter == 7:

            self.Player_start_posx = 500
            self.Player_start_posy = 700
            
            self.map_rect = [
                pygame.Rect(300, 100, 400, 30),
                pygame.Rect(300, 100, 30, 700),
                pygame.Rect(300, 780, 400, 30),
                pygame.Rect(680, 100, 30, 710),
                pygame.Rect(300, 450, 300, 30)
            ]
            
            self.map_background_rect = [
                pygame.Rect(300, 100, 400, 700)
            ]

            self.map_moving_block = [
                [310, 455, 300, 20, 360, 455, 1, 1, 0, 0]
            ]  # array inside array is [firstx, firsty, width, height, finalx, finaly, directionx, directiony, movex, movey]

            self.map_moving_block_rect = [None] * len(self.map_moving_block)

            self.goalpos = (500, 250)

            self.mapname = "8. Moving wall stone"

        if self.map_counter == 8:
            self.Player_start_posx = 500
            self.Player_start_posy = 900
            
            self.map_rect = [
                pygame.Rect(400, 50, 30, 900),
                pygame.Rect(570, 50, 30, 900),
                pygame.Rect(400, 50, 200, 30),
                pygame.Rect(400, 930, 200, 30)
            ]
            
            self.map_background_rect = [
                pygame.Rect(400, 50, 200, 900)
            ]

            self.map_moving_block = [
            ]  # array inside array is [firstx, firsty, width, height, finalx, finaly, directionx, directiony, movex, movey]

            self.map_moving_block_rect = [None] * len(self.map_moving_block)

            self.goalpos = (500, 100)

            self.mapname = "9. Longt gong"

        if self.map_counter == 9:
            self.Player_start_posx = 150
            self.Player_start_posy = 150
            
            self.map_rect = [
                pygame.Rect(50, 50, 30, 900),
                pygame.Rect(220, 50, 30, 680),
                pygame.Rect(50, 50, 200, 30),
                pygame.Rect(50, 920, 900, 30),
                pygame.Rect(220, 730, 120, 30),

                pygame.Rect(340, 400, 30, 360),
                pygame.Rect(410, 400, 30, 360),
                pygame.Rect(340, 400, 70, 30),

                pygame.Rect(510, 400, 30, 360),
                pygame.Rect(580, 400, 30, 360),
                pygame.Rect(510, 400, 70, 30),

                pygame.Rect(440, 730, 70, 30),
                pygame.Rect(610, 730, 70, 30),

                pygame.Rect(650, 50, 30, 680),
                pygame.Rect(680, 50, 270, 30),

                pygame.Rect(920, 50, 30, 900),

                pygame.Rect(835, 200, 30, 560),
                pygame.Rect(735, 200, 30, 560)
            ]
            
            self.map_background_rect = [
                pygame.Rect(50, 50, 200, 900),
                pygame.Rect(50, 750, 900, 200),
                pygame.Rect(680, 50, 250, 900),
                pygame.Rect(510, 400, 70, 360),
                pygame.Rect(360, 400, 70, 360),
            ]

            self.map_moving_block = [
            ]  # array inside array is [firstx, firsty, width, height, finalx, finaly, directionx, directiony, movex, movey]

            self.map_moving_block_rect = [None] * len(self.map_moving_block)

            self.goalpos = (800, 150)

            self.mapname = "10. Ludd"

        if self.map_counter == 10:
            self.Player_start_posx = 310
            self.Player_start_posy = 750
            
            self.map_rect = [
                pygame.Rect(200, 150, 30, 700),
                pygame.Rect(200, 150, 600, 30),
                pygame.Rect(200, 820, 220, 30),
                pygame.Rect(600, 820, 220, 30),
                pygame.Rect(800, 150, 30, 700),

                pygame.Rect(420, 620, 150, 30),
                pygame.Rect(390, 620, 30, 200),
                pygame.Rect(570, 620, 30, 230),

                pygame.Rect(620, 250, 30, 200),
                pygame.Rect(350, 250, 30, 200),
                pygame.Rect(350, 250, 300, 30),
                pygame.Rect(350, 420, 300, 30),

            ]
            
            self.map_background_rect = [
                pygame.Rect(200, 150, 600, 100),
                pygame.Rect(200, 450, 600, 200),
                pygame.Rect(200, 650, 200, 200),
                pygame.Rect(600, 650, 200, 200),
                pygame.Rect(200, 250, 150, 200),
                pygame.Rect(650, 250, 150, 200),
            ]

            self.map_moving_block = [
            ]  # array inside array is [firstx, firsty, width, height, finalx, finaly, directionx, directiony, movex, movey]

            self.map_moving_block_rect = [None] * len(self.map_moving_block)

            self.goalpos = (750, 220)

            self.mapname = "11. Sus"

        if self.map_counter == 11:
            self.Player_start_posx = 500
            self.Player_start_posy = 700
            
            self.map_rect = [
                pygame.Rect(300, 100, 400, 30),
                pygame.Rect(300, 100, 30, 700),
                pygame.Rect(300, 780, 400, 30),
                pygame.Rect(680, 100, 30, 710)
            ]
            
            self.map_background_rect = [
                pygame.Rect(300, 100, 400, 700)
            ]

            self.map_moving_block = [[310, 100, 380, 20, 310, 455, 1, 1, 0, 0]
            ]  # array inside array is [firstx, firsty, width, height, finalx, finaly, directionx, directiony, movex, movey]

            self.map_moving_block_rect = [None] * len(self.map_moving_block)
            self.goalpos = (500, 250)

            self.mapname = "12. The Wave"

        if self.map_counter == 12:
            self.Player_start_posx = 500
            self.Player_start_posy = 700
            
            self.map_rect = [
                pygame.Rect(300, 100, 400, 30),
                pygame.Rect(300, 100, 30, 700),
                pygame.Rect(300, 780, 400, 30),
                pygame.Rect(680, 100, 30, 710)
            ]
            
            self.map_background_rect = [
                pygame.Rect(300, 100, 400, 700)
            ]

            self.map_moving_block = [[310, 130, 150, 20, 530, 455, 1, 1, 0, 0],
            ]  # array inside array is [firstx, firsty, width, height, finalx, finaly, directionx, directiony, movex, movey]

            self.map_moving_block_rect = [None] * len(self.map_moving_block)
            self.goalpos = (500, 250)

            self.mapname = "13. Moving Stone"

        if self.map_counter == 13:
            self.Player_start_posx = 200
            self.Player_start_posy = 800
            
            self.map_rect = [
                pygame.Rect(0, 0, 1000, 30),
                pygame.Rect(0, 0, 30, 1000),
                pygame.Rect(0, 970, 1000, 30),
                pygame.Rect(970, 0, 30, 1000)
            ]
            
            self.map_background_rect = [
                pygame.Rect(0, 0, 1000, 1000)
            ]

            self.map_moving_block = [
            ]  # array inside array is [firstx, firsty, width, height, finalx, finaly, directionx, directiony, movex, movey]

            self.map_moving_block_rect = [None] * len(self.map_moving_block)
            self.goalpos = (900, 100)

            self.mapname = "14. Giant"

        if self.map_counter == 14:
            self.Player_start_posx = WIDTH//2
            self.Player_start_posy = HEIGHT//2
            
            self.map_rect = [
                pygame.Rect(0, 0, 1000, 30),
                pygame.Rect(0, 0, 30, 1000),
                pygame.Rect(0, 970, 1000, 30),
                pygame.Rect(970, 0, 30, 1000),

                pygame.Rect(100,300,200,30),
                pygame.Rect(100, 100, 30, 200),
                pygame.Rect(270, 100, 30, 200),

                pygame.Rect(WIDTH - 270 - 30, 300,200,30),
                pygame.Rect(WIDTH - 100 - 30, 100, 30, 200),
                pygame.Rect(WIDTH - 270 - 30, 100, 30, 200),

                pygame.Rect(WIDTH - 270 - 30, HEIGHT - 330,200,30),
                pygame.Rect(WIDTH - 100 - 30, HEIGHT - 300, 30, 200),
                pygame.Rect(WIDTH - 270 - 30, HEIGHT - 300, 30, 200),

                pygame.Rect(100, HEIGHT - 330,200,30),
                pygame.Rect(100, HEIGHT - 300, 30, 200),
                pygame.Rect(270, HEIGHT - 300, 30, 200),


            ]
            
            self.map_background_rect = [
                pygame.Rect(0, 0, 1000, 1000)
            ]

            self.map_moving_block = [
            ]  # array inside array is [firstx, firsty, width, height, finalx, finaly, directionx, directiony, movex, movey]

            self.map_moving_block_rect = [None] * len(self.map_moving_block)

            rngx = random.choice([1, 4])
            rngy = random.choice([1, 4])

            self.goalpos = (200*rngx, 200*rngy)

            self.mapname = "15. Lost"

        if self.map_counter == 15:
            self.Player_start_posx = WIDTH//2
            self.Player_start_posy = HEIGHT//2
            
            self.map_rect = [

                pygame.Rect(0, 0, 1000, 30),
                pygame.Rect(0, 0, 30, 1000),
                pygame.Rect(0, 970, 1000, 30),
                pygame.Rect(970, 0, 30, 1000),
                

                pygame.Rect(300, 300, 400, 30),
                pygame.Rect(300, 300, 30, 400),
                pygame.Rect(300, 670, 400, 30),
                pygame.Rect(670, 300, 30, 300),

                pygame.Rect(300, 100, 550, 30),
                pygame.Rect(820, 100, 30, 700),
                pygame.Rect(150, 100, 30, 700),
                pygame.Rect(150, 800, 700, 30),

            ]
            
            self.map_background_rect = [
                pygame.Rect(0,0,500,500),
                pygame.Rect(0,500,500,500),
                pygame.Rect(500,0,500,500),
                pygame.Rect(500,500,500,500)
            ]

            self.map_moving_block = [
            ]  # array inside array is [firstx, firsty, width, height, finalx, finaly, directionx, directiony, movex, movey]

            self.map_moving_block_rect = [None] * len(self.map_moving_block)

            self.goalpos = (900,900)

            self.mapname = "16. Get Out"

        if self.map_counter == 16:

            self.Player_start_posx = 900
            self.Player_start_posy = 900
            
            self.map_rect = [

                pygame.Rect(0, 0, 1000, 30),
                pygame.Rect(0, 0, 30, 1000),
                pygame.Rect(0, 970, 1000, 30),
                pygame.Rect(970, 0, 30, 1000),
                

                pygame.Rect(300, 300, 400, 30),
                pygame.Rect(300, 300, 30, 400),
                pygame.Rect(300, 670, 400, 30),
                pygame.Rect(670, 300, 30, 300),

                pygame.Rect(300, 100, 550, 30),
                pygame.Rect(820, 100, 30, 700),
                pygame.Rect(150, 100, 30, 700),
                pygame.Rect(150, 800, 700, 30),

            ]
            
            self.map_background_rect = [
                pygame.Rect(0,0,500,500),
                pygame.Rect(0,500,500,500),
                pygame.Rect(500,0,500,500),
                pygame.Rect(500,500,500,500)
            ]

            self.map_moving_block = [
            ]  # array inside array is [firstx, firsty, width, height, finalx, finaly, directionx, directiony, movex, movey]

            self.map_moving_block_rect = [None] * len(self.map_moving_block)

            self.goalpos = (WIDTH//2,HEIGHT//2)

            self.mapname = "17. Get In"

        if self.map_counter == 17:

            self.Player_start_posx = WIDTH//2
            self.Player_start_posy = HEIGHT//2 - 100
            
            self.map_rect = [
                
                pygame.Rect(300, 300, 400, 30),
                pygame.Rect(300, 300, 30, 400),
                pygame.Rect(300, 670, 400, 30),
                pygame.Rect(670, 300, 30, 400),

            ]
            
            self.map_background_rect = [
                pygame.Rect(300,300,400,400),
            ]

            self.map_moving_block = [
            ]  # array inside array is [firstx, firsty, width, height, finalx, finaly, directionx, directiony, movex, movey]

            self.map_moving_block_rect = [None] * len(self.map_moving_block)

            self.goalpos = (WIDTH//2,HEIGHT//2 + 100)

            self.mapname = "18. Last is hardest"

    def display(self):
        
        
        for background in self.map_background_rect:
            background = pygame.draw.rect(self.screen, GOLF_GREEN, background)
            scaled_texture = pygame.transform.scale(grass_texture, (background.width, background.height))
            self.screen.blit(scaled_texture, background)

        for index, moving_wall in enumerate(self.map_moving_block):
            if moving_wall[0] + moving_wall[8] > moving_wall[4] or moving_wall[0] + moving_wall[8] < moving_wall[0]:
                moving_wall[6] *= -1

            elif moving_wall[1] + moving_wall[9] > moving_wall[5] or moving_wall[1] + moving_wall[9] < moving_wall[1]:
                moving_wall[7] *= -1

            pygame.draw.rect(self.screen, BLACK, (moving_wall[0] + moving_wall[8] - 5, moving_wall[1] + moving_wall[9]-5, moving_wall[2]+10, moving_wall[3]+10))
            self.map_moving_block_rect[index] = pygame.draw.rect(self.screen, GREY, (moving_wall[0] + moving_wall[8], moving_wall[1] + moving_wall[9], moving_wall[2], moving_wall[3]))

            if moving_wall[0] != moving_wall[4]:
                moving_wall[8] += moving_wall[6] * 0.5
            if moving_wall[1] != moving_wall[5]:
                moving_wall[9] += moving_wall[7] * 0.5

        for wall in self.map_rect:
            wall_rect = pygame.draw.rect(self.screen, MAROON, wall)
            scaled_texture = pygame.transform.scale(Wall_texture, (wall.width, wall.height))
            self.screen.blit(scaled_texture, wall_rect)


        plate_rect = pygame.draw.rect(self.screen, BLACK, (self.Player_start_posx - 50, self.Player_start_posy - 25, 101, 51))
        self.screen.blit(Plate_start, plate_rect)

        pygame.draw.circle(self.screen, GREEN, self.goalpos, self.Goal_radius + 5)
        pygame.draw.circle(self.screen, BLACK, self.goalpos, self.Goal_radius)
        self.fall_in_rect = pygame.draw.circle(self.screen, BLACK, self.goalpos, self.fall_in_goal)

        # Render text
        self.text_render = my_font.render(self.mapname, True, WHITE)

        # Center text within the specified rectangle
        self.text_rect = self.text_render.get_rect(center=(800, 950))

        # Blit the text onto the screen
        self.screen.blit(self.text_render, self.text_rect)

class player:
    def __init__(self, screen, posx, posy, color = WHITE, radius = 15, score = []):
        self.posx = posx
        self.posy = posy
        self.ball_colour = color
        self.radius = radius
        self.screen = screen
        self.Power_click = False
        self.force = [0,0]
        self.velocity = [0,0]
        self.friction = 0.99
        self.force_colour = [0, 0] 
        self.ball_black_line = pygame.draw.circle(self.screen, BLACK, (self.posx, self.posy), self.radius)
        self.ball = pygame.draw.circle(self.screen, WHITE, (self.posx, self.posy), self.radius - 3)
        self.Score = score
        self.level_score = 0

    def display(self, mouse_pos):
        self.mouse_pos = mouse_pos

        self.force = [(self.posx - mouse_pos[0]) * 0.05, (self.posy - mouse_pos[1]) * 0.05]

        self.force_colour[0] = abs(max(-255, min(self.force[0], 255))) 
        self.force_colour[1] = abs(max(-255, min(self.force[1], 255)))
        
        alpha = math.sqrt(self.force_colour[0]**2 + self.force_colour[1]**2) * 5.1

        if alpha > 255:
            alpha = 255

        if self.Power_click:
            self.Power_circle = pygame.draw.circle(self.screen, BLACK, (self.mouse_pos[0], self.mouse_pos[1]), radius=10)

            self.Power_line = pygame.draw.line(self.screen, (255, 255-alpha, 0), (self.posx, self.posy), (self.mouse_pos[0], self.mouse_pos[1]), width=11)
            self.Power_circle = pygame.draw.circle(self.screen, (255, 255-alpha, 0), (self.mouse_pos[0], self.mouse_pos[1]), radius=8)
        
        self.ball_black_line = pygame.draw.circle(self.screen, BLACK, (self.posx, self.posy), self.radius)
        self.ball = pygame.draw.circle(self.screen, self.ball_colour, (self.posx, self.posy), self.radius - 3)

        pygame.draw.rect(self.screen, MAROON, (10, 930, 180, 50))
        pygame.draw.rect(self.screen, (255, 215, 0), (10, 930, 180, 50), 5)
        level_score_text = my_font.render(f"Strokes: {self.level_score}", True, (255, 215, 0))
        Score_level_score_text = level_score_text.get_rect(center=(100, 950))
        self.screen.blit(level_score_text, Score_level_score_text)

    def apply_force(self, mouse_pos):   
        # Compute force
        self.force = [(self.posx - mouse_pos[0]) * 0.04, (self.posy - mouse_pos[1]) * 0.04]
        self.force[0] = max(-40, min(self.force[0], 40))
        self.force[1] = max(-40, min(self.force[1], 40))

        # Set velocity
        self.velocity = self.force[:]

    def move(self):
        MAX_VELOCITY = 5

        velocity_magnitude = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)

        velocity_x = self.velocity[0]
        velocit_y = self.velocity[1]

        if velocity_magnitude > MAX_VELOCITY:
            scale = MAX_VELOCITY / velocity_magnitude
            velocity_x = scale * self.velocity[0]
            velocit_y = scale * self.velocity[1]

        self.posx += velocity_x
        self.posy += velocit_y

        # Boundary checks
        if self.posx - self.radius < 0:
            self.posx = self.radius
            self.velocity[0] = -self.velocity[0]
        elif self.posx + self.radius > WIDTH:
            self.posx = WIDTH - self.radius
            self.velocity[0] = -self.velocity[0]

        if self.posy - self.radius < 0:
            self.posy = self.radius
            self.velocity[1] = -self.velocity[1]
        elif self.posy + self.radius > HEIGHT:
            self.posy = HEIGHT - self.radius
            self.velocity[1] = -self.velocity[1]

        self.velocity[0] *= self.friction
        self.velocity[1] *= self.friction

        if abs(self.velocity[0]) < 0.1:
            self.velocity[0] = 0
        if abs(self.velocity[1]) < 0.1:
            self.velocity[1] = 0

async def End_score(score):

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    running = True
    clock = pygame.time.Clock()

    background_scroll = 0

    score.pop(0)

    while running:
        await asyncio.sleep(0)
        screen.fill(MARINE_BLUE)

        background_scroll -= 0.25
        if background_scroll < -999:
            background_scroll = 0

# Graphics

        Background_rect = pygame.draw.rect(screen, GOLF_GREEN, (background_scroll,background_scroll,0,0))
        screen.blit(Background, Background_rect)

        pygame.draw.rect(screen, WHITE, (200, 50, 600, 920))
        pygame.draw.rect(screen, BLACK, (200, 50, 600, 920), 5)

        for pos, x in enumerate(score):
            y_position = 100 + 40 * pos
            level_pos_rect = pygame.Rect(250, y_position - 20, 80, 40)
            pygame.draw.rect(screen, BLACK, level_pos_rect, 5)

            level_pos_text = my_font.render(str(pos + 1), True, BLACK)
            level_pos_text_rect = level_pos_text.get_rect(center=level_pos_rect.center)
            screen.blit(level_pos_text, level_pos_text_rect)

            score_rect = pygame.Rect(328, y_position - 20, 400, 40)
            pygame.draw.rect(screen, BLACK, score_rect, 5)

            Score_level = my_font.render(str(x), True, BLACK)
            Score_level_rect = Score_level.get_rect(center=score_rect.center)
            screen.blit(Score_level, Score_level_rect)

        total_score = sum(score)
        final_y_position = 100 + 40 * len(score)
        total_score_rect = pygame.Rect(328, final_y_position - 5, 400, 40)
        pygame.draw.rect(screen, BLACK, total_score_rect, 5)
        total_score_text = my_font.render(f"Score: {total_score}", True, BLACK)
        total_score_text_rect = total_score_text.get_rect(center=total_score_rect.center)
        screen.blit(total_score_text, total_score_text_rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
    
        pygame.display.update()
        clock.tick(FPS)

async def Gameplay(Ball_colour):

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    running = True
    clock = pygame.time.Clock()

    sound_played = True
    Power_check = True

    background_scroll = 0

    ball = player(screen, WIDTH/2, HEIGHT/2, color = Ball_colour, radius = 10, score = [])
    map = current_map(screen)

    while running:
        await asyncio.sleep(0)
        screen.fill(MARINE_BLUE)

        print(pygame.mouse.get_pos())

        background_scroll -= 0.25
        if background_scroll < -999:
            background_scroll = 0

        Background_rect = pygame.draw.rect(screen, GOLF_GREEN, (background_scroll,background_scroll,0,0))
        screen.blit(Background, Background_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and ball.velocity == [0,0] and Power_check == True:
                if ball.ball_black_line.collidepoint(pygame.mouse.get_pos()) and ball.Power_click == False:
                    ball.Power_click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if ball.Power_click:
                    pygame.mixer.Sound.set_volume(Golf_swing_sound, 0.1)
                    pygame.mixer.Sound.play(Golf_swing_sound)
                    ball.apply_force(event.pos)
                    ball.Power_click = False
                    ball.level_score += 1

        for wall in map.map_rect + map.map_moving_block_rect:
            if ball.ball.colliderect(wall):
                if abs(wall.right - ball.ball_black_line.left) < 10:
                    ball.velocity[0] = -ball.velocity[0]
                    ball.posx += 5
                elif abs(wall.left - ball.ball.right) < 10:
                    ball.velocity[0] = -ball.velocity[0]
                    ball.posx -= 5
                elif abs(wall.bottom - ball.ball.top) < 10:
                    ball.velocity[1] = -ball.velocity[1]
                    ball.posy += 5
                elif abs(wall.top - ball.ball.bottom) < 10:
                    ball.velocity[1] = -ball.velocity[1]
                    ball.posy -= 5
                pygame.mixer.Sound.set_volume(Wall_hit_sound, 0.1)
                pygame.mixer.Sound.play(Wall_hit_sound)                

        if ball.ball.colliderect(map.fall_in_rect) and abs(ball.velocity[0]) < 0.9 and abs(ball.velocity[1]) < 0.9:
            
            Power_check = False
            ball.velocity = [0, 0]
            ball.posx += (map.goalpos[0] - ball.posx) * 0.3
            ball.posy += (map.goalpos[1] - ball.posy) * 0.3

            if abs(map.goalpos[0] - ball.posx) < 0.2:
                ball.posx = int(map.goalpos[0])
            if abs(map.goalpos[1] - ball.posy) < 0.2:
                ball.posy = int(map.goalpos[1])

            if abs(ball.posx - map.goalpos[0]) < 1 and abs(ball.posy - map.goalpos[1]) < 1:
                
                if int(ball.radius) > 3:
                    ball.radius -= 0.1  # Shrink gradually

                    if sound_played:
                        pygame.mixer.Sound.set_volume(in_hole, 0.2)
                        pygame.mixer.Sound.play(in_hole)
                        sound_played = False

                if abs(map.goalpos[0] - ball.posx) < 0.2:
                    ball.posx = int(map.goalpos[0])
                if abs(map.goalpos[1] - ball.posy) < 0.2:
                    ball.posy = int(map.goalpos[1])

                if int(ball.radius) <= 3:
                    map.map_counter += 1
                    map.New_map = True
                    ball.radius = 10
                    sound_played = True

        if map.New_map == True:
            ball.Score.append(ball.level_score)
            ball.level_score = 0
            map.change_of_map()
            ball.posx = map.Player_start_posx
            ball.posy = map.Player_start_posy
            map.New_map = False
            Power_check = True

        if map.map_counter > 17:
            await End_score(ball.Score)
            return

        map.display()
        ball.move()
        ball.display(pygame.mouse.get_pos())
        pygame.display.update()
        clock.tick(FPS)

async def main():

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    running = True
    clock = pygame.time.Clock()

    background_scroll = 0

    Grey_change = [100,100,100]

    dragging_1 = False
    change_colour_rect_1 = pygame.Rect(WIDTH//2 - 50, 750, 100, 50)

    dragging_2 = False
    change_colour_rect_2 = pygame.Rect(WIDTH//2 - 200, 750, 100, 50)

    dragging_3 = False
    change_colour_rect_3 = pygame.Rect(WIDTH//2 + 100, 750, 100, 50)

    Ball_colour = [255,255,255]

    pygame.mixer.music.load(Music)
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely
    pygame.mixer.music.set_volume(0.08)

    while running:
        await asyncio.sleep(0)
        screen.fill(MARINE_BLUE)

        background_scroll -= 0.25
        if background_scroll < -999:
            background_scroll = 0

# Graphics

        Background_rect = pygame.draw.rect(screen, GOLF_GREEN, (background_scroll,background_scroll,0,0))
        screen.blit(Background, Background_rect)

        pygame.draw.rect(screen, GOLF_GREEN, (200,0,600,1000))

        pygame.draw.rect(screen, GREY, (200,0,20,1000))
        pygame.draw.rect(screen, GREY, (780,0,20,1000))

        flag_1 = pygame.Rect((250,150,100,100))
        flag_2 = pygame.Rect((680,150,100,100))
        screen.blit(flag_sprite, flag_1)
        screen.blit(flag_sprite, flag_2)

        XPGolfRender_shadow = font_100.render("XP-Golf", True, BLACK)
        text_rect_shadow = XPGolfRender_shadow.get_rect(center=(WIDTH//2 + 6, 208))
        screen.blit(XPGolfRender_shadow, text_rect_shadow)

        XPGolfRender = font_100.render("XP-Golf", True, WHITE)
        text_rect = XPGolfRender.get_rect(center=(WIDTH//2, 210))
        screen.blit(XPGolfRender, text_rect)

        XPGolfRender = pygame.font.SysFont('Comicsans', 30, bold=True, italic=False).render("Jh got 55, can you beat it?", True, BLACK)
        text_rect = XPGolfRender.get_rect(center=(WIDTH//2 + 3, 265))
        screen.blit(XPGolfRender, text_rect)

        XPGolfRender = pygame.font.SysFont('Comicsans', 30, bold=True, italic=False).render("Jh got 55, can you beat it?", True, YELLOW)
        text_rect = XPGolfRender.get_rect(center=(WIDTH//2, 265))
        screen.blit(XPGolfRender, text_rect)

        pygame.draw.rect(screen, BLACK, (WIDTH//2 - 205, 360, 410, 110))
        start_rect = pygame.draw.rect(screen, Grey_change, (WIDTH//2 - 200, 365, 400, 100))

        XPGolfRender = pygame.font.SysFont('Arial', 50, bold=True, italic=False).render("Start?", True, BLACK)
        text_rect = XPGolfRender.get_rect(center=(WIDTH//2, 410))
        screen.blit(XPGolfRender, text_rect)

        pygame.draw.rect(screen, GREEN, (WIDTH//2 - 100, 500, 200, 200))
        pygame.draw.rect(screen, BLACK, (WIDTH//2 - 100, 500, 200, 200),10)
        pygame.draw.circle(screen, BLACK, (WIDTH//2, 600) , 10)
        pygame.draw.circle(screen, Ball_colour, (WIDTH//2, 600) , 7)

        pygame.draw.rect(screen, BLACK, (WIDTH//2 - 10, 775, 20, 150))
        pygame.draw.rect(screen, MAROON, change_colour_rect_1)
        pygame.draw.rect(screen, BLACK, change_colour_rect_1, 5)

        pygame.draw.rect(screen, BLACK, (WIDTH//2 - 160, 775, 20, 150))
        pygame.draw.rect(screen, MAROON, change_colour_rect_2)
        pygame.draw.rect(screen, BLACK, change_colour_rect_2, 5)

        pygame.draw.rect(screen, BLACK, (WIDTH//2 + 140, 775, 20, 150))
        pygame.draw.rect(screen, MAROON, change_colour_rect_3)
        pygame.draw.rect(screen, BLACK, change_colour_rect_3, 5)



###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(pygame.mouse.get_pos()):
                    await Gameplay(Ball_colour)
                if change_colour_rect_1.collidepoint(pygame.mouse.get_pos()):
                    dragging_1 = True
                if change_colour_rect_2.collidepoint(pygame.mouse.get_pos()):
                    dragging_2 = True
                if change_colour_rect_3.collidepoint(pygame.mouse.get_pos()):
                    dragging_3 = True
            if event.type == pygame.MOUSEBUTTONUP:
                dragging_1 = False
                dragging_2 = False
                dragging_3 = False

            if event.type == pygame.MOUSEMOTION:
                if dragging_1:
                    change_colour_rect_1.centery = event.pos[1]
                if dragging_2:
                    change_colour_rect_2.centery = event.pos[1]
                if dragging_3:
                    change_colour_rect_3.centery = event.pos[1]
            
        change_colour_rect_1.centery = max(775, min(925, change_colour_rect_1.centery))
        change_colour_rect_2.centery = max(775, min(925, change_colour_rect_2.centery))
        change_colour_rect_3.centery = max(775, min(925, change_colour_rect_3.centery))

        Ball_colour = [int((1-(change_colour_rect_2.centery-775)/150)*255),int((1-(change_colour_rect_1.centery-775)/150)*255),int((1-(change_colour_rect_3.centery-775)/150)*255)]

        if start_rect.collidepoint(pygame.mouse.get_pos()):
            Grey_change = [169, 169, 169]
        else:
            Grey_change = [100, 100, 100]
        pygame.display.update()
        clock.tick(FPS)

asyncio.run(main())