import numpy as np
from classes import funk, q_funk, mngs, mps
A=np.array([[4, 1, 1], [1, 2*(3+0.1*9), -1], [1, -1, 2*(4+0.1*9)]])
b=np.array([1, -2, 3])
eps= 10**-6
X=np.array([0, 0, 0])
mngs(X, A, b, eps)
mps(X, A, b, eps)
#print(q_funk([0, 0, 0], A, b ))
