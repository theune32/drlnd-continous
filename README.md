# DRLND: Continuous Control Project

## Overview and project details
In this project a model is trained to move a robotic arm towards a moving target location.
This project is setup is to use 20 agents simultaneously.

The unity environment has (per agent) an observation space of 33 parameters, correspongin to position, rotation,
velocity, and angular velocities of the arm and the position of the target location.
The action space consists of 4 parameters that correspond to the torgues for the joints with values between -1 and 1.

The reward function is +0.01 per time step that the end of the arm is inside the target location.

The goal is to have an average score of 30 or more across all 20 agents for the last 100 episodes.

## Setup
This repo can should be cloned from [https://github.com/theune32/drlnd-continous] and subsequently run:
`make setup`

The basic setup was shared by a colleague:
* create "files" directory
* Download the unity environment app: "Reacher.app"
* create a venv based on the "requirements.txt"
* download the "Continous_Cotrol.ipynb" from the Udacity repo, can be used by:
`jupyter notebook`

The repository contains 4 files:
* train.py: here the training, setup and logging are handled
* agent.py: all interactions with the model are handled here
* model.py: contains the model itself
* tensorboard.py: contains some wrapper functionality for tensorboardX

Tensorboard can be run by
`tensorboard --logdir` and accessing the dashboard from your browser [localhost:6006]
The log files for tensorboard are stored in /logs and contain information about the loss of the Actor and Critic and the
score over time (steps)

Saved model weights when finished are stored in the following checkpoint files:
- checkpoint_actor_30+-{episode number needed}.pth
- checkpoint_critic_30+-{episode number needed}.pth

The complete list of scores for a successful run are stored in: scores_30+-{episode number needed}.npy

End results and conclusions can be found in the "Report.md" file
