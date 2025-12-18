# @title Default title text
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)', color='red', linewidth=3)
plt.title('Line Plot of sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.legend()
plt.show()