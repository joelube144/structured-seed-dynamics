import matplotlib.pyplot as plt
from simulation_2d import simulate_2d

if __name__ == "__main__":
    final_fib, ent_fib, int_fib = simulate_2d(mode="fibonacci")
    final_rand, ent_rand, int_rand = simulate_2d(mode="random")

    plt.figure()
    plt.imshow(final_fib)
    plt.title("Fibonacci Final State")
    plt.colorbar()

    plt.figure()
    plt.imshow(final_rand)
    plt.title("Random Final State")
    plt.colorbar()

    plt.figure()
    plt.plot(ent_fib, label="Fibonacci")
    plt.plot(ent_rand, label="Random")
    plt.legend()
    plt.title("Entropy")

    plt.figure()
    plt.plot(int_fib, label="Fibonacci")
    plt.plot(int_rand, label="Random")
    plt.legend()
    plt.title("Interface Strength")

    plt.show()
