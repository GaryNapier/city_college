#!/usr/bin/env python3

"""Tests for hello.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './hello.py'

def test_exists():
    """exists"""

    assert os.path.isfile(prg)

def test_runnable():
    """Runs using python3"""

    out = getoutput(f'python3 {prg}')
    assert out.strip() == 'Hello, World!'

def test_executable():
    """Says 'Hello, World!' by default"""

    out = getoutput(prg)
    assert out.strip() == 'Hello, World!'

