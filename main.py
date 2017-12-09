#!/usr/bin/env python3

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

import argparse
import tweettools_config
import tweettools_utils
import twitter_follow_bot as tfb

def main():
    """Main program"""
    
    parser = argparse.ArgumentParser(description='Automating Twitter common usage.')
    parser.add_argument('-fb', '--followback', action='store_true', dest='followback_t', default=False, help='Auto follow back pending users.')
    
    args = parser.parse_args()

    tt_utils = tweettools_utils.Utils()

    if args.followback_t:
        print('Executing auto follow back followers..')
        tt_utils.auto_followback()
if __name__ == '__main__':
    main()
