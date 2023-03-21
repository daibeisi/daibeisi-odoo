"""
本地库
"""

from .QYMP import QYMP
qymp = QYMP(corpid="", corpsecret="")

__all__ = ['qymp']

__version__ = '0.0.1'