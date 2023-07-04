import pygame
import modules.data_base as m_data
import modules.settings as m_settings
import modules.model_block as m_block

pygame.init()

# 0 - pass
# 1 - white_model
# 2 - red_model
# 3 - water_model
# 4 - tree_model
# 5 - ice_model
# 7 - comand_model

class Map(m_settings.Settings):
    def __init__(self, x1= -36, y1= -36):
        m_settings.Settings.__init__(self, x= x1, y= y1)
        
    def create_map(self):
        x = self.X
        y = self.Y
        #
        for list_model in m_data.list_map_one:
            for model in list_model:
                if model == 1:
                    block = m_block.Block(x1= x, y1= y)
                    block.create_block(set_column= 2, set_row= 2, width= 18, height= 18, name_file= "images/textures/white_brick.png")
                    m_data.list_models.append(block)
                if model == 4:
                    block = m_block.Block(x1= x, y1= y)
                    block.create_block(set_column= 2, set_row= 2, width= 18, height= 18, name_file= "images/textures/tree.png")
                    m_data.list_models.append(block)
                if model == 3:
                    block = m_block.Block(x1= x, y1= y)
                    block.create_block(set_column= 2, set_row= 2, width= 18, height= 18, name_file= "images/textures/water.png")
                    m_data.list_models.append(block)
                if model == 2:
                    block = m_block.Block(x1= x, y1= y)
                    block.create_red_block()
                if model == 6:
                    block = m_block.Block(x1= x, y1= y)
                    block.create_block(set_column= 1, set_row= 1, width= 18, height= 18, name_file= "images/textures/white_brick.png")
                    m_data.list_models.append(block)
                x = x + 36
            y = y + 36
            x = self.X


map1 = Map()
map1.create_map()