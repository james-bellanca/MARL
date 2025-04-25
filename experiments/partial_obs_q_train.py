'''
Utilizes custom command line arguements to parameterize episodes of a q-learning
agent experiment and writing the results to a CSV file. Enables reusable experimentation 
of varying observability. 
'''

import argparse
import csv
import os
import random

import numpy as np
from custom_environment.env.base_env import GridExplorationMaskedEnv

def parse_args():
    parser = argparse.ArgumentParser(
        description="Train Q-learning on grid exploration with partial observability."
    )
    parser.add_argument("--obs_radius", type=int, default=None,
                        help="Observation radius (None for full grid).")
    parser.add_argument("--episodes",   type=int, default=2000,
                        help="Number of episodes to train.")
    parser.add_argument("--alpha",      type=float, default=0.1,
                        help="Learning rate α.")
    parser.add_argument("--gamma",      type=float, default=0.99,
                        help="Discount factor γ.")
    parser.add_argument("--epsilon",    type=float, default=0.2,
                        help="Exploration rate ε.")
    parser.add_argument("--max_steps",  type=int, default=100,
                        help="Max steps per episode (truncation).")
    parser.add_argument("--grid_size",  type=int, nargs=2, default=(10,10),
                        help="Grid dimensions: HEIGHT WIDTH.")
    parser.add_argument("--output",     type=str, default="csvs/results.csv",
                        help="Output CSV file for logging results.")
    return parser.parse_args()

def main():
    args = parse_args()

    # Ensure the output directory exists
    out_dir = os.path.dirname(args.output)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    # Unpack grid dimensions
    H, W = args.grid_size

    # Create environment
    env = GridExplorationMaskedEnv(
        grid_size=(H, W),
        num_agents=2,
        max_steps=args.max_steps,
        obs_radius=args.obs_radius
    )

    S = H * W       # number of states
    N = len(env.possible_agents)
    Q = np.zeros((N, S, 4), dtype=float)  # Q-table: [agent, state, action]

    # Prepare CSV file
    with open(args.output, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "obs_radius", "episode",
            "coverage_time", "total_reward", "final_coverage"
        ])

        for ep in range(1, args.episodes + 1):
            obs, _ = env.reset()
            total_reward = 0
            coverage_time = None

            # Run one episode
            for step in range(1, args.max_steps + 1):
                actions = {}
                states  = {}

                # 1) Select ε-greedy actions
                for a in env.possible_agents:
                    if a not in env.agents:
                        continue
                    idx = env.possible_agents.index(a)

                    r, c = env.agent_positions[a]
                    s     = r * W + c
                    states[a] = s

                    mask = obs[a]["action_mask"]
                    if random.random() < args.epsilon:
                        valid = [i for i,m in enumerate(mask) if m]
                        act = random.choice(valid)
                    else:
                        qvals = Q[idx, s]
                        qvals = [qvals[i] if mask[i] else -np.inf for i in range(4)]
                        act = int(np.argmax(qvals))

                    actions[a] = act

                # 2) Step the environment
                obs_next, rewards, *_ = env.step(actions)

                # 3) Q-update and logging
                for a, act in actions.items():
                    idx = env.possible_agents.index(a)
                    r   = rewards[a]
                    total_reward += r

                    r2, c2 = env.agent_positions[a]
                    s2      = r2 * W + c2
                    mask2   = obs_next[a]["action_mask"]

                    q2 = Q[idx, s2]
                    q2 = [q2[i] if mask2[i] else -np.inf for i in range(4)]
                    max_q2 = max(q2) if any(mask2) else 0.0

                    Q[idx, states[a], act] += args.alpha * (
                        r + args.gamma * max_q2 - Q[idx, states[a], act]
                    )

                obs = obs_next

                # 4) Track when full coverage is first reached
                coverage = np.count_nonzero(env.grid) / float(S)
                if coverage_time is None and coverage >= 1.0:
                    coverage_time = step

                if not env.agents:
                    break

            if coverage_time is None:
                coverage_time = args.max_steps
            final_coverage = np.count_nonzero(env.grid) / float(S)

            writer.writerow([
                args.obs_radius, ep,
                coverage_time, total_reward, final_coverage
            ])

            if ep % 100 == 0:
                print(f"Ep {ep:4d} | "
                      f"TotalR {total_reward:5.1f} | "
                      f"CovTime {coverage_time:3d} | "
                      f"FinalCov {final_coverage:.2f}")

    print(f"\nTraining complete. Results saved to {args.output}")

if __name__ == "__main__":
    main()