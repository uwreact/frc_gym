import gym
import gym_frc

import numpy as np
import jsonable
import random

env = gym.make('Graph-v2019')

action_space_size = env.action_space.to_jsonable
state_space_size = env.observation_space


# State space size by action space size
q_table = np.zeros((4, 21))


num_episodes = 90000
max_steps_per_episode = 100

learning_rate = 0.2
discount_rate = 0.91

exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.01

rewards_all_episodes = []


for episode in range(num_episodes):
    state = env.reset()
    rewards_current_episode = 0

    for step in range(max_steps_per_episode): 
        # Exploration-exploitation 

        exploration_rate_threshold = random.uniform(0, 1)
        if exploration_rate_threshold > exploration_rate:
            action = np.argmax(q_table[2,:]) 
        else:
            action = env.action_space.sample()

        new_state, reward, done, info = env.step(action)


        q_table[new_state[0], action] = q_table[new_state[0], action] * (1 - learning_rate) + learning_rate * (reward + discount_rate * np.max(q_table[new_state[0], :]))

        #print(q_table)

        state = new_state
        rewards_current_episode += reward 

        if done:
            break
    
    exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate*episode)
 
    rewards_all_episodes.append(rewards_current_episode)

rewards_per_thosand_episodes = np.split(np.array(rewards_all_episodes),num_episodes/10000)
count = 1000


print(q_table)
print("********Average reward per thousand episodes********\n")
for r in rewards_per_thosand_episodes:
    print(count, ": ", str(sum(r/1000)))
    count += 1000


