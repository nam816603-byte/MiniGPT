"""Activation modules for MiniGPT."""

from core.module import Module
from core import functional as F


class ReLU(Module):
    def forward(self, x):
        return F.relu(x)
