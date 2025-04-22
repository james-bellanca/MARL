"""
Version 0 entry point for the custom GridWorld environment.
"""
from custom_environment.env.custom_environment import GridExplorationMaskedEnv


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