from pettingzoo.utils.env import AECEnv
from gym import spaces
import numpy as np
import matplotlib.pyplot as plt

class GridWorldEnv(AECEnv):
    metadata = {'render.modes': ['human', 'rgb_array']}

    def __init__(self, grid_size=(50, 50)):
        super().__init__()
        self.grid_size = grid_size
        self.grid = None
        self.agents = []
        self.possible_agents = []
        self.agent_name_mapping = {}
        self.observation_spaces = {}
        self.action_spaces = {}
        self.has_reset = False

    def reset(self, seed=None, return_info=False, options=None):
        self.grid = np.zeros(self.grid_size, dtype=int)
        self.has_reset = True
        return {} if not return_info else ({}, {})

    def step(self, agent, action):
        raise RuntimeError("No agents in the environment. Add agents before stepping.")

    def render(self, mode='human'):
        if not self.has_reset:
            self.reset()
        fig, ax = plt.subplots()
        ax.imshow(self.grid, cmap='Greys', interpolation='none')
        ax.set_xticks(np.arange(self.grid_size[1] + 1) - 0.5, minor=True)
        ax.set_yticks(np.arange(self.grid_size[0] + 1) - 0.5, minor=True)
        ax.grid(which='minor', color='black', linewidth=1)
        ax.tick_params(which='major', bottom=False, left=False,
                       labelbottom=False, labelleft=False)
        if mode == 'human':
            plt.show()
        elif mode == 'rgb_array':
            fig.canvas.draw()
            img = np.array(fig.canvas.renderer.buffer_rgba())
            plt.close(fig)
            return img
        plt.close(fig)

    def close(self):
        plt.close('all')