from unityagents import UnityEnvironment
import numpy as np
import torch

from collections import deque
from agent import Agent
from model import Actor, Critic
from tensorboard import Tensorboard
from datetime import datetime

# import matplotlib.pyplot as plt

env = UnityEnvironment(file_name='files/Reacher.app')
brain_name = env.brain_names[0]
env_info = env.reset(train_mode=True)[brain_name]
brain = env.brains[brain_name]
agent = Agent(state_size=env_info.vector_observations.shape[1], action_size=brain.vector_action_space_size, random_seed=10, agent_count=20)
models = (Actor, Critic)
tag = "run_1"
tensorboard = Tensorboard(models, './logs/logs-{}-{}'.format(tag, datetime.now()))


# number of agents
num_agents = len(env_info.agents)
print('Number of agents:', num_agents)

# size of each action
action_size = brain.vector_action_space_size
print('Size of each action:', action_size)

# examine the state space
states = env_info.vector_observations
state_size = states.shape[1]
print('There are {} agents. Each observes a state with length: {}'.format(states.shape[0], state_size))
print('The state for the first agent looks like:', states[0])


def ddpg(n_episodes=500):
    scores_deque = deque(maxlen=100)
    scores = []
    for i_episode in range(1, n_episodes + 1):
        env_info = env.reset(train_mode=True)[brain_name]
        state = env_info.vector_observations
        agent.reset()
        score = np.zeros(num_agents)
        while True:
            action = agent.act(state)
            env_info = env.step(action)[brain_name]
            next_state = env_info.vector_observations
            reward = env_info.rewards
            done = env_info.local_done
            agent.step(state, action, reward, next_state, done)
            state = next_state
            score += np.array(reward)

            tensorboard.add_scalar("{}-actor".format(tag), agent.loss[0])
            tensorboard.add_scalar("{}-critic".format(tag), agent.loss[1])
            if np.any(done):
                break
        scores.append(score)
        scores_deque.append(score)
        ep_mean_score = np.mean(score)
        hundred_ep_average = np.mean(scores_deque)
        tensorboard.add_scalar("{}-mean-scores".format(tag), ep_mean_score)
        tensorboard.add_scalar("{}-100-ep-scores".format(tag), hundred_ep_average)
        print('\rEpisode {}\tAverage Score: {}\tScore: {}'.format(i_episode, hundred_ep_average, ep_mean_score),
              end="")
        if i_episode % 100 == 0 or hundred_ep_average > 30:
            torch.save(agent.actor_local.state_dict(), 'checkpoint_actor-{}.pth'.format(i_episode))
            torch.save(agent.critic_local.state_dict(), 'checkpoint_critic-{}.pth'.format(i_episode))
            print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, hundred_ep_average))
        if hundred_ep_average > 30:
            torch.save(agent.actor_local.state_dict(), 'checkpoint_actor_30+-{}.pth'.format(i_episode))
            torch.save(agent.critic_local.state_dict(), 'checkpoint_critic_30+-{}.pth'.format(i_episode))
            np.save("scores_30+-{}".format(i_episode), scores)
            break

    return scores


scores = ddpg()

