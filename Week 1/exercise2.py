import numpy as np
def sigmoid(x):
    return 1 / 1 + np.exp(-x)

def relu(x):
    return np.where(x > 0, x, 0) 
    # (condition, satisfied, unsatisfied)

def elu(x):
    return np.where(x > 0, x, 0.01 * (np.exp(x) - 1))