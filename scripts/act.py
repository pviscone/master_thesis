import numpy as np
import matplotlib.pyplot as plt
import mplhep

mplhep.style.use("CMS")

x = np.linspace(-4, 4, 1000)
sigma = lambda x: 1 / (1 + np.exp(-x))

swish = lambda x, a: x * sigma(a * x)


def relu(x):
    res = np.zeros_like(x)
    res[x > 0] = x[x > 0]
    return res


plt.figure()
plt.close()
plt.figure(figsize=(3, 10))

plt.plot(x, swish(x, 3), label=r"Swish $(\beta=3)$", linewidth=2)
plt.plot(x, sigma(x), label="Logistic", linewidth=2)
plt.plot(x, relu(x), label="ReLU", linewidth=2)
plt.ylim(-0.5, 2)
# plt.plot(x, np.tanh(x), label="tanh")
plt.grid()

plt.legend()
plt.show()
