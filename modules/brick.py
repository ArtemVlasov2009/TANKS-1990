import pygame
import modules.settings as m_settings
pygame.init()

class Brick(m_settings.Settings):
    #
    def __init__(self, width1 = 0, height1= 0, x1= 0, y1= 0, name_file1= None):
        m_settings.Settings.__init__(self, width= width1, height= height1, x= x1, y = y1, name_file= name_file1)
        self.load_image()
