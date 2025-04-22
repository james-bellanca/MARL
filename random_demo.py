import random
from custom_environment.env.custom_environment import GridExplorationMaskedEnv


def run_random(steps=20):
    env = GridExplorationMaskedEnv()
    obs, infos = env.reset()
    print("=== Initial ===")
    env.render()

    for _ in range(steps):
        actions = {}
        for agent, data in obs.items():
            mask = data["action_mask"]





if __name__ == "__main__":
    run_random(steps=10)