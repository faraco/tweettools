""" 
    <one line to give the program's name and a brief idea of what it does.>
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

CONFIG_PATH = '{}/.tweettools_config.yaml'.format(os.path.expanduser('~'))

class Config:
    def __init__(self, con_key, con_secr, acc_token, acc_token_secr, t_handle):
        self.con_key = con_key
        self.con_secr = con_secr
        self.acc_token = acc_token
        self.acc_token_secr = acc_token_secr
        self.t_handle = t_handle

        self.data_dict = dict(
            consumer_key = self.con_key,
            consumer_secret = self.con_secr,
            access_token = self.acc_token,
            access_token_secret = self.acc_token_secr,
            twitter_handle = self.t_handle
        )

    def write_to_config(self):
        """Write twitter credentials to the configuration file"""
        try:
            with open(CONFIG_PATH, 'w+') as outfile:
                yaml.dump(self.data_dict, outfile, default_flow_style=False)

            print('Configuration file at {} is generated.'.format(CONFIG_PATH))

        except OSError:
            raise
