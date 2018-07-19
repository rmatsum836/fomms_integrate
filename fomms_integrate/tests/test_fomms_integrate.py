"""
Unit and regression test for the fomms_integrate package.
"""

# Import package, test suite, and other packages as needed
import fomms_integrate
import pytest
import sys

def test_fomms_integrate_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "fomms_integrate" in sys.modules
