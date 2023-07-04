import pygame
import modules.path_to_file as m_path
import modules.settings as m_settings
import modules.create_bullet as m_bullet
import modules.data_base as m_data
import modules.create_sound as m_sound
import random
#
class My_hero(m_settings.Settings):
    #
    def __init__(self, width1= 32, height1= 32, x1= 260, y1= 540, name_file1= "images/hero/tank_UP_DW_1.png", sound1 = True, folder_img1 = "hero", hp1 = 0):
        m_settings.Settings.__init__(self, width= width1, height= height1, x= x1, y= y1, name_file= name_file1, hp= hp1)
        self.load_image()
        self.DIRECTION_H_V = False
        self.IMG_1 = None
        self.IMG_2 = None
        self.ROTATE = None
        self.COUNT_WHILE = 0
        self.SPEED = 2
        self.RANDOM_NUMBER = 0
        self.FOLDER_IMG = folder_img1
        self.SOUND_STOP = pygame.mixer.Sound(m_path.find_path_to_file("sound/tank_stop.mp3"))
        self.SOUND_MOVE = pygame.mixer.Sound(m_path.find_path_to_file("sound/tank_move.mp3"))
        self.TYPE_OBJECT = 'hero'
        if sound1:
            self.sounds_move()
    #
    def get_keys(self):
        return pygame.key.get_pressed()
    #
    def move_animation(self, rotate = None, direction_x = False, direction_y = False, name_img = None):
        if self.ROTATE != rotate:
            self.ROTATE = rotate
            self.DIRECTION_L_R = direction_x
            self.DIRECTION_U_D = direction_y
            self.NAME_FILE = f"images/{self.FOLDER_IMG}/tank_{name_img}_1.png"
            self.IMG_1 = self.load_image(check_img= False)
            self.NAME_FILE = f"images/{self.FOLDER_IMG}/tank_{name_img}_2.png"
            self.IMG_2 = self.load_image(check_img= False)
        if self.COUNT_WHILE == 2:
            self.IMAGE = self.IMG_1
        if self.COUNT_WHILE == 4:
            self.IMAGE = self.IMG_2
            self.COUNT_WHILE = 0
        self.COUNT_WHILE = self.COUNT_WHILE + 1
    #
    def move_left(self):
        if self.get_keys()[pygame.K_LEFT] == True:
            self.collision_left()
            self.move_animation(rotate= "L", direction_x= False, name_img= "L_R")
            self.X = self.X - self.SPEED
            self.SPEED = 2
    #
    def move_right(self):
        if self.get_keys()[pygame.K_RIGHT] == True:
            self.collision_right()
            self.move_animation(rotate= "R", direction_x= True, name_img= "L_R")
            self.X = self.X + self.SPEED
            self.SPEED = 2
    #     
    def move_up(self):
        if self.get_keys()[pygame.K_UP] == True:
            self.collision_up()
            self.move_animation(rotate= "UP", direction_y= False, name_img= "UP_DW")
            self.Y = self.Y - self.SPEED
            self.SPEED = 2
    #
    def move_down(self):
        if self.get_keys()[pygame.K_DOWN] == True:
            self.collision_down()
            self.move_animation(rotate= "DW", direction_y= True, name_img= "UP_DW")
            self.Y = self.Y + self.SPEED
            self.SPEED = 2
    #
    def sounds_move(self):
        if not self.get_keys()[pygame.K_RIGHT] and not self.get_keys()[pygame.K_LEFT] and not self.get_keys()[pygame.K_UP] and not self.get_keys()[pygame.K_DOWN]:
            self.SOUND_MOVE.stop()
            if self.SOUND_STOP.get_num_channels() == 0:
                self.SOUND_STOP.play()
        if self.get_keys()[pygame.K_RIGHT] or self.get_keys()[pygame.K_LEFT] or self.get_keys()[pygame.K_UP] or self.get_keys()[pygame.K_DOWN]:
            self.SOUND_STOP.stop()
            if self.SOUND_MOVE.get_num_channels() == 0:
                self.SOUND_MOVE.play()
    #
    def shoot(self):
        
        if self.get_keys()[pygame.K_SPACE] == True and len(m_data.list_bullets_hero) == 0:
            # sound = m_sound.Sound_track('sound/shoot.mp3')
            sound = m_sound.Sound_track(name_file= 'sound/shoot.mp3')
            m_data.list_sound.append(sound)
            y = self.Y
            x = self.Y
            if self.ROTATE == "DW":
                x = self.X + self.WIDTH // 2 - 3
                y = self.Y + self.HEIGHT - 3
            if self.ROTATE == "UP" or self.ROTATE == None:
                x = self.X + self.WIDTH // 2 - 3
                y = self.Y 
            if self.ROTATE == "L":
                x = self.X + 3
                y = self.Y + self.HEIGHT // 2 - 3
            if self.ROTATE == "R":
                x = self.X + self.WIDTH - 6
                y = self.Y + self.HEIGHT // 2 - 3
            bullet = m_bullet.Bullet(name_file1 = "images/bullet/bullet.png", x1 = x, y1 = y, direction= self.ROTATE, speed= 3)
            m_data.list_bullets_hero.append(bullet)
    #
    def stop_up(self, brick, step):
        if brick.X < self.X + step and brick.X + brick.WIDTH > self.X + step: 
            if brick.Y + brick.HEIGHT > self.Y - 2 and  brick.Y + brick.HEIGHT < self.Y + self.HEIGHT:
                number = random.randint(0,3)
                while number == 2:
                   number = random.randint(0,3)
                self.RANDOM_NUMBER = number
                self.SPEED = 0
    #
    def stop_dw(self, brick, step):
        if brick.X < self.X + step and brick.X + brick.WIDTH > self.X  + step:
            if brick.Y <= self.Y + self.HEIGHT + 2 and brick.Y > self.Y:
                self.SPEED = 0
                self.RANDOM_NUMBER = random.randint(1,3)
    #
    def collision_up(self):
        for brick in m_data.list_bricks:
            #
            if brick.NAME_FILE != "images/textures/tree.png":
                self.stop_up(brick= brick, step = 0)
                self.stop_up(brick= brick, step = 2)
                self.stop_up(brick= brick, step = 6)
                self.stop_up(brick= brick, step = self.WIDTH // 8)
                self.stop_up(brick= brick, step = 12)
                self.stop_up(brick= brick, step = self.WIDTH // 2)
                self.stop_up(brick= brick, step = self.WIDTH // 4)
                self.stop_up(brick= brick, step = 20)
                self.stop_up(brick= brick, step = 24)
                self.stop_up(brick= brick, step = 28)
                self.stop_up(brick= brick, step = 30)
                self.stop_up(brick= brick, step = self.WIDTH)
    #               
    def collision_right(self):    
        for brick in m_data.list_bricks:
            #
            if brick.NAME_FILE != "images/textures/tree.png":
                if brick.Y < self.Y and brick.Y + brick.HEIGHT > self.Y:
                    if brick.X <= self.X + self.WIDTH + 2 and brick.X > self.X:
                        number = random.randint(0,3)
                        while number == 3:
                           number = random.randint(0,3)
                        self.RANDOM_NUMBER = number
                        self.SPEED = 0
                #
                if brick.Y < self.Y + self.HEIGHT // 4 and brick.Y + brick.HEIGHT > self.Y + self.HEIGHT // 4:
                    if brick.X <= self.X + self.WIDTH + 2 and brick.X > self.X:
                        number = random.randint(0,3)
                        while number == 3:
                           number = random.randint(0,3)
                        self.RANDOM_NUMBER = number
                        self.SPEED = 0
                #
                if brick.Y < self.Y + self.HEIGHT // 2 and brick.Y + brick.HEIGHT > self.Y + self.HEIGHT // 2:
                    if brick.X <= self.X + self.WIDTH + 2 and brick.X > self.X:
                        number = random.randint(0,3)
                        while number == 3:
                           number = random.randint(0,3)
                        self.RANDOM_NUMBER = number
                        self.SPEED = 0
                #
                if brick.Y < self.Y + self.HEIGHT // 2 + 8 and brick.Y + brick.HEIGHT > self.Y + self.HEIGHT // 2 + 8:
                    if brick.X <= self.X + self.WIDTH + 2 and brick.X > self.X:
                        number = random.randint(0,3)
                        while number == 3:
                           number = random.randint(0,3)
                        self.RANDOM_NUMBER = number
                        self.SPEED = 0
                #
                if brick.Y < self.Y + self.HEIGHT and brick.Y + brick.HEIGHT > self.Y + self.HEIGHT:
                    if brick.X <= self.X + self.WIDTH + 2 and brick.X > self.X:
                        number = random.randint(0,3)
                        while number == 3:
                           number = random.randint(0,3)
                        self.RANDOM_NUMBER = number
                        self.SPEED = 0
    #   
    def collision_left(self):    

        for brick in m_data.list_bricks:
            #
            if brick.NAME_FILE != "images/textures/tree.png":

                if brick.Y < self.Y and brick.Y + brick.HEIGHT > self.Y:
                    if brick.X + brick.WIDTH >= self.X - 2 and brick.X + brick.WIDTH < self.X + self.WIDTH:
                        number = random.randint(1,3)
                        while number == 1:
                            number = random.randint(1,3)
                        self.RANDOM_NUMBER = number
                        self.SPEED = 0
                #
                if brick.Y < self.Y + self.HEIGHT // 4 and brick.Y + brick.HEIGHT > self.Y + self.HEIGHT // 4:
                    if brick.X + brick.WIDTH >= self.X - 2 and brick.X + brick.WIDTH < self.X + self.WIDTH:
                        number = random.randint(1,3)
                        while number == 1:
                            number = random.randint(1,3)
                        self.RANDOM_NUMBER = number
                        self.SPEED = 0
                #
                if brick.Y < self.Y + self.HEIGHT // 2 and brick.Y + brick.HEIGHT > self.Y + self.HEIGHT // 2:
                    if brick.X + brick.WIDTH >= self.X - 2 and brick.X + brick.WIDTH < self.X + self.WIDTH:
                        number = random.randint(1,3)
                        while number == 1:
                           number = random.randint(1,3)
                        self.RANDOM_NUMBER = number
                        self.SPEED = 0
                #
                if brick.Y < self.Y + self.HEIGHT // 2 + 8 and brick.Y + brick.HEIGHT > self.Y + self.HEIGHT // 2 + 8:
                    if brick.X + brick.WIDTH >= self.X - 2 and brick.X + brick.WIDTH < self.X + self.WIDTH:
                        number = random.randint(1,3)
                        while number == 1:
                           number = random.randint(1,3)
                        self.RANDOM_NUMBER = number
                        self.SPEED = 0
                #
                if brick.Y < self.Y + self.HEIGHT and brick.Y + brick.HEIGHT > self.Y + self.HEIGHT:
                    if brick.X + brick.WIDTH >= self.X - 2 and brick.X + brick.WIDTH < self.X + self.WIDTH:
                        number = random.randint(1,3)
                        while number == 1:
                           number = random.randint(1,3)
                        self.RANDOM_NUMBER = number
                        self.SPEED = 0
    #
    def collision_down(self):
        for brick in m_data.list_bricks:
            #
            if brick.NAME_FILE != "images/textures/tree.png":
                self.stop_dw(brick= brick, step= 0)
                self.stop_dw(brick= brick, step= 2)
                self.stop_dw(brick= brick, step= self.WIDTH // 8)
                self.stop_dw(brick= brick, step= 6)
                self.stop_dw(brick= brick, step=  self.WIDTH // 4)
                self.stop_dw(brick= brick, step= 12)
                self.stop_dw(brick= brick, step=  self.WIDTH // 2)
                self.stop_dw(brick= brick, step=  self.WIDTH // 4 * 3)
                self.stop_dw(brick= brick, step = 20)
                self.stop_dw(brick= brick, step = 24)
                self.stop_dw(brick= brick, step = 28)
                self.stop_dw(brick= brick, step = 30)
                self.stop_dw(brick= brick, step=  self.WIDTH)

#
first_hero = My_hero()
m_data.list_bricks.append(first_hero)
#
# second_hero = My_hero()
