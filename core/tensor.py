"""Tensor implementation for MiniGPT."""

class Tensor:
    def __init__(self, data, requires_grad=False):
        self.data = data
        self.requires_grad = requires_grad
        self.grad = None

    @property
    def shape(self):
        return getattr(self.data, "shape", None)
