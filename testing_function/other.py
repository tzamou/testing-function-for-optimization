import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

class StyblinsliTang:
    '''
    global minimum: f(x)=-39.16599*d ,if x=(-2.903534, -2.903534, ..., -2.903534)
    input domain recommended x ∈ [-5,5]
    '''
    def function(self, x):
        x = np.array(x)
        return 1/2*(np.sum(x**4-16*x**2+5*x))
    def get_latex(self):
        return r'$\frac{1}{2}\sum_{i=1}{d}(x_i^4-16x_i^2+5x_i)$'
    def plot(self):
        pass



if __name__=='__main__':
    func = StyblinsliTang()
    d=1
    print(func.function(x=[-2.903533 for i in range(d)]))
    print(-39.16599*d)
    print(func.function(x=[-2.903534 for i in range(d)]))