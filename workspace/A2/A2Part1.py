import numpy as np
import math
import matplotlib.pyplot as plt

"""
A2-Part-1: Generate a sinusoid

Write a function to generate a real sinusoid (use np.cos()) given its amplitude A, frequency f (Hz), initial phase phi (radians), 
sampling rate fs (Hz) and duration t (seconds). 

All the input arguments to this function (A, f, phi, fs and t) are real numbers such that A, t and fs are 
positive, and fs > 2*f to avoid aliasing. The function should return a numpy array x of the generated 
sinusoid.

EXAMPLE: If you run your code using A=1.0, f = 10.0, phi = 1.0, fs = 50.0 and t = 0.1, the output numpy 
array should be: array([ 0.54030231, -0.63332387, -0.93171798,  0.05749049,  0.96724906])
"""
def genSine(A, f, phi, fs, t):
    """
    Inputs:
        A (float) =  amplitude of the sinusoid
        f (float) = frequency of the sinusoid in Hz
        phi (float) = initial phase of the sinusoid in radians
        fs (float) = sampling frequency of the sinusoid in Hz
        t (float) =  duration of the sinusoid (is second)
    Output:
        The function should return a numpy array
        x (numpy array) = The generated sinusoid (use np.cos())
    """
    π = np.pi
    sample_times = np.arange(0, t, 1.0 / fs)
    cos = np.vectorize(lambda time: A * np.cos(2 * π * f * time + phi))
    return cos(sample_times)


if __name__ == '__main__':
    # test case
    expected = np.array([0.54030231, -0.63332387, -0.93171798,  0.05749049,  0.96724906])
    expected_len = expected.shape[0]

    # generate sinusoid based on test case
    A = 1.0
    f = 10.0
    phi = 1.0
    fs = 50.0
    t = 0.1
    actual = genSine(A, f, phi, fs, t)
    actual_len = actual.shape[0]

    # test correct output size
    print(f"FAIL: output size mismatch. expected: {expected_len}; actual: {actual_len}") \
        if actual_len != expected_len else ""

    # test output values
    for a, e in zip(actual, expected):
        print(f"FAIL: expected: {expected}; actual: {actual}") \
            if not math.fabs(a - e) < 0.001 else ""

    sample_times = np.arange(0, t, 1.0 / fs)
    plt.plot(sample_times, actual, label="actual")
    plt.plot(sample_times, expected, label="expected")
    plt.legend()
    plt.xlabel('time')
    plt.ylabel('amplitude')

    plt.show()
