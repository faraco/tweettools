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

import twitter_follow_bot as tfb
import twitter

class Utils:
    """Handle tweettool utilities."""

    def __init__(self):
        self.tw = twitter.Twitter(
                auth = twitter.OAuth(
                    tfb.ACCESS_TOKEN,
                    tfb.ACCESS_TOKEN_SECRET,
                    tfb.API_KEY,
                    tfb.API_SECRET
                )
        )
        

    def send_tweet(self, text):
        """Send tweet to user's timeline."""
        
        try:
            results = self.tw.statuses.update(status=text)
            return results

        except twitter.TwitterHTTPError as e:
            print("Error: {}".format(e))

    def auto_followback(self):
        """Simple wrapper for following back the users following you."""
        tfb.auto_follow_followers()

    def autounfollow_nonfollowers(self):
        """Simple wrapper to unfollow non followers"""
        tfb.auto_unfollow_nonfollowers()
