import numpy as np


def hadamard_walsh(f):
    """
    Compute the Hadamard-Walsh transform of a signal f.
    f must be of length N = 2^n.
    """
    N = len(f)
    if N & (N - 1) != 0:
        raise ValueError("Length of the signal must be a power of 2.")

    n = int(np.log2(N))
    x = np.array(f)

    for j in range(n):
        step = 2 ** (j + 1)
        for k in range(0, N, step):
            for i in range(step // 2):
                a = x[k + i]
                b = x[k + i + step // 2]
                x[k + i] = a + b
                x[k + i + step // 2] = a - b
                print(x)

    return x


def inverse_hadamard_walsh(s):
    """
    Compute the inverse Hadamard-Walsh transform of a signal s.
    s must be of length N = 2^n.
    """
    N = len(s)
    transformed = hadamard_walsh(s)
    return transformed / N


if __name__ == "__main__":
    test_lengths = [4]
    for N in test_lengths:
        print(f"Testing with N = {N}")
        f = np.array([1, 1, 1, 1])  # Generate random vector
        print("Original vector:", f)

        # Forward transform
        s = hadamard_walsh(f)
        print("Transformed vector:", s)

        # # Inverse transform
        # f_reconstructed = inverse_hadamard_walsh(s)
        # print("Reconstructed vector:", f_reconstructed)
        #
        # # Check correctness
        # if np.allclose(f, f_reconstructed):
        #     print("Test passed!")
        # else:
        #     print("Test failed.")
        # print()