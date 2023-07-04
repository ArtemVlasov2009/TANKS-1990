import pygame
import modules.settings as m_settings
import modules.brick as m_brick
import  modules.data_base as m_data
pygame.init()

class Block(m_settings.Settings):
    def __init__(self, width1 = 0, height1= 0, x1= 0, y1= 0, name_file1= None):
        m_settings.Settings.__init__(self, width= width1, height= height1, x= x1, y= y1, name_file= name_file1)

    def create_block(self, set_column, set_row, width, height, name_file):
        x = self.X
        y = self.Y
        for count in range(set_column):
            for count in range(set_row):
                brick = m_brick.Brick(width1= width, height1= height, name_file1= name_file)
                brick.X = x
                brick.Y = y
                m_data.list_bricks.append(brick)
                x = x + brick.WIDTH
            y = y + brick.HEIGHT
            x = self.X

    def create_red_block(self):
        X = self.X
        Y = self.Y
        list_name_brick_row1 = ['1.png', '2.png', '3.png']
        list_row_width1 = [12, 18, 6]
        list_name_brick_row2 = ['4.png', '5.png']
        list_row_width2 = [20, 16]
        for count in range(4):
            if count % 2 == 0:
                for count1 in range(3):
                    brick = m_brick.Brick(width1= list_row_width1[count1], height1= 9, name_file1= f"images/textures/red_brick/{list_name_brick_row1[count1]}")
                    brick.X = X
                    brick.Y = Y
                    m_data.list_bricks.append(brick)
                    X = X + brick.WIDTH
            elif count % 2 == 1:
                for count1 in range(2):
                    brick = m_brick.Brick(width1= list_row_width2[count1], height1= 9, name_file1= f"images/textures/red_brick/{list_name_brick_row2[count1]}")
                    brick.X = X
                    brick.Y = Y
                    m_data.list_bricks.append(brick)
                    X = X + brick.WIDTH
            Y = Y + 9
            X = self.X

    # def blit_block(self, screen_game):
        # for brick in m_data.list_bricks:
            # brick.blit_sprite(screen_game)