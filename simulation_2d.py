import numpy as np

def fibonacci(n):
    F = [0, 1]
    for i in range(2, n+1):
        F.append(F[-1] + F[-2])
    return np.array(F, dtype=float)

def initialize_lattice_2d(n, m, mode="fibonacci"):
    A = np.zeros((n, m))

    if mode == "fibonacci":
        Fx = fibonacci(n)
        Fy = fibonacci(m)
        for i in range(n):
            for j in range(m):
                A[i, j] = ((-1)**(i+j)) * Fx[i] * Fx[n-1-i] * Fy[j] * Fy[m-1-j]

    elif mode == "random":
        A = np.random.randn(n, m)

    elif mode == "exponential":
        for i in range(n):
            for j in range(m):
                A[i, j] = ((-1)**(i+j)) * (2**i) * (2**(n-1-i))

    return A / np.max(np.abs(A))

def update_2d(A, alpha=0.5, beta=0.2, gamma=0.3):
    n, m = A.shape
    A_new = np.zeros_like(A)

    for i in range(n):
        for j in range(m):
            nn = 0

            if i > 0: nn += A[i-1, j]
            if i < n-1: nn += A[i+1, j]
            if j > 0: nn += A[i, j-1]
            if j < m-1: nn += A[i, j+1]

            A_new[i, j] = (
                alpha * A[i, j]
                + beta * nn
                + gamma * np.tanh(A[i, j])
            )

    return A_new

def entropy(A):
    p = np.abs(A).flatten()
    p = p / np.sum(p)
    p = p[p > 0]
    return -np.sum(p * np.log(p))

def interface_strength(A):
    grad = 0
    n, m = A.shape
    for i in range(n-1):
        for j in range(m-1):
            grad += abs(A[i,j] - A[i+1,j])
            grad += abs(A[i,j] - A[i,j+1])
    return grad

def simulate_2d(n=100, m=100, steps=200, mode="fibonacci"):
    A = initialize_lattice_2d(n, m, mode)

    entropies = []
    interfaces = []

    for _ in range(steps):
        A = update_2d(A)
        entropies.append(entropy(A))
        interfaces.append(interface_strength(A))

    return A, entropies, interfaces
