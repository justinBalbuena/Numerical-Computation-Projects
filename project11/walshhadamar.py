import numpy as np


def hadamard_walsh(f):
    # Check if N is a power of 2
    N = len(f)
    if N & (N - 1) != 0:
        raise ValueError("Length of the signal must be a power of 2.")

    n = int(np.log2(N))

    x = np.array(f)

    for j in range(n):
        y = np.copy(x)

        for k in range(0, N, 2 ** (j + 1)):
            for i in range(2 ** (j)):
                a = x[k + i]
                b = x[k + i + 2 ** (j)]
                y[k + i] = a + b
                y[k + i + 2 ** (j)] = a - b

        x = np.copy(y)

    return x

def inverse_hadamard_walsh(s):
    N = len(s)
    transformed = hadamard_walsh(s)
    return transformed / N

if __name__ == "__main__":
    print(f"Testing with N = 4")
    f = np.array([1, 1, 1, 1])
    print("Original vector:", f)
    s = hadamard_walsh(f)
    print("Transformed vector:", s)

    # Inverse transform
    f_reconstructed = inverse_hadamard_walsh(s)
    print("Reconstructed vector:", f_reconstructed)

    print("-------------------------\n")

    print(f"Testing with N = 8")
    f = np.array([1, 1, 1, 1, 1, 1, 1, 1])
    print("Original vector:", f)
    s = hadamard_walsh(f)
    print("Transformed vector:", s)

    # Inverse transform
    f_reconstructed = inverse_hadamard_walsh(s)
    print("Reconstructed vector:", f_reconstructed)

    print("-------------------------\n")

    print(f"Testing with N = 16")
    f = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    print("Original vector:", f)
    s = hadamard_walsh(f)
    print("Transformed vector:", s)

    # Inverse transform
    f_reconstructed = inverse_hadamard_walsh(s)
    print("Reconstructed vector:", f_reconstructed)

    print("-------------------------\n")
