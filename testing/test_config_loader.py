import sys
import os
import unittest

sys.path.insert(0,'../')
from SentientSharedLibraries.config_loader import ConfigLoader


class MyTest(unittest.TestCase):
    def test_influxdb(self):
        local = ConfigLoader('test.conf')
        assert local.config['influxdb']
    def test_influxdb_address(self):
        local = ConfigLoader('test.conf')
        assert local.config['influxdb']['address']
    def test_influxdb_port(self):
        local = ConfigLoader('test.conf')
        assert local.config['influxdb']['port']
    def test_influxdb_password(self):
        local = ConfigLoader('test.conf')
        assert local.config['influxdb']['password']
    def test_influxdb_user(self):
        local = ConfigLoader('test.conf')
        assert local.config['influxdb']['user']
    def test_influxdb_db(self):
        local = ConfigLoader('test.conf')
        assert local.config['influxdb']['db']

