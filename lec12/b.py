import matplotlib.pyplot as plt
import numpy as np
n = int(input("enter a number : "))
x = np.random.uniform(-1,1,n)
y = np.random.uniform(-1,1,n)
total_points = np.arange(1,n+1)

in_circle = x**2+y**2<=1
# print(in_circle)
count_cf = np.cumsum(in_circle)
# print(count_cf[-1])
pi_value = (4*count_cf)/total_points
fig,ax = plt.subplots(1,2,figsize = (1,1000),layout = "constrained")
ax[0].plot(total_points,pi_value)
ax[0].axhline(np.pi,color = "red")
ax[0].set_title("pi graph")
ax[0].set_xlabel("number of iterations")
ax[0].set_ylabel("pi values")
ax[1].scatter(x[in_circle],y[in_circle],s = 0.1)
ax[1].scatter(x[~in_circle],y[~in_circle],s=0.1)
ax[1].set_xlabel("xaxis")
ax[1].set_ylabel("yaxis")
circle = plt.Circle((0,0),1, fill = False)
ax[1].add_patch(circle)
# print(pi_value)
plt.show()