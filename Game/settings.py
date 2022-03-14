
class Settings:
    """A class to store all settings for Game Project"""

    def __init__(self):
        """initialize game settings"""
        #screen settings
        self.screen_width =1200
        self.screen_height =736
        self.bg_color =(230, 230, 230)

        #player settings
        self.player_speed =1.5
        self.player_limit =3

        #how quicky the game speeds up
        self.speedup_scale =1.1

        self.initialize_dynamic_settings()

        #rainbow settings
        self.rainbow_speed =1.0
        self.rainbow_width =3
        self.rainbow_height=15
        self.rainbow_color = (255,0,0)
        self.rainbows_allowed =5

        #gnome settings
        self.gnome_speed =1
        self.army_drop_speed =10

        #fleet_direction of 1 represents right; -1 represents left.
        self.army_direction=1

        #how quickly the gnome point values increase
        self.score_scale =1.5

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""

        self.gnome_speed =1.0

        #fleet_direction of 1 represents right; -1 represents left.
        self.army_direction=1

        #scoring
        self.gnome_points=50

    def increase_speed(self):
        """Increase speed settings and alien values"""
    
        self.gnome_speed *=self.speedup_scale

        self.gnome_points =int(self.gnome_points *self.score_scale)