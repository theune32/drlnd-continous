import torch
import torchvision.utils as vutils
import numpy as np
import torchvision.models as tv_models
from torchvision import datasets
from tensorboardX import SummaryWriter


class Tensorboard(object):

    def __init__(self, models, log_dir):
        self.writer = SummaryWriter(log_dir)
        self.models = models
        self.steps = {}

    def add_scalar(self, tag, value):
        if tag not in self.steps:
            self.steps[tag] = 0
        step = self.steps[tag]
        value = np.asarray([value])
        self.writer.add_scalar(tag, value, step)
        self.steps[tag] += 1

    def add_graphs(self, models):
        for model in models:
            self.writer.add_graph(model)



