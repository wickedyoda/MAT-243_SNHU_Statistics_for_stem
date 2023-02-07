from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("http://data-analytics.zybooks.com/Cars.csv")

fig = plt.figure()

#mplot3d is needed for projection='3d'
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['Speed'], df['Quality'], df['Angle'], c='b', marker='o')

ax.set_xlabel('Speed, X1')
ax.set_ylabel('Angle, X2')
ax.set_zlabel('Quality, Y')

plt.show()