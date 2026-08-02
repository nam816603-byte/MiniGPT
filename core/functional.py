"""Functional API for MiniGPT core."""

from core.tensor import Tensor


def relu(x: Tensor) -> Tensor:
    raise NotImplementedError("relu is not implemented yet")


def softmax(x: Tensor, dim: int = -1) -> Tensor:
    raise NotImplementedError("softmax is not implemented yet")
