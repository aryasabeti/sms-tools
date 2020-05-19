import numpy as np
import sys
import matplotlib.pyplot as plt

"""
A2-Part-2: Generate a complex sinusoid 

Write a function to generate the complex sinusoid that is used in DFT computation of length N (samples), 
corresponding to the frequency index k. Note that the complex sinusoid used in DFT computation has a 
negative sign in the exponential function.

The amplitude of such a complex sinusoid is 1, the length is N, and the frequency in radians is 2*pi*k/N.

The input arguments to the function are two positive integers, k and N, such that k < N-1. 
The function should return cSine, a numpy array of the complex sinusoid.

EXAMPLE: If you run your function using N=5 and k=1, the function should return the following numpy array cSine:
array([ 1.0 + 0.j,  0.30901699 - 0.95105652j, -0.80901699 - 0.58778525j, -0.80901699 + 0.58778525j, 
0.30901699 + 0.95105652j])
"""
def genComplexSine(k, N):
    """
    Inputs:
        k (integer) = frequency index of the complex sinusoid of the DFT
        N (integer) = length of complex sinusoid in samples
    Output:
        The function should return a numpy array
        cSine (numpy array) = The generated complex sinusoid (length N)
    """
    π = np.pi
    frequency = 2 * π * k / N
    sample_times = np.arange(0, N)
    complex_sin = np.vectorize(lambda t: np.exp(-1j * frequency * t))
    return complex_sin(sample_times)


if __name__ == '__main__':
    test = False
    if len(sys.argv) == 3:
        k = int(sys.argv[1])
        N = int(sys.argv[2])
    else:
        test = True

    if test:
        # test case
        expected = np.array([1.0 + 0.j,  0.30901699 - 0.95105652j, -0.80901699 - 0.58778525j, -0.80901699 + 0.58778525j,
    0.30901699 + 0.95105652j])
        expected_len = expected.shape[0]

        # generate COMPLEX sinusoid based on test case
        k = 1
        N = 5
        actual = genComplexSine(k, N)
        actual_len = actual.shape[0]

        # test correct output size
        print(f"FAIL: output size mismatch. expected: {expected_len}; actual: {actual_len}") \
            if actual_len != expected_len else ""

        # test output values
        for a, e in zip(actual, expected):
            print(f"FAIL:\nexpected: {expected}\nactual:   {actual}") \
                if (a.real - e.real > 0.001 or a.imag - e.imag > 0.001) else ""

        sample_times = np.arange(0, N)
        plt.plot(sample_times, np.real(actual), label="actual real", color="red")
        plt.plot(sample_times, np.imag(actual), label="actual imag", color="pink")

        plt.plot(sample_times, np.real(expected), label="expected real", color="blue", linestyle='dotted')
        plt.plot(sample_times, np.imag(expected), label="expected imag", color="teal", linestyle='dotted')

        plt.title('test data comparision')
        plt.legend()
        plt.xlabel('time')
        plt.ylabel('amplitude')

        plt.show()
    else:
        actual = genComplexSine(k, N)
        sample_times = np.arange(0, N)

        plt.plot(sample_times, np.real(actual), label="actual real", color="red")
        plt.plot(sample_times, np.imag(actual), label="actual imag", color="pink")
        plt.legend()
        plt.xlabel('time')
        plt.ylabel('amplitude')
        plt.show()