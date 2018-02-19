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

import apt
import sys
import argparse
import launchpadlib
from launchpadlib.launchpad import Launchpad

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="The path of the input file", required=True)
parser.add_argument("-u", "--lp-user", help="The Launchpad ID of the team you would like to subscribe the bugs to", required=True)
parser.add_argument("-r", "--remove", action="store_true", help="Instead of subscribing to the packages, unsubscribe")
args = parser.parse_args()

def no_credential():
    raise ValueError("Can't proceed without Launchpad credentials.")

lp = Launchpad.login_with("masspackagelp", "production", credential_save_failed=no_credential)

def main():
    while True:
        try:
            with open(args.file, "r") as ins:
                filelines = []
                for line in ins:
                    filelines.append(line.strip())
            break
        except FileNotFoundError:
            raise FileNotFoundError("File not found.")

    if not args.remove:
        for i in range(len(filelines)):
            try:
                lp.distributions["ubuntu"].getSourcePackage(name=filelines[i]).addBugSubscription(subscriber=lp.people[args.lp_user])
                print("Successfully added subscription for " + filelines[i])
            except AttributeError:
                print("Source package " + filelines[i] + " not found")
    else:
        for i in range(len(filelines)):
            print("Removing subscription for: " + filelines[i])
            try:
                lp.distributions["ubuntu"].getSourcePackage(name=filelines[i]).removeBugSubscription(subscriber=lp.people[args.lp_user])
                print("Successfully removed subscription for " + filelines[i])
            except AttributeError:
                print("Source package not found.")
            except:
                print(args.lp_user + " is not subscribed to " + filelines[i] + " so not removing")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit()
