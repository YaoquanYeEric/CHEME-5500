import matplotlib.pyplot as plt
import numpy as np

class Graph(object):
    
    def f(x):
        return x
    
    #def __init__(self,func = lambda x: x):
        #self.func = func
    
        
    def __init__(self,func = f):
        self.func = func
    
    def plot(self):
        
        x = np.arange(0, 5, 0.1)
        y = []
        for i in np.arange(0, 5, 0.1):
            y.append(self.func(i))
            
        plt.plot(x,y)
        plt.show()