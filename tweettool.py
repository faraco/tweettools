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
import os

def generate_config_prompt():
    """Prompt user to write or edit twitter credentials configs"""

    print('\n***Write configuration file***\n')
    con_key = input('Consumer Key: ')
    con_secr = input('Consumer Secret: ')
    acc_token = input('Access Token: ')
    acc_token_secr = input('Access Token Secret: ')
    t_handle = input('Twitter Handle: ')

    return con_key, con_secr, acc_token, acc_token_secr, t_handle
    

def main():
    """Main program"""
    
    # Run the config prompt if the config file is not exist.
    if not os.path.isfile(tweettools_config.CONFIG_PATH):
        print('Executing automatic file generation')

        key = generate_config_prompt()

        tt_config = tweettools_config.Config(key[0], key[1], key[2], key[3], key[4])
        tt_config.write_to_config()

    # this needs the config file to be generated first, so had to import after config file is generated in the first run.
    import tweettools_utils


    parser = argparse.ArgumentParser(description='Automating Twitter common usage.')

    parser.add_argument('-s', '--setup', action='store_true', dest='setup_t', default=False, help='Setup Twitter credentials configuration.')

    parser.add_argument('-fb', '--followback', action='store_true', dest='followback_t', default=False, help='Auto follow back pending users.')
    
    args = parser.parse_args()

    tt_utils = tweettools_utils.Utils()
    tt_config = ''
    
    if args.setup_t:
        key = generate_config_prompt()
        
        tt_config = tweettools_config.Config(key[0], key[1], key[2], key[3], key[4])
        tt_config.write_to_config()

    elif args.followback_t:
        print('Executing auto follow back followers..')
        tt_utils.auto_followback()

if __name__ == '__main__':
    main()
