from RL_games.Abstract.game import *
import numpy as np

class GreedySpider(Game):
    
    def __init__(self,player_list,start_state):
        super().__init__(player_list)
        self.set_state(start_state)
        self.player = self.player_list[0]
        self.spider = self.player_list[1]
        
    def set_state(self, state):
        self.state = state
        
    def step(self):
        #spider takes a turn
        #player takes a turn
        
        self.last_state = self.state
        
        next_state_ps = self.player.take_turn(self.state)
        
        reward, terminal = self.done(next_state_ps)
        
        if not terminal:
            next_state = self.spider.take_turn(next_state_ps)
            reward, terminal = self.done(next_state)
        else:
            next_state = next_state_ps
        self.state = next_state
        
        return self.state, self.last_state, reward, terminal 
    
    def _get_reachable_nodes(self, A, node, steps = 0):
        r = A[node,:]
        
        if steps == 0:
            steps = A.shape[0]
        elif steps == 1:
            return np.where(r > 0)[0]
        
        for _ in range(steps-1):
            r = np.inner(A.T,r)
        return np.where(r > 0)[0]
        
    
    def done(self, state):
        A, spider, flies = state
        reachable = self._get_reachable_nodes(A, int(np.where(spider > 0)[0]), steps = 0)
        where_flies = np.where(flies > 0)[0]
        
        if np.sum(flies) == 0:
            return -1, True
        elif len(set(reachable).intersection(where_flies)) == 0:
            return np.sum(flies)/len(flies), True
        else:
            return 0, False
        
        
        
        
        
    
    
    
        
        
    