import numpy as np
from lab_3_pr_2 import h
from lab_3_pr_2 import a
from lab_3_pr_2 import b
from lab_3_pr_1 import g
n=np.cos(a)
m=np.tan(b)
l=np.tan(a)
x=g*h*m**2
y=2*n**2*(1-m*l)
v=np.sqrt(x/y)
print(v)