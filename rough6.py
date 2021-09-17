# 9.a

class MyClass:
    x = 5


print(MyClass)

p1 = MyClass()
print(p1.x)

# 9.b

import math

print(math.sqrt(0))
print(math.sqrt(4))
print(math.sqrt(3.5))

import numpy as np
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])
print(np.dot(v, w), "\n")
print(np.dot(x, v), "\n")
print(np.dot(x, y))

import pandas as pd

data = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}
data_table = pd.DataFrame(data)
print(data_table)

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, x, label='linear')
plt.legend()
plt.show()


