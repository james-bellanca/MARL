from custom_environment.env.custom_environment import GridExplorationMaskedEnv

from pettingzoo.test import parallel_api_test

if __name__ == "__main__":
    env = GridExplorationMaskedEnv()
    parallel_api_test(env, num_cycles=1_000_000)