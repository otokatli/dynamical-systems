import matplotlib.pyplot as plt
from numpy import linspace, meshgrid, sin, zeros
import seaborn as sns

sns.set()


def dx(t, x):
    return x[1], -sin(x[0])


if __name__ == "__main__":
    t = 0

    x1 = linspace(-4, 4, 10)
    x2 = linspace(-2, 2, 10)

    X1, X2 = meshgrid(x1, x2)

    u, v  = zeros(X1.shape), zeros(X2.shape)
    
    num_1, num_2 = X1.shape
    for i in range(num_1):
        for j in range(num_2):
            x = X1[i, j]
            y = X2[i, j]
            u[i, j], v[i, j] = dx(t, [x, y])
            
    fig, ax = plt.subplots()
    ax.quiver(X1, X2, u, v)
    ax.set_xlim((-4, 4))
    ax.set_ylim((-2, 2))
    ax.set_xlabel(r'$x_1$')
    ax.set_ylabel(r'$x_2$')
    plt.savefig("phase_plot.png")
