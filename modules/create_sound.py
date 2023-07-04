import modules.data_base as m_data
import pygame
import modules.path_to_file as m_path
pygame.init()

class Sound_track:
    def __init__(self, name_file = None):
        self.NAME_FILE = name_file
        self.SOUND = pygame.mixer.Sound(m_path.find_path_to_file(self.NAME_FILE))

    def play_sound_track(self, sound = None, loops = 0):
        pygame.mixer.music.load(m_path.find_path_to_file(self.NAME_FILE))
        pygame.mixer.music.play(loops= loops)
        if sound != None:
            index = m_data.list_sound.index(sound)
            del m_data.list_sound[index]
    #
    def play_sound_track_1(self, sound):
        self.SOUND.stop()
        if self.SOUND.get_num_channels() == 0:
            self.SOUND.play()
        if sound in m_data.list_sound_1:
            m_data.list_sound_1.remove(sound)
        if sound in m_data.list_sound:
            m_data.list_sound.remove(sound)
    