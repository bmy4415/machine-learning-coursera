import numpy as np


def n_size_ndarray_creation(n, dtype=np.int):
    return np.arange(n**2, dtype=dtype).reshape((n, n))


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type == 0:
        return np.zeros(shape=shape, dtype=dtype)
    elif type == 1:
        return np.ones(shape=shape, dtype=dtype)
    elif type == 99:
        return np.empty(shape=shape, dtype=dtype)


def change_shape_of_ndarray(X, n_row):
    return np.squeeze(np.reshape(X, (n_row, -1)))


def concat_ndarray(X_1, X_2, axis):
    if X_1.ndim == 1:
        x1_2d = np.expand_dims(X_1, axis=0)
    else:
        x1_2d = X_1

    if X_2.ndim == 1:
        x2_2d = np.expand_dims(X_2, axis=0)
    else:
        x2_2d = X_2

    # return False if concatenation is impossible
    if x1_2d.shape[1-axis] != x2_2d.shape[1-axis]:
        return False
    else:
        return np.concatenate((x1_2d, x2_2d), axis=axis)

def normalize_ndarray(X, axis=99, dtype=np.float32):
    if axis == 99:
        axis = None

    if X.ndim == 1:
        # vector
        return (X-np.mean(X)) / np.std(X)
    else:
        # matrix
        mean = np.mean(X, axis=axis)
        std = np.std(X, axis=axis)

        if axis:
            # broadcasting
            mean = np.expand_dims(mean, axis=axis)
            std = np.expand_dims(std, axis=axis)

        return (X-mean) / std


def save_ndarray(X, filename="test.npy"):
    np.save(filename, X)


def boolean_index(X, condition):
    return np.where(eval(str('X') + condition))


def find_nearest_value(X, target_value):
    idx = np.argmin(np.abs(X-target_value))
    return X[idx]


def get_n_largest_values(X, n):
    return X[np.argsort(-X)[:n]]

