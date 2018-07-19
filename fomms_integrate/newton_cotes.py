"""
newton_cotes.py
Integrate package for MolSSI

Handles the primary functions
"""


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


 """
This file contains the implementation of the trapezoidal rule
"""

import numpy as np

def trapz(x, f):
    """ 
    Compute a 1D definite integral using the trapezoidal rule
    Parameters
    ----------
    f : function
        User defined function.
    x : numpy array
        Integration domain.
    Returns
    -------
    I : float
        Integration result.
    """   
    a = x[0]
    b = x[1]
    ya = f(a)
    yb = f(b)
    I = (b-a) * (ya + yb) / 2
    return I


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
