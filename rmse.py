import numpy as np
from scipy.sparse import lil_matrix
import pdb

def rmse(predictions,targets):
    return np.sqrt(((predictions - targets)** 2).mean())


predicted_new = []
actual = []
with open('res2015.txt') as f:
    for line in f.readlines():
        tokens = line.split(" ")
        predicted_new.append(float(tokens[0]))
        actual.append(float(tokens[1]))

    print rmse(np.array(predicted_new), np.array(actual))