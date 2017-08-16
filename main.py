#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
