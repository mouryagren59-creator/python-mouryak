from matplotlib import pyplot as plt
import numpy as np
a = np.random.uniform(-1,1,5)
b = np.random.uniform(-1,1,5)

fig,ax = plt.subplot(figsize=(10,7),layout = 'constrained')
ax.scatter(a,b,s=100)
ax.plot(a,b)
ax.grid()
ax.set_xlabel("x values")
ax.set_ylabel("y values")
ax.set_title("scatter diagram")
plt.show()