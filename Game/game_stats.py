class GameStats:
    """Track statistics for Gnomes Invastion"""

    def __init__(self, gp_game):
        """Initialize statistics"""
        self.settings =gp_game.settings
        self.reset_stats()

        #start Gnomes Invasion in an active state.
        self.game_active =False

        #high scoe should never be reset.
        self.high_score =0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.players_left =self.settings.player_limit
        self.score =0
        self.level =1
