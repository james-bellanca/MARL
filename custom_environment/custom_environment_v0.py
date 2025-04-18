"""
Version 0 entry point for the custom GridWorld environment.
"""
from custom_environment.env.custom_environment import GridWorldEnv


def env():
    """
    Factory: returns a new GridWorldEnv instance.
    """
    return GridWorldEnv()


if __name__ == "__main__":
    # Quick test
    environment = env()
    environment.reset()
    environment.render()