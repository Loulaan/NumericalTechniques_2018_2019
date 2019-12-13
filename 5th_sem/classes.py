import numpy as np
import math

from numpy.core.multiarray import ndarray

def funk( X, A, b):
    f= np.dot(X, np.dot(A, X))+ np.dot(X, b) +9
    return (f)

def q_funk(X, A, b):
    q_funk=np.dot(A, X)+b
    return (q_funk)

def mngs (X, A, b, eps):
    i=0
    q=q_funk(X, A, b)
    m = -(np.dot(q,(np.dot(A, X)+b))/(np.dot(q, (np.dot(A, q)))))
    Xk = X + m * q
    while np.linalg.norm(q_funk(Xk, A, b)) >= eps:
        q=q_funk(Xk, A, b)
        m = -(np.dot(q, (np.dot(A, Xk) + b)) / (np.dot(q, (np.dot(A, q)))))
        X = Xk
        Xk = Xk + m * q
        i+=1
    print( 'МНГС', Xk, funk(Xk, A, b), i)

def mps (X, A, b, eps):
    q = np.array([1, 0, 0])
    i=0
    #for i in range(3):
       # q = np.array([0, 0, 0])
        #q[i] = 1
    m = -(np.dot(q, (np.dot(A, X) + b)) / (np.dot(q, (np.dot(A, q)))))
    Xk = X + m * q
    grad=q_funk(Xk, A, b)
    #print(m)
    #print('q: ', q, 'X: ', Xk[0], Xk[1], Xk[2], 'grad: ', grad)
    while math.sqrt(grad[0]**2+grad[1]**2+grad[2]**2)>=eps:
            #np.linalg.norm(q_funk(Xk, A, b)) >= eps:
            i+=1
            q = np.array([0, 0, 0])
            q[i%3]=1
            m = -(np.dot(q, (np.dot(A, Xk) + b)) / (np.dot(q, (np.dot(A, q)))))
            #m = -np.dot(q.T, (np.dot(A, Xk) + b)) / np.dot(np.dot(q.T, A), q)
            X = Xk
            Xk = Xk + m * q
            grad = q_funk(Xk, A, b)
           # print(m)
           # print('q: ', q, 'X: ', Xk[0], Xk[1], Xk[2], 'grad: ', grad )
    print('МПС', Xk, funk(Xk, A, b), i)
#'grad: ', grad, 'norma: ', math.sqrt(grad[0]**2+grad[1]**2+grad[2]**2)