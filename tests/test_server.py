import unittest
import json
import socket

import unittest.mock as mock
from server import HandleName, Response, receive, send


class TestHandleName(unittest.TestCase):

    def test_handle_name(self):
        handle_name = HandleName()
        handle_name.setName('addr', 'aname')
        self.assertEqual(handle_name.selName('addr'), 'aname')


class TestResponse(unittest.TestCase):

    def test_rain(self):
        self.assertTrue('there be rain tomorrow'.islower())

    def test_get_rain(self):

        conn = mock.Mock()
        addr = mock.Mock()
        response = Response(conn, addr)
        response.getRain()
        self.assertFalse(response.rain, False)

    def test_getLuckyNum(self):

        conn = mock.Mock()
        addr = mock.Mock()
        response = Response(conn, addr)
        response.getLuckyNum()
        self.assertNotEqual(response.getLuckyNum(), 0)


class TestReceive(unittest.TestCase):

    def test_receive(self):

        conn = mock.Mock()
        conn.recv.return_value = b'test'
        result = receive(conn)

        conn.recv.assert_called_once_with(4096)
        self.assertEqual(result, 'test')
