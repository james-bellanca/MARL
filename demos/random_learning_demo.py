'''
This script demonstrates 2 random agents exploring a grid world of arbitrary size.
The agents are initialized at random positions and take random actions in each step.
'''
import random
from custom_environment.env.base_env import GridExplorationMaskedEnv


def run_random(steps):
    env = GridExplorationMaskedEnv(grid_size=(10, 10), num_agents=2, max_steps=100)
    obs, infos = env.reset()
    print("=== Initial ===")
    env.render()

    for t in range(steps):
        actions = {}
        for agent, data in obs.items():
            mask = data["action_mask"]
            valid = [i for i, m in enumerate(mask) if m]
            actions[agent] = random.choice(valid)

        # 2) Step
        obs, rewards, terms, truncs, infos = env.step(actions)
        print(f"Step {t+1}, rewards={rewards}")
        env.render()

        # 3) Stop if done
        if not env.agents:
            break





if __name__ == "__main__":
    run_random(steps=25)