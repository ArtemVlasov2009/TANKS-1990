import pygame
import modules.path_to_file as m_path

pygame.init()

class Settings:
    def __init__(self, width = 0, height= 0, x=0, y=0, name_file= None, hp = 1):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.NAME_FILE = name_file
        self.IMAGE = None
        self.DIRECTION_L_R = False
        self.DIRECTION_U_D = False
        #
        self.TYPE_OBJECT = None
        self.HP = hp
        
    def load_image(self, check_img = True):
        image_load = pygame.image.load(m_path.find_path_to_file(self.NAME_FILE))
        image_transform = pygame.transform.scale(image_load, (self.WIDTH, self.HEIGHT))
        if check_img:
            self.IMAGE = pygame.transform.flip(image_transform, flip_x= self.DIRECTION_L_R, flip_y= self.DIRECTION_U_D)
        else:
            return pygame.transform.flip(image_transform, flip_x= self.DIRECTION_L_R, flip_y= self.DIRECTION_U_D)

    def blit_sprite(self, screen_game):
        screen_game.blit(self.IMAGE, (self.X, self.Y))

