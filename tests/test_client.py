import socket
import unittest
from unittest.mock import Mock

from client import receive, connection


class TestReceive(unittest.TestCase):

    def test_receive(self):

        sock = Mock()
        sock.recv.return_value = b'test'
        result = receive(sock)

        sock.recv.assert_called_once_with(4096)
        self.assertEqual(result, "test")


class TestConnection(unittest.TestCase):

    def test_connection(self):

        self.assertIsNotNone(connection())
