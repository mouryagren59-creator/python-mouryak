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
fig,ax = plt.subplots(figsize = (12,6),layout = "constrained")
ax.plot(total_points,pi_value)
ax.axhline(np.pi,color = "red")
# print(pi_value)
plt.show()