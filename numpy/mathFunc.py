import numpy as np
import matplotlib.pyplot as plt

print("{0:=^25}".format("pi(파이)"))
print(np.pi)

print("{0:=^25}".format("sin"))
print(np.sin(0))
print(np.sin(np.pi / 2))

print("{0:=^25}".format("cos"))
print(np.cos(0))
print(np.cos(np.pi / 2))

x = np.linspace(0, 2 * np.pi, 100)

plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')

plt.legend()
plt.show()

print("{0:=^25}".format("tan"))
x = np.linspace(-(np.pi) / 3, np.pi / 3, 100)

plt.plot(x, np.tan(x))
plt.axis('scaled')
plt.show()

print("{0:=^25}".format("log"))

x = np.linspace(0.1, 7.0, 100)

plt.plot(x, np.log(x))
plt.show()