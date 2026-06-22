import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5])
x1=np.linspace(0,5,50)
y=x1**3
print(y)
fig,ax = plt.subplots(figsize = (10,8),layout = "constrained")
ax.plot(x,y)
plt.show()
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")
ax.set_titles("Simple Graph: ")
ax.grid()
ax.legend()
plt.show()
 