import numpy as np
import scipy.integrate as integrate
import sympy as sp


f=lambda x: 4*np.cos(0.5*x)*np.exp(-5/4*x) + 2*np.sin(4.5*x)*np.exp(x/8) + 2
a=1.3; b=2.2; alpha=0; beta=5/6; points=np.array([a, (a+b)/2, b]); n=10
p=lambda x, j: (x-a)**(-alpha) * (b-x)**(-beta)*x**j

def Neuton_Cotes(a, b, n=3):  # Default n is 3
    x_n = np.linspace(a, b, n)  # Split the segment into n parts
    M = np.array([integrate.quad(p, a, b, args = (j))[0] for j in range(n)])
    X = np.array([[x**i for x in x_n] for i in range(n)], dtype=np.float64)
    A = np.linalg.solve(X, M)
    return np.sum([A[j]*f(x_n[j]) for j in range(n)])

f_p = lambda x: (4*np.cos(0.5*x)*np.exp(-5/4*x) + 2*np.sin(4.5*x)*np.exp(x/8) + 2) * (b-x)**(-beta)
print('Absolute error is', np.abs(Neuton_Cotes(a, b) - integrate.quad(f_p, a, b)[0]))



def cqf(a, b, points):
    cqf = 0
    for i in range(points.size-1):
        cqf += Neuton_Cotes(points[i], points[i+1])
    return cqf


n=40; m=2; L=2
points1, points2 = np.linspace(a, b, n), np.linspace(a, b, n*L)
CQF1, CQF2 = cqf(a, b, points1), cqf(a, b, points2)
R1, R2 = (CQF2 - CQF1)/(1-L**(-m)), (CQF2 - CQF1)/(L**m-1)
print('R1 =', R1, '\nR2 =', R2)

eps = 1e-6
h_opt = (b-a)/n*((eps/abs(R1)))**(1/m)
n_opt = int((b-a)//h_opt)
print('Optimal step is', h_opt ,'. So it\'s mean we shoud split our interval into', n_opt, 'parts.')

r = 4
h = np.array([n*L**i for i in range(r)])
S = np.array([-cqf(a, b, np.linspace(a, b, h[i])) for i in range(h.size)], dtype=np.float64)
H = np.array([[(b-a)/h[i-1]**(j+1) for j in range(r)] for i in range(r)])
H[:, 0] = -1
C = np.linalg.solve(H, S)
R1 = 0
for i in range(1, C.size):
    R1 += C[i] * H[-1, i]
print('Integral value is', C[0])
print('Error estimate is', R1)