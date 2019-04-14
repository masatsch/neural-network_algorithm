import numpy as np

# step
def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def relu(x: np.ndarray) -> np.ndarray:
    return np.maximum(0, x)


def softmax(x: np.ndarray) -> np.ndarray:
    c: np.int = np.max(x)
    return np.exp(x - c) / np.sum(np.exp(x - c))


def step(x: np.ndarray) -> np.ndarray:
    return np.array(x > 0, dtype=np.int)


def identity(x: np.ndarray) -> np.ndarray:
    return x


# loss
def mean_squad_error(y: np.ndarray, t: np.ndarray) -> np.int:
    return 0.5 * np.sum((y - t) ** 2)


def cross_entropy(y: np.ndarray, t: np.ndarray) -> np.int:
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    delta = 1e-7
    return - np.sum(t * np.log(y + delta)) / batch_size