from pettingzoo.utils.env import AECEnv
import numpy as np
import matplotlib.pyplot as plt
import random
from gym import spaces

class GridWorldEnv(AECEnv):
    metadata = {'render.modes': ['human', 'rgb_array']}

    def __init__(self, grid_size=(10, 10), num_agents=2):
        super().__init__()
        self.grid_size = grid_size
        self._num_agents = num_agents

        # 0 = unvisited; 1...num_agents = agent‐IDs
        self.grid = np.zeros(self.grid_size, dtype=int)

        # Agent bookkeeping
        self.agents = [f"agent_{i}" for i in range(self._num_agents)]
        self.possible_agents = self.agents[:]
        self.agent_name_mapping = {a: i for i, a in enumerate(self.agents)}

        # Action space: 0=up, 1=right, 2=down, 3=left
        self.action_spaces = {a: spaces.Discrete(4) for a in self.agents}

        # (Not used in the demo) each agent could observe the full grid
        self.observation_spaces = {
            a: spaces.Box(low=0, high=self._num_agents, shape=self.grid_size, dtype=int)
            for a in self.agents
        }

        # Will hold (x,y) for each agent
        self.agent_positions = {}
        self.has_reset = False

    def reset(self, seed=None, return_info=False, options=None):
        # Clear grid
        self.grid[:] = 0
        # Place each agent at a random unique cell
        taken = set()
        for a in self.agents:
            while True:
                pos = (random.randrange(self.grid_size[0]),
                       random.randrange(self.grid_size[1]))
                if pos not in taken:
                    taken.add(pos)
                    self.agent_positions[a] = pos
                    # Mark visited
                    self.grid[pos] = self.agent_name_mapping[a] + 1
                    break
        self.has_reset = True
        return {} if not return_info else ({}, {})

    def step(self, agent, action):
        # Move one agent, mark its new cell visited
        x, y = self.agent_positions[agent]
        if action == 0 and x > 0:
            x -= 1
        elif action == 1 and y < self.grid_size[1] - 1:
            y += 1
        elif action == 2 and x < self.grid_size[0] - 1:
            x += 1
        elif action == 3 and y > 0:
            y -= 1

        self.agent_positions[agent] = (x, y)
        self.grid[x, y] = self.agent_name_mapping[agent] + 1

    def render(self, mode="human"):
        if not self.has_reset:
            self.reset()

        # Build a discrete colormap:
        # 0 -> light gray, 1 -> blue, 2 -> orange, etc.
        cmap = plt.cm.get_cmap("tab10", self._num_agents + 1)

        fig, ax = plt.subplots(figsize=(5, 5))
        im = ax.imshow(self.grid, cmap=cmap, vmin=0, vmax=self.num_agents, 
                       interpolation="none")

        # Outer border
        for spine in ax.spines.values():
            spine.set_edgecolor("black")
            spine.set_linewidth(2)

        # Cell boundaries
        ax.set_xticks(np.arange(self.grid_size[1] + 1) - 0.5, minor=True)
        ax.set_yticks(np.arange(self.grid_size[0] + 1) - 0.5, minor=True)
        ax.grid(which="minor", color="white", linewidth=1)

        ax.tick_params(
            which="both", bottom=False, left=False, labelbottom=False, labelleft=False
        )

        if mode == "human":
            plt.show()
        elif mode == "rgb_array":
            fig.canvas.draw()
            arr = np.array(fig.canvas.renderer.buffer_rgba())
            plt.close(fig)
            return arr

        plt.close(fig)