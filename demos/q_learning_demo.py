import random
import numpy as np
from custom_environment.env.base_env import GridExplorationMaskedEnv
import matplotlib.pyplot as plt

def q_learning(episodes=500, α=0.5, γ=0.99, ε=0.2):
    # 1) Create env and Q‑table
    env = GridExplorationMaskedEnv(grid_size=(10,10), num_agents=2, max_steps=50)
    H, W = env.grid_size
    S = H * W
    N = len(env.possible_agents)
    Q = np.zeros((N, S, 4))  # one Q‑table per agent

    rewards_per_ep = []

    for ep in range(episodes):
        obs, _ = env.reset()
        total_reward = 0

        # 2) Run one episode
        while env.agents:
            actions = {}
            states  = {}
            # 2a) Select ε‑greedy actions
            for a in env.possible_agents:
                if a not in env.agents:
                    continue
                idx = env.possible_agents.index(a)
                # current state s
                x,y = env.agent_positions[a]
                s    = x * W + y
                states[a] = s

                mask = obs[a]["action_mask"]
                if random.random() < ε:
                    valid = [i for i,m in enumerate(mask) if m]
                    a_choice = random.choice(valid)
                else:
                    # mask out invalid moves
                    qvals = Q[idx, s]
                    qvals = [qvals[i] if mask[i] else -np.inf for i in range(4)]
                    a_choice = int(np.argmax(qvals))
                actions[a] = a_choice

            # 2b) Step env
            obs_next, rewards, terms, truncs, _ = env.step(actions)

            # 2c) Q‑update for each agent
            for a, a_choice in actions.items():
                idx = env.possible_agents.index(a)
                s   = states[a]
                r   = rewards[a]
                total_reward += r

                x2,y2 = env.agent_positions[a]
                s2     = x2 * W + y2
                mask2  = obs_next[a]["action_mask"]

                # max_{valid a'}
                q2 = Q[idx, s2]
                q2 = [q2[i] if mask2[i] else -np.inf for i in range(4)]
                max_q2 = max(q2) if any(mask2) else 0.0

                # Bellman update
                Q[idx, s, a_choice] += α * (r + γ * max_q2 - Q[idx, s, a_choice])

            obs = obs_next

        rewards_per_ep.append(total_reward)

        # 3) Logging
        if (ep+1) % 50 == 0:
            avg = np.mean(rewards_per_ep[-50:])
            print(f"Episode {ep+1}, avg reward (last 50): {avg:.2f}")

    # 4) Plot learning curve
    plt.plot(np.arange(1, episodes+1), rewards_per_ep)
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.title("Q‐Learning on Grid Exploration")
    plt.show()

if __name__ == "__main__":
    q_learning(episodes=10000)