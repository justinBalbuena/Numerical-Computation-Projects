import numpy as np


def hadamard_walsh(f):
    """
    Compute the Hadamard-Walsh transform of a signal f.
    f must be of length N = 2^n.
    """
    N = len(f)

    if N & (N - 1) != 0:  # Check if N is a power of 2
        raise ValueError("Length of the signal must be a power of 2.")

    x = np.array(f)
    n = int(np.log2(N))  # Number of iterations (log2 of N)

    for j in range(1, n + 1):  # Iterate over log2(N) iterations
        for r in range(1, 2 ** (j - 1) + 1):  # Iterate over groups in the j-th iteration
            m = N // r  # Size of the group

            # Calculate the index of the first element in the group
            s = (r - 1) * m

            # First half of the group: apply sum
            for k in range(s, s + m // 2):
                x[k] = x[k] + x[k + m // 2]

            # Second half of the group: apply difference
            for k in range(s + m // 2, N):
                x[k] = x[k - m // 2] - x[k]

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
