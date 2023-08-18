import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

class Ackley:
    def __init__(self,a=20,b=0.2,c=np.pi*2):
        '''

        :param a: recommended = 20
        :param b: recommended = 0.2
        :param c: recommended = 2pi

        global minimum: f(x)=0 ,if x=(0,0...,0)
        input domain recommended x ∈ [-32.768,32.768]
        '''
        self.a = a
        self.b = b
        self.c = c
    def function(self, x):
        x = np.array(x)
        return -self.a*np.exp(-self.b*np.sqrt(1/len(x)*np.sum(x**2)))-np.exp(1/len(x)*np.sum(np.cos(self.c*x)))+self.a+np.exp(1)
    def get_latex(self):
        return r'$f(x)=-a\times exp(-b\sqrt{\frac{1}{d}\sum_{i=1}^{d}x_i^2})-exp(\frac{1}{d}\sum_{i=1}^{d}cos(cx_i))+a+exp(1)$'
    def plot(self):
        plt.text(0,0.5,s=self.get_latex(),fontsize=12)
        plt.axis(False)
        plt.show()

class Bukin:
    '''
    global minimum: f(x)=0 ,if x=(-10, 1)
    input domain recommended x1 ∈ [-15, -5], x2 ∈ [-3, 3]
    '''
    def function(self, x):
        assert len(x)==2, 'Dimensions muse be 2.'
        x = np.array(x)
        return 100*np.sqrt(np.abs(x[1]-0.01*x[0]**2))+0.01*np.abs(x[0]+10)
    def get_latex(self):
        return r'$f(x)=100\sqrt{|x_2-0.01x_1^2|}+0.01|x_1+10|$'
    def plot(self):
        plt.text(0,0.5,s=self.get_latex(),fontsize=12)
        plt.axis(False)
        plt.show()

class Griewank:
    '''
    global minimum: f(x)=0 ,if x=(0,0...,0)
    input domain recommended x ∈ [-600,600]
    '''
    def function(self, x):
        x = np.array(x)
        return np.sum(x**2/4000)-np.prod(np.cos(x/np.sqrt(np.array([i+1 for i in range(len(x))]))))+1
    def get_latex(self):
        return r'$f(x)=\sum_{i=1}^d{\frac{x_i^2}{4000}}-\prod_{i=1}^{d}cos(\frac{x_i}{\sqrt{i}})+1$'
    def plot(self):
        pass

class Levy:
    '''
    global minimum: f(x)=0 ,if x=(1, 1, 1, ..., 1)
    input domain recommended x ∈ [-10,10]
    '''
    def function(self, x):
        w = (np.array(x)+3)/4
        return np.sin(np.pi*w[0])**2+np.sum((w[:-1]-1)**2*(1+10*np.sin(np.pi*w[:-1]+1)**2))+(w[-1]-1)**2*(1+np.sin(2*np.pi*w[-1])**2)

    def get_latex(self):
        return r'$f(x)=sin^2(\pi w_1)+\sum_{i=1}^{d-1}(w_i-1)^2[1+10sin^2(\pi w_i+1)]+(w_d-1)^2[1+sin^2(2\pi w_d)], where w_i=\frac{3+x_i}{4}$'

    def plot(self):
        X = np.linspace(-5.12, 5.12, 100)
        Y = np.linspace(-5.12, 5.12, 100)
        X, Y = np.meshgrid(X, Y)

        Z = (X ** 2 - 10 * np.cos(2 * np.pi * X)) + \
            (Y ** 2 - 10 * np.cos(2 * np.pi * Y)) + 20

        fig = plt.figure(figsize=(5, 5))
        ax = fig.gca(projection='3d')
        ax.set_title('Rastrigin Function')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('fitness value')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                        cmap=cm.nipy_spectral, linewidth=0.08,
                        antialiased=True)
        # plt.savefig('rastrigin_graph.png')
        plt.show()

class Rastrgin:
    '''
    global minimum: f(x)=0 ,if x=(0, 0, 0, ..., 0)
    input domain recommended x ∈ [-5.12,5.12]
    '''
    def function(self, x):
        x = np.array(x)
        return 10*len(x)+np.sum(x**2-10*np.cos(2*np.pi*x))

    def get_latex(self):
        return r'$f(x)=10d+\sum_{i=1}^{d}[x_i^2-10cos(2\pi x_i)]$'

    def plot(self):
        pass

class Schwefel:
    '''
    global minimum: f(x)=0 ,if x=(420.9687, 420.9687...)
    input domain recommended x ∈ [-500,500]
    '''
    def function(self, x):
        return 418.9829*len(x)-np.sum(x*np.sin(np.sqrt(np.abs(x))))

    def get_latex(self):
        return r'$f(x)=418.9829d-\sum_{i=1}^{d}x_isin(\sqrt{|x_i|})$'

    def plot(self):
        pass

if __name__=='__main__':
    # func = Schwefel()
    # print(func.function(x=[420.9687 for i in range(5)]))
    func = Bukin()
    print(func.function(x=[-10,1]))
    func.plot()
