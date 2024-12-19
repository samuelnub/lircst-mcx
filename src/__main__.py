import pmcx
import numpy as np
import matplotlib.pyplot as plt

res = pmcx.run(nphoton=1000000, 
               vol=np.ones([60, 60, 60], dtype='uint8'), 
               tstart=0, 
               tend=5e-9, 
               tstep=5e-9, 
               srcpos=[30,30,0], 
               srcdir=[0,0,1], 
               prop=np.array([[0, 0, 1, 1], [0.005, 1, 0.01, 1.37]]),
               )
res['flux'].shape

plt.imshow(np.log10(res['flux'][30,:, :]))
plt.show()