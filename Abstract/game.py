'''
Abstract Game class that will be used by all specific games to setup the different function calls
'''


class Game:
    def __init__(self, player_list, render=False):
        self.player_list = player_list
        self.render = render
        self.state = None
    
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state
    
    def render_(self):
        pass
    
    def step(self):
        raise NotImplemented
    
    def done(self):
        raise NotImplemented
