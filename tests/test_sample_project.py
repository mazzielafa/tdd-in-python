import pytest

from app import app



def test_version():
    assert __version__ == '0.1.0'
