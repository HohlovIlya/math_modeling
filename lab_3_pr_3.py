import numpy as np
t=np.arange(0,5,0.1)
from physic_constant import g
x0=4#м
v0x=3#м/с
y0=0#м
x=x0+v0x*t
y=y0+v0x*t-g*(t**2)/2
j=np.ndarray(shape=(len(t),3))
t=np.ndarray(shape=(len(x),3))
r=np.ndarray(shape=(len(y),3))
print(t,r,j)
