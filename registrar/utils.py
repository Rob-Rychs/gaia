"""
    Registrar
    ~~~~~

    copyright: (c) 2014 by Halfmoon Labs, Inc.
    copyright: (c) 2015 by Blockstack.org

This file is part of Registrar.

    Registrar is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Registrar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Registrar. If not, see <http://www.gnu.org/licenses/>.
"""

from pybitcoin import hex_hash160
import json


def get_hash(profile):

    if type(profile) is not dict:
        try:
            # print "WARNING: converting to json"
            profile = json.loads(profile)
        except:
            print "WARNING: not valid json"

    return hex_hash160(json.dumps(profile, sort_keys=True))


def pretty_print(data):

    try:
        data = data[0]
    except:
        pass

    if type(data) is not dict:
        try:
            data = json.loads(data)
        except Exception as e:
            print "got here"
            print e

    print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))