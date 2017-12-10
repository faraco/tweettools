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

import os
import yaml
import twitter_follow_bot as tfb
import tweettools_config

class Utils:
    """Handle tweettool utilities."""

    def auto_followback(self):
        """Simple wrapper for following back the users following you."""
        tfb.auto_follow_followers()

    def autounfollow_nonfollowers(self):
        """Simple wrapper to unfollow non followers"""
        tfb.auto_unfollow_nonfollowers()
