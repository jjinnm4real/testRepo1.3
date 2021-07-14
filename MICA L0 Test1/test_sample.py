#from https://docs.pytest.org/en/latest/
import os, sys, time
import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
