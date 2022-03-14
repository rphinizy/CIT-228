import sys
from time import sleep
import pygame

from settings import Settings
from player import Player
from rainbow import Rainbow
from meteor import Meteor
from gnome import Gnome
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class GameProject:
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        pygame.mixer.init()
        self.settings =Settings()

        """Create display window for the game"""
        self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Game Project")

        #make play button
        self.play_button =Button(self, "Play")

        #create instance of game stats
        self.stats=GameStats(self)

        #draw score information
        self.sb =Scoreboard(self)

        self.player =Player(self)
        self.rainbows =pygame.sprite.Group()
        self.gnomes =pygame.sprite.Group()
        self.meteors=pygame.sprite.Group()

        self._create_army()
        self._create_meteor()

        pygame.mixer.music.load("media/music.wav")
        pygame.mixer.music.play(1,0.0)
        self.background_image = pygame.image.load("media/background.jpg").convert()
       
    def run_game(self):
        """Start loop for main game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.player.update()
                self._update_rainbow()
                self._update_gnomes()
                self._update_meteors()
            self._update_screen()

    def _check_events(self):
        #watch for keybaord and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type ==pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            elif event.type ==pygame.KEYUP:
                self._check_keyup_events(event)
            
            elif event.type ==pygame.MOUSEBUTTONDOWN:
                mouse_pos =pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start game when player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            if not self.stats.paused:
                #reset the game statistics
                self.settings.initialize_dynamic_settings()
                self.stats.reset_stats()
                self.stats.game_active =True
                self.sb.prep_score()
                self.sb.prep_level()
                self.sb.prep_players()
                self.sb.prep_high_score()

                #Get rid of any remaining aliens and bullets.
                self.gnomes.empty()
                self.rainbows.empty()

                #create a new fleet and center the ship
                self._create_army()
                self.player.center_player()
            else:
                self.stats.game_active =True
            #Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        #move player to the right
        if event.key == pygame.K_RIGHT:
            self.player.moving_right=True
        #move player to the left
        elif event.key ==pygame.K_LEFT:
            self.player.moving_left=True
        #check for Q to quit
        elif event.key ==pygame.K_q:
                sys.exit()

        elif event.key ==pygame.K_p:
                self.stats.game_active =False
                self.stats.paused =True
                pygame.mouse.set_visible(True)

        elif event.key==pygame.K_SPACE:
            self._fire_rainbow()

        elif event.key ==pygame.K_UP:
            self.player.jump_up=True
            self.player.fall_down =False

    def _check_keyup_events(self,event):
         #stop right movement
        if event.key==pygame.K_RIGHT:
            self.player.moving_right=False
        #stop left movement
        if event.key==pygame.K_LEFT:
            self.player.moving_left=False

        elif event.key ==pygame.K_UP:
            self.player.fall_down =True
            self.player.jump_up =False
      
    def _fire_rainbow(self):
        """Create a new rainbow and add it to the rainbows group"""
        if len(self.rainbows) < self.settings.rainbows_allowed:
            new_rainbow =Rainbow(self)
            self.rainbows.add(new_rainbow)
            pygame.mixer.music.load("media/shoot.wav")
            pygame.mixer.music.play(1,0.0)
    
    def _update_rainbow(self):
        self.rainbows.update()
        #get rid of rainbows
        for rainbow in self.rainbows.copy():
            if rainbow.rect.bottom <=0:
                self.rainbows.remove(rainbow)
        #check for any rainbows that hat hit gnomes
        self._check_rainbow_gnome_collisions()

    def _check_rainbow_gnome_collisions(self):
        """Respond to rainbow-gnome_collisions"""
        #remove any rainbows and gnomes that have collided. 
        collisions =pygame.sprite.groupcollide(self.rainbows, self.gnomes, True, True)
        if collisions:
            pygame.mixer.music.load("media/ouch.wav")
            pygame.mixer.music.play(1,0.0)
            self.stats.score +=self.settings.gnome_points
            self.sb.prep_score()
            self.sb.prep_high_score()
    
        if not self.gnomes:
            self.rainbows.empty()
            self._create_army()
            self.settings.increase_speed()

            #increase level
            self.stats.level+=1
            self.sb.prep_level()

    def _create_meteor(self):
        meteor=Meteor(self)
        self.meteors.add(meteor)

    def _create_army(self):
        """Create army of gnomes"""
        #make gnome
        gnome = Gnome(self)
        gnome_width, gnome_height= gnome.rect.size
        #self.gnomes.add(gnome)
        gnome_width = gnome.rect.width
        available_space_x =self.settings.screen_width -(2* gnome_width)
        number_gnomes_x =available_space_x // (2*gnome_width)

        #determine the number of rows of aliens that fit on the screen
        player_height =self.player.rect.height
        available_space_y =(self.settings.screen_height -player_height)
        number_rows=available_space_y // (2 *gnome_height)

        #create the firs row of gnomes
        for row_number in range(number_rows):
            for gnome_number in range(number_gnomes_x):
                self._create_gnome(gnome_number, row_number)
            
    def _create_gnome(self, gnome_number, row_number):
        #create and alien and place it in the row. 
        gnome =Gnome(self)
        gnome_width, gnome_height= gnome.rect.size
        gnome_width =gnome.rect.width
        gnome.x= gnome_width +1.75 * gnome_width * gnome_number
        gnome.rect.x = gnome.x
        gnome.rect.y=gnome_height+1 * gnome.rect.height * row_number
        self.gnomes.add(gnome)

    def _check_army_edges(self):
        """Respond appropriately if any gnomes have reached an edge"""
        for gnome in self.gnomes.sprites():
            if gnome.check_edges():
                self._change_army_direction()
                break

    def _change_army_direction(self):
        for gnome in self.gnomes.sprites():
            gnome.rect.y+=self.settings.army_drop_speed
        self.settings.army_direction *= -1
    
    def _update_meteors(self):
        self.meteors.update()
        if pygame.sprite.spritecollideany(self.player, self.meteors):
            self._player_hit()

    def _update_gnomes(self):
        self._check_army_edges()
        self.gnomes.update()
        #look for gnome-player collisions.
        if pygame.sprite.spritecollideany(self.player, self.gnomes):
            self._player_hit()
        
        #look for gnomes hitting the bottom of the screen.
        self._check_gnomes_bottom()
    
    def _check_gnomes_bottom(self):
        """Check if gnomes have reached the bottom"""
        screen_rect=self.screen.get_rect()
        for gnome in self.gnomes.sprites():
            if gnome.rect.bottom >=600:
                self._player_hit()
                break

    def _player_hit(self):
        """Respond to the player being hit by a gnome"""
        if self.stats.players_left >0:
            #decrement lives_left and update scoreboard.
            self.stats.players_left -=1
            self.sb.prep_players()
            #get rid of any remaining gnomes and rainbows.
            self.gnomes.empty()
            self.rainbows.empty()
            self.meteors.empty()
            #Create a new army and center the player
            self._create_army()
            self._create_meteor()
            self.player.center_player()
            #pause
            sleep(1.0)
        else:
            self.stats.game_active =False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """update images on the screen, and flip to the new screen"""
        pygame.display.flip()
        self.screen.blit(self.background_image, [0, 0])
        self.player.blitme()
        self.meteors.draw(self.screen)
        for rainbow in self.rainbows.sprites():
            rainbow.blitme()
        self.gnomes.draw(self.screen)

        self.sb.show_score()
        #draw button if game is inactive
        if  not self.stats.game_active:
            self.play_button.draw_button()


if __name__ == '__main__':
    gp=GameProject()
    gp.run_game()
    