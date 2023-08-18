import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

class Zakharov:
    '''
    global minimum: f(x)=0 ,if x=(0, 0, 0, ..., 0)
    input domain recommended x ∈ [-5,10]
    '''
    def function(self, x):
        x = np.array(x)
        return np.sum(x**2)+np.sum(0.5*np.arange(1,len(x)+1)*x)**2+np.sum(0.5*np.arange(1,len(x)+1)*x)**4
    def get_latex(self):
        return r'$f(x)=\sum_{i=1}^dx_i^2+(\sum_{i=1}^d0.5ix_i)^2+(\sum_{i=1}^d0.5ix_i)^4$'
    def plot(self):
        pass

if __name__=='__main__':
    func = Zakharov()
    d=6
    print(func.function(x=[10 for i in range(d)]))