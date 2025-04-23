'''
Simple program to load and test a custom environment using PettingZoo's built in tests.
'''
from custom_environment.env.base_env import GridExplorationMaskedEnv

from pettingzoo.test import parallel_api_test

if __name__ == "__main__":
    env = GridExplorationMaskedEnv()
    parallel_api_test(env, num_cycles=1_000_000)