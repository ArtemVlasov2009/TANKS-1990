import pygame

pygame.init()

import random
import modules.main_hero as m_hero
import modules.data_base as m_data
import modules.create_bullet as m_bullet
import modules.settings as m_settings

class Bot(m_hero.My_hero):
    def __init__(self, width2 = 32, height2 = 32, x2 = 0, y2 = 0, name_file2 = None, sound2 = False, folder_img2 = None, type_bot = None, fire_rate = None, speed_bot = None, hp2 = 1):
        m_hero.My_hero.__init__(self, width1 = width2, height1 = height2, x1= x2, y1 = y2, name_file1= name_file2, sound1= sound2, folder_img1= folder_img2, hp1= hp2)
        self.DIRECTION_U_D = True
        self.TYPE_BOT = type_bot
        self.TYPE_OBJECT = 'bot'
        self.FIRE_RATE = fire_rate
        self.COUNT_FIRE_RATE = 0
        self.SPEED_BOT = speed_bot
        self.SPEED = speed_bot

        self.load_image()

    def move_left(self):
        self.collision_left()
        self.move_animation(rotate= "L", direction_x= False, name_img= "L_R")
        self.X = self.X - self.SPEED
        self.SPEED = self.SPEED_BOT
#   
    def move_right(self):
        self.collision_right()
        self.move_animation(rotate= "R", direction_x= True, name_img= "L_R")
        self.X = self.X + self.SPEED
        self.SPEED = self.SPEED_BOT
    #     
    def move_up(self):
        self.collision_up()
        self.move_animation(rotate= "UP", direction_y= False, name_img= "UP_DW")
        self.Y = self.Y - self.SPEED
        self.SPEED = self.SPEED_BOT

    def move_down(self):
        self.collision_down()
        self.move_animation(rotate= "DW", direction_y= True, name_img= "UP_DW")
        self.Y = self.Y + self.SPEED
        self.SPEED = self.SPEED_BOT

    def move_bot(self):
        if self.RANDOM_NUMBER == 0:
            self.move_down()
        if self.RANDOM_NUMBER == 1:
            self.move_left()
        if self.RANDOM_NUMBER == 2:
            self.move_up()
        if self.RANDOM_NUMBER == 3:
            self.move_right()

    def shoot(self):
        check = True
        for bullet in m_data.list_bullets_bots:
            if bullet.TYPE_BULLET == self.TYPE_BOT:
                check = False
        if check and self.COUNT_FIRE_RATE == self.FIRE_RATE:
            y = self.Y
            x = self.Y
            if self.ROTATE == "DW":
                x = self.X + self.WIDTH // 2 - 3
                y = self.Y + self.HEIGHT
            if self.ROTATE == "UP" or self.ROTATE == None:
                x = self.X + self.WIDTH // 2 - 3
                y = self.Y
            if self.ROTATE == "L":
                x = self.X
                y = self.Y + self.HEIGHT // 2 - 3
            if self.ROTATE == "R":
                x = self.X + self.WIDTH - 4
                y = self.Y + self.HEIGHT // 2 - 3
            bullet = m_bullet.Bullet(name_file1 = "images/bullet/bullet.png", x1 = x, y1 = y, direction= self.ROTATE, type_bullet= self.TYPE_OBJECT, speed= 3)
            m_data.list_bullets_bots.append(bullet)
            self.COUNT_FIRE_RATE = 0

        if self.COUNT_FIRE_RATE < self.FIRE_RATE:
            self.COUNT_FIRE_RATE += 1
        
bot1 = Bot(name_file2 = "images/bot/bot1/tank_UP_DW_1.png", folder_img2= "bot/bot1", type_bot= "bot1", fire_rate= 100, speed_bot = 2)
m_data.list_bricks.append(bot1)
bot2 = Bot(name_file2 = "images/bot/bot2/tank_UP_DW_1.png", folder_img2= "bot/bot2", type_bot = "bot2", x2= 540, y2= 0, fire_rate= 150, speed_bot= 1)
m_data.list_bricks.append(bot2)
bot3 = Bot(name_file2 = "images/bot/bot3/tank_UP_DW_1.png", folder_img2= "bot/bot3", type_bot = "bot3", x2= 540, y2= 0, fire_rate= 150, speed_bot= 0.5, hp2 = 3)
m_data.list_bricks.append(bot3)
bot4 = Bot(name_file2 = "images/bot/bot3/tank_UP_DW_1.png", folder_img2= "bot/bot3", type_bot = "bot3", x2= 256, y2= 0, fire_rate= 150, speed_bot= 0.5, hp2 = 3)
m_data.list_bricks.append(bot4)