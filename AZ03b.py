# 2. Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.
# import numpy as np
# random_array = np.random.rand(5) # массив из 5 случайных чисел
# print(random_array)

import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(5)
y = np.random.rand(5)

print("x =", x)
print("y =", y)

plt.scatter(x, y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Scatter Plot")
plt.show()
