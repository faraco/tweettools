""" 
    tweettool - A command line program to automate common Twitter usage.
    Copyright (C) 2017 faraco <skelic3@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import unittest
import tweettools_config
import os
import yaml

CONSUMER_KEY = os.getenv('T_CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('T_CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('T_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('T_ACCESS_TOKEN_SECRET')
TWITTER_HANDLE = os.getenv('T_HANDLE')


tc = tweettools_config.Config(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET,
        TWITTER_HANDLE
)

class TestConfig(unittest.TestCase):
    """Handle configuration testing"""

    def test_write_to_config(self):
        """Test config generation"""

        tc.write_to_config()
        try:
            with open(tweettools_config.CONFIG_PATH, 'r') as infile:
                indata = yaml.load(infile)
        except OSError:
            raise

        self.assertEqual(indata['consumer_key'], CONSUMER_KEY)
        self.assertEqual(indata['consumer_secret'], CONSUMER_SECRET)
        self.assertEqual(indata['access_token'], ACCESS_TOKEN)
        self.assertEqual(indata['access_token_secret'], ACCESS_TOKEN_SECRET)
        self.assertEqual(indata['twitter_handle'], TWITTER_HANDLE)
