import matplotlib.pyplot as plt
import random
from random import choice

random.seed()

for i in range(1, 50):
    x = []
    y = []
    for j in range(0, 100000):
        last_y = 0
        if j > 1:
            last_y = y[j-1]

        random_step = choice([k for k in range(-1,2) if k != 0])

        x.append(j)
        y.append(last_y + random_step)

    plt.plot(x, y)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Simple Random Walk')
plt.show()