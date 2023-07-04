
import pygame
import modules.main_hero as m_hero
import modules.model_block as m_block
import modules.create_map as m_map
import modules.data_base as m_data
import modules.create_bullet as m_bullet
import modules.create_bot as m_bot


pygame.init()
FPS = pygame.time.Clock()
screen = pygame.display.set_mode((576, 576))

game = True

while game:
    #
    FPS.tick(60)
    screen.fill((0, 0, 0))

    for hero in m_data.list_bricks:
        if hero.TYPE_OBJECT == 'hero':
            hero.blit_sprite(screen_game= screen)

            hero.move_left() 
            hero.move_right()
            hero.move_up()
            hero.move_down()

            hero.shoot()
            hero.sounds_move()
    #
    for bot in m_data.list_bricks:
        if bot.TYPE_OBJECT == 'bot':
            bot.blit_sprite(screen_game= screen)
            bot.move_bot()
            bot.shoot()
    #
    for bullet in m_data.list_bullets_hero:
        bullet.blit_sprite(screen_game = screen)
        bullet.move_bullet(bullet, m_data.list_bullets_hero)

    for bullet in m_data.list_bullets_bots:
        bullet.blit_sprite(screen_game = screen)
        bullet.move_bullet(bullet, m_data.list_bullets_bots)
    #
    for brick in m_data.list_bricks:
        if brick.TYPE_OBJECT == None:
            brick.blit_sprite(screen_game = screen)
    #
    for explosion in m_data.list_explosion:
        explosion.blit_sprite(screen_game = screen)
        explosion.draw_explosion(explosion)
    #
    for sound in m_data.list_sound:
        sound.play_sound_track(sound)
    #
    for sound in m_data.list_sound_1:
        sound.play_sound_track_1(sound)
    # 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.flip()