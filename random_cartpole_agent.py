from functools import total_ordering
import gym
from typing import TypeVar
import random

Action = TypeVar("Action")


class RandomActionWrapper(gym.ActionWrapper):
    def __init__(self, env, epsilon=0.1):
        super().__init__(env)
        self.epsilon = epsilon

    def action(self, action):
        if random.random() < self.epsilon:
            print("random !")
            return self.env.action_space.sample()
        return action


env = RandomActionWrapper(gym.make("CartPole-v0"))
env = gym.wrappers.Monitor(env, "recording", force=True)
obs = env.reset()
total_reward = 0.0

while True:
    obs, reward, done, _ = env.step(0)
    total_reward += reward
    if done:
        break

print(f"total reward : {total_reward}")
