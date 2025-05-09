import functools
import random

import numpy as np
from gymnasium.spaces import Discrete, Box, MultiBinary, Dict
from pettingzoo import ParallelEnv


class GridExplorationMaskedEnv(ParallelEnv):
    """
    A ParallelEnv where each agent explores a shared grid.
    Observations include:
      - `grid`: the full grid state (0=unvisited, >0 = agent_id+1)
      - `action_mask`: which of the 4 moves are valid (up/right/down/left)
    Rewards: +1 for visiting a new cell, 0 otherwise.
    Episode truncates after max_steps.
    """

    metadata = {"name": "grid_exploration_masked_v0"}

    def __init__(self, grid_size=(10,10), num_agents=2, max_steps=100, obs_radius=None, comm_level='none'):
        self.grid_size = grid_size
        self._num_agents = num_agents
        self.max_steps = max_steps
        self.obs_radius = obs_radius

        # agent IDs: "agent_0", "agent_1", ...
        self.possible_agents = [f"agent_{i}" for i in range(self._num_agents)]

        # internal state placeholders
        self.grid = None
        self.agent_positions = {}
        self.step_count = None
        self.agents = []

    def reset(self, seed=None, options=None):
        # Initialize blank grid and agent list
        self.grid = np.zeros(self.grid_size, dtype=int)
        self.step_count = 0
        self.agents = self.possible_agents[:]

        # Place agents randomly without overlap
        taken = set()
        for a in self.agents:
            while True:
                pos = (random.randrange(self.grid_size[0]),
                       random.randrange(self.grid_size[1]))
                if pos not in taken:
                    taken.add(pos)
                    self.agent_positions[a] = pos
                    # Mark starting cell visited
                    self.grid[pos] = self.agent_id(a) + 1
                    break

        obs = {a: self._make_observation(a) for a in self.agents}
        infos = {a: {} for a in self.agents}
        return obs, infos

    def step(self, actions):
        # Move each agent
        for a, act in actions.items():
            x, y = self.agent_positions[a]
            if act == 0 and x > 0:
                x -= 1
            elif act == 1 and y < self.grid_size[1] - 1:
                y += 1
            elif act == 2 and x < self.grid_size[0] - 1:
                x += 1
            elif act == 3 and y > 0:
                y -= 1
            self.agent_positions[a] = (x, y)

        # Compute rewards and update grid visits
        rewards = {}
        for a in self.agents:
            pos = self.agent_positions[a]
            if self.grid[pos] == 0:
                rewards[a] = 1
            else:
                rewards[a] = 0
            self.grid[pos] = self.agent_id(a) + 1

        # Increment step and check truncation
        self.step_count += 1
        truncations = {a: (self.step_count >= self.max_steps) for a in self.agents}
        terminations = {a: False for a in self.agents}

        obs = {a: self._make_observation(a) for a in self.agents}
        infos = {a: {} for a in self.agents}

        # End episode if all truncated
        if all(truncations.values()):
            self.agents = []

        return obs, rewards, terminations, truncations, infos

    def _compute_mask(self, agent):
        """Return a length-4 binary mask of valid moves for this agent."""
        x, y = self.agent_positions[agent]
        H, W = self.grid_size
        # up, right, down, left
        return np.array([
            x > 0,
            y <  W - 1,
            x <  H - 1,
            y >  0,
        ], dtype=np.int8)

    def _make_observation(self, agent):
        full = self.grid.copy()
        r, c = self.agent_positions[agent]

        if self.obs_radius is None:
            local = full
        else:
            R = self.obs_radius
            H, W = self.grid_size
            # start/end indices, clipped to grid
            r0, r1 = max(0, r-R), min(H, r+R+1)
            c0, c1 = max(0, c-R), min(W, c+R+1)

            # everything outside [r0:r1, c0:c1] becomes -1
            local = np.full_like(full, fill_value=-1)
            local[r0:r1, c0:c1] = full[r0:r1, c0:c1]

        return {
            "grid": local,
            "action_mask": self._compute_mask(agent)
        }

    def render(self):
        """
        ASCII render with row/column numbers, marking:
        - [A], [B], … for current agent positions
        -  0, 1, … for cells they have visited
        -  . for unvisited cells
        """
        H, W = self.grid_size

        # 1) Column header
        header = "    " + "  ".join(f"{j:2}" for j in range(W))
        print(header)

        # 2) Each row
        for i in range(H):
            # row index
            row_str = f"{i:2}  "
            for j in range(W):
                # is there an agent here?
                agent_here = None
                for a in self.agents:
                    if self.agent_positions[a] == (i, j):
                        agent_here = a
                        break

                if agent_here is not None:
                    # letter based on agent index
                    ch = chr(ord("A") + self.agent_id(agent_here))
                    cell = f"[{ch}]"
                else:
                    v = self.grid[i, j]
                    if v > 0:
                        # visited cell: show agent index (v-1)
                        cell = f" {v-1} "
                    else:
                        cell = " . "
                row_str += cell + " "
            print(row_str)
        print()

    @functools.lru_cache(maxsize=None)
    def observation_space(self, agent):
        if self.obs_radius is None:
            shape = self.grid_size
        else:
            # local square of size (2R+1) but clipped at borders
            R = self.obs_radius
            max_dim = max(self.grid_size)
            # we’ll declare the box shape as full grid for simplicity,
            # or as (2R+1, 2R+1) if you prefer exact local dims.
            shape = self.grid_size
        return Dict({
            "grid": Box(low=-1,
                        high=self._num_agents,
                        shape=shape,
                        dtype=int),
            "action_mask": MultiBinary(4)
        })

    @functools.lru_cache(maxsize=None)
    def action_space(self, agent):
        return Discrete(4)

    def agent_id(self, agent):
        return self.possible_agents.index(agent)