import scipy.optimize
import math
import time
def f(x):
    return math.cos(x)/(1+x**2)
def derivative(x):
    return (-math.sin(x)/(1+x**2))-((math.cos(x)*2*X)/(1+x**2)**2)
print (scipy.optimize.bisect(f(x),0.1,2.4))
start_time=time.time()
for i in range(10000):
