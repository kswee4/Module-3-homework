import jax
import jax.numpy as jnp
from typing import Callable
from matplotlib import pyplot as plt

def phi(y : float, beta : float) -> float:
    return -1.0 / beta * jnp.log(-y + 1e-9)

x_points = jnp.linspace(-3.0, 0.0, 120)

beta_01 = [phi(y, 0.1) for y in x_points]
beta_05 = [phi(y, 0.5) for y in x_points]
beta_1  = [phi(y, 1.0) for y in x_points]
beta_10 = [phi(y, 10.0) for y in x_points]

plt.plot(x_points, beta_01, label='β = 0.1')
plt.plot(x_points, beta_05, label='β = 0.5')
plt.plot(x_points, beta_1, label='β = 1')
plt.plot(x_points, beta_10, label='β = 10')

plt.title(f"$ϕ(y) = − 1/β * ln(−y)$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend(ncol=2)
plt.show()


