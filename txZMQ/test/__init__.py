"""
Tests for L{txZMQ}.
"""

from twisted.internet import defer, reactor


def _wait(interval):
    d = defer.Deferred()
    reactor.callLater(interval, d.callback, None)

    return d
