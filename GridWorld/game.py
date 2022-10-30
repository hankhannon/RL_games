import numpy as np
import math

class GridWorld:
    def __init__(self, height = 10, width = None, reward_location = None):

        self.height = height

        if width:
            self.width = width
        else:
            self.width = height

        if reward_location:
            self.rwd_loc = reward_location
        else:
            self.rwd_loc = (np.random.randint(height), np.random.randint(width))

    def step(self, state, action):
        if type(action) is int:
            action = self._decode_action(action)

        state += action

        pass



