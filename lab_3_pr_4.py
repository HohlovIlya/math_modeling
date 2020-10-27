import numpy as np
N=int(input('введите число:_'))
M=int(input('введите число:_'))
mxn=np.ndarray(shape=(N,M))
for i in range(N):
    for j in range(M):
        if i>0 and j>0:
            mxn[i][j]=np.sin(N*(i)+M*(j))
            if mxn[i][j]<0:
                mxn[i][j]=0
        else:
            mxn[i][j]=np.sin(N*(i+1)+M*(j+1))
            if mxn[i][j]<0:
                mxn[i][j]=0
print(mxn)

