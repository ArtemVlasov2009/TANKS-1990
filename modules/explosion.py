import pygame
import modules.settings as m_settings
import modules.data_base as m_data


class Explosion(m_settings.Settings):
    def __init__(self, width1 = 18, height1 = 18, x1 = 0, y1 = 0, name_file1 = "images/explosions/explosion_1.png"):
        m_settings.Settings.__init__(self, width = width1, height = height1 ,x = x1, y = y1,name_file = name_file1 )
        self.COUNT_WHILE = 0
        self.IMG_1 = None
        self.IMG_2 = None
        self.IMG_3 = None
        self.LOAD_IMG = False
        self.load_image()

    def draw_explosion(self, explosion):
        if self.LOAD_IMG == False:
            self.NAME_IMG = "images/explosions/explosion_1.png"
            self.IMG_1 = self.load_image(check_img = False)
            self.NAME_IMG = "images/explosions/explosion_2.png"
            self.IMG_2 = self.load_image(check_img = False)
            self.NAME_IMG = "images/explosions/explosion_3.png"
            self.IMG_3 = self.load_image(check_img = False)
            self.LOAD_IMG = True
        if self.COUNT_WHILE == 2:
            self.IMAGE = self.IMG_1
        if self.COUNT_WHILE == 4:
            self.IMAGE = self.IMG_2
        if self.COUNT_WHILE == 6:
            self.IMAGE = self.IMG_3
        if self.COUNT_WHILE == 8:
            index_explosion = m_data.list_explosion.index(explosion)
            del m_data.list_explosion[index_explosion]
        self.COUNT_WHILE += 1
 
 