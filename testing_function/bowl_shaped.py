import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

class Perm:
    def __init__(self, beta=1):
        '''
        :param beta: 1

        global minimum: f(x)=0 ,if x=(1, 1/2, 1/3, ..., 1/d)
        input domain recommended x ∈ [-d,d]
        '''
        self.beta = beta
    def function(self, x):
        s = 0
        for i in range(1,len(x)+1):
            s1 = 0
            for j in range(1, len(x)+1):
                s1+=(j+self.beta)*(x[j-1]**i-1/j**i)
            s+=s1**2
        return s
    def get_latex(self):
        return r'$f(x)=\sum_{i=1}^d(\sum_{j=1}^d(j+\beta)(x_j^i-\frac{1}{j^i}))^2$'
    def plot(self):
        pass

class RotatedHyperEllipsoid:
    '''
    global minimum: f(x)=0 ,if x=(0, 0, ..., 0)
    input domain recommended x ∈ [-65.536,65.536]
    '''
    def function(self, x):
        s=0
        for i in range(1,len(x)+1):
            for j in range(1,i+1):
                print(i,j)
                s += x[j-1]**2
        return s
    def get_latex(self):
        return r'$f(x)=\sum_{i=1}^{d}\sum_{j=1}^ix_j^2$'
    def plot(self):
        pass

class Sphere:
    '''
    global minimum: f(x)=0 ,if x=(0, 0, ..., 0)
    input domain recommended x ∈ [-5.12,5.12]
    '''
    def function(self, x):
        x = np.array(x)
        return np.sum(x**2)
    def get_latex(self):
        return r'$f(x)=\sum{i=1}^dx_i^2$'
    def plot(self):
        pass

class SumOfDifferentPowers:
    '''
    global minimum: f(x)=0 ,if x=(0, 0, ..., 0)
    input domain recommended x ∈ [-1,1]
    '''
    def function(self, x):
        x = np.array(x)
        return np.sum(np.abs(x)**(np.array([i+2 for i in range(len(x))])))
    def get_latex(self):
        return r'$f(x)=\sum_{i=1}^d|x_i|^{i+1}$'
    def plot(self):
        pass

class SumSquares:
    '''
    global minimum: f(x)=0 ,if x=(0, 0, ..., 0)
    input domain recommended x ∈ [-10,10]
    '''
    def function(self, x):
        x = np.array(x)
        return np.sum(np.arange(1,len(x)+1)*x**2)
    def get_latex(self):
        return r'$f(x)=\sum_{i=1}^dix_i^2$'
    def plot(self):
        pass

class Trid:
    '''
    global minimum: f(x)=0 ,if x=(0, 0, ..., 0)
    input domain recommended x ∈ [-d^2,d^2]
    '''
    def function(self, x):
        x=np.array(x)
        return np.sum((x-1)**2)-np.sum(x[1:]*x[:-1])
    def get_latex(self):
        return r'$f(x)=\sum_{i=1}^d(x_i-1)^2-\sum_{i=1}^dx_ix_{i-1}$'
    def plot(self):
        pass

if __name__=='__main__':
    func = Trid()
    d=6
    print((-d*(d+4)*(d-1))/6)
    print(func.function(x=[(i+1)*(d-i) for i in range(d)]))
