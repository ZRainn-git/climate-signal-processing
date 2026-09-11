import numpy as np
from scipy.signal import lfilter


def compute_direct_form_coefficients(f0, fs, epsilon, M):
    """
    Compute numerator and denominator coefficients for the notch filter.

    Parameters
    ----------
    f0 : float
        Target notch frequency.
    fs : float
        Sampling frequency.
    epsilon : float
        Parameter controlling the pole/zero spacing.
    M : float
        Normalization factor.

    Returns
    -------
    numerator : list
        Filter numerator coefficients [a, b, c].
    denominator : list
        Filter denominator coefficients [1, F, G].
    """
    a = M
    b = -2 * M * np.cos(2 * np.pi * f0 / fs)
    c = M

    F = -2 * (1 + epsilon) * np.cos(2 * np.pi * f0 / fs)
    G = (1 + epsilon) ** 2

    return [a, b, c], [1, F, G]


def ratFilter(N, D, x):
    """
    Apply a rational digital filter to a one-dimensional signal.

    Parameters
    ----------
    N : array-like
        Numerator coefficients.
    D : array-like
        Denominator coefficients.
    x : array-like
        Input signal.

    Returns
    -------
    numpy.ndarray
        Filtered output signal.
    """
    N = np.asarray(N, dtype=float)
    D = np.asarray(D, dtype=float)

    if D[0] != 1:
        N = N / D[0]
        D = D / D[0]

    return lfilter(N, D, x)
