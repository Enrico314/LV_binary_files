"""
This calss test the beam class
"""

import logging
import sys

import pytest
import io

from LV_binary_files.lvbf import LV_fd

_logger = logging.getLogger(__name__)

"""Setup basic logging"""
log_format = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
logging.basicConfig(
    level="DEBUG", stream=sys.stderr, format=log_format, datefmt="%Y-%m-%d %H:%M:%S"
)


def test_constructur():
    b = io.BytesIO(bytes.fromhex("505448300000000B0000000201430466696C65"))
    a = LV_fd()
    a.fobj = io.BufferedRandom(b)
