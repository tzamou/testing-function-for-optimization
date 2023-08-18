import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

class DixonPrice:
    '''
    global minimum: f(x)=0 ,if x=2^(-(2^i-2)/2^i)
    input domain recommended x ∈ [-10,10]
    '''
    def function(self, x):
        x = np.array(x)
        return (x[0]-1)**2+np.sum(np.arange(2,len(x)+1)*(2*x[1:]**2-x[:-1])**2)
    def get_latex(self):
        return r'$f(x)=(x_1-1)^2+\sum_{i=1}^di(2x_i^2-x_{i-1})^2$'
    def plot(self):
        pass

class Rosenbrock:
    '''
    global minimum: f(x)=0 ,if x=(1, 1, 1, ..., 1)
    input domain recommended x ∈ [-2.048,2.048]
    '''
    def function(self, x):
        x = np.array(x)
        return np.sum(100*(x[1:]-x[:-1]**2)**2+(x[:-1]-1)**2)
    def get_latex(self):
        return r'$f(x)=\sum_{i=1}^{d-1}[100(x_{i+1}-x_i^2)^2+(x_i-1)^2]$'
    def plot(self):
        pass

if __name__=='__main__':
    func = Rosenbrock()
    d=6
    print(func.function(x=[1 for i in range(d)]))