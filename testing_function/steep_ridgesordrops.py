import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

class Michalewicz:
    '''
    global minimum: d=2 f(x)=-1.8013 ,if x=(2.2, 1.57)
                    d=5 f(x)=-4.687658
                    d=10 f(x)=-9.66015
    input domain recommended x ∈ [0,pi]
    '''
    def __init__(self, m=10):
        '''

        :param m: 10
        '''
        self.m = m
    def function(self, x):
        x = np.array(x)
        return -1*np.sum(np.sin(x)*np.sin(np.arange(1,len(x)+1)*x**2/np.pi)**(2*self.m))
    def get_latex(self):
        return r'$f(x)=-\sum_{i=1}^dsin(x_i)sin^{2m}(\frac{ix_i^2}{\pi})$'
    def plot(self):
        pass


if __name__=='__main__':
    func = Michalewicz()
    d=2
    print(func.function(x=[2.203,np.pi/2]))