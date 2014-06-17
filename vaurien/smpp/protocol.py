from twisted.internet.protocol import Protocol

import vaurien.protocols.base.BaseProtocol
import smpp.pdu

"""
SMPP Protocol handling for Vaurien. Bulk of the work is done by smpp.pdu.

http://vaurien.readthedocs.org/en/1.8/extending.html#extending
"""

class SMPP(BaseProtocol, Protocol):
    """
    Extends both BaseProtocol from Vaurien and Protocol from Twisted.
    """

    name = "smpp"
    options = {"port": ("Port where vaurien will bind", int, 16981),}

    def _handle(self, source, dest, to_backend):
        data = self._get_data(source)
