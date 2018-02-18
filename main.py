#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Copyright (C) 2015-2018 Lubuntu Developers <lubuntu-devel@lists.ubuntu.com>
Authored by Simon Quigley <tsimonq2@ubuntu.com>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

A copy of the GNU General Public License version 2 is in license.txt.
"""

import sys
import launchpadlib
from launchpadlib.launchpad import Launchpad

def no_credential():
    print("Can't proceed without Launchpad credentials.")
    sys.exit()

lp = Launchpad.login_with('Mass package bug subscription adder', 'production', credential_save_failed=no_credential)
teamtowrite = (input('What person/team would you like to use for this? (Launchpad ID) '))

while True:
    try:
        filepath = (input('Please specify the path of the input file: '))
        with open(filepath, "r") as ins:
            filearray = []
            for line in ins:
                filearray.append(line.strip())
        break
    except FileNotFoundError:
        print("File not found.")

for i in range(len(filearray)):
    print("Assigning:")
    print(filearray[i])
    try:
        lp.distributions['ubuntu'].getSourcePackage(name=filearray[i]).addBugSubscription(subscriber=lp.people[teamtowrite])
    except AttributeError:
        print("Source package not found.")
    print("Complete")
