"""
Version 0 entry point for the custom GridWorld environment.

Displays initial instance of the ParallelEnv GridExplorationMaskedEnv.
"""
from custom_environment.env.base_env import GridExplorationMaskedEnv


def env():
    """
    Factory: returns a new GridWorldEnv instance.
    """
    return GridExplorationMaskedEnv()


if __name__ == "__main__":
    # Quick test
    environment = env()
    environment.reset()
    environment.render()