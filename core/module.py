"""Base module class."""

class Module:
    def __init__(self):
        self.training = True

    def train(self):
        self.training = True
        return self

    def eval(self):
        self.training = False
        return self

    def forward(self, *args, **kwargs):
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)
