import numpy as np

def get_array(size):
    if type(size) is int:
        return np.random.rand(size)
    return np.random.rand(*size)

    