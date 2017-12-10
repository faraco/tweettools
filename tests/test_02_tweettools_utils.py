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
import tweettools_utils
import os

tu = tweettools_utils.Utils()

class TestUtils(unittest.TestCase):
    """Handle utilities tests."""
    
    def test_send_tweet(self):
        """Send tweet to timeline."""
        self.assertTrue(tu.send_tweet('hello world'))

    # NOTE skipped to avoid long test
    #def test_autofollow_back(self):
    #    """Auto following pending followers"""
    #
    #    self.assertTrue(tu.auto_followback())
    
    # NOTE skipped to avoid long test
    #def test_autounfollow_nonfollowers(self):
    #    """Auto unfollow the nonfollowers"""
    #    self.assertTrue(tu.autounfollow_nonfollowers())
