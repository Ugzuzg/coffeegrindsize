#!/usr/bin/env python
# -*- coding: utf-8 -*-#
###############################################################################
#
# fix_info_plist.py: Support script for coffeegrindsize Mac executable build
#
###############################################################################
#
# This file contains a Python script to assist in the process of
# building a Mac executable for the coffeegrindsize application.
#
# Its input is the default Info.plist file that pyinstaller generates.
# It modifies that file as follows:
#
#   - Changes the value of CFBundleShortVersionString to the version
#     number in the version.txt file
#   - Adds NSHumanReadableCopyright with the copyright string
#   - Adds NSHighResolutionCapable, set to True
#   - Adds NSRequiresAquaSystemAppearance, set to True (NO Dark Mode)
#
#  usage: fix_info_plist.py [-h] info_plist_file
#
#  positional arguments:
#    info_plist_file  (full or relative path)
#
#  optional arguments:
#    -h, --help       show this help message and exit
#
import argparse
import plistlib
import os


# Parse command line args
parser = argparse.ArgumentParser()
parser.add_argument("version", type=str, nargs=1, help=("app version"))
parser.add_argument("info_plist", metavar='info_plist_file',
                    type=str, nargs=1,
                    help=("(full or relative path)"))
args = parser.parse_args()

# Get the version number
app_path = os.path.join(".", "dist", "coffeegrindsize")
version = args.version[0]

# Read Info.plist into a plist object
try:
    # Python 3
    with open(args.info_plist[0], 'rb') as fp:
        plist = plistlib.load(fp)
except AttributeError:
    # Python 2
    plist = plistlib.readPlist(args.info_plist[0])

# Change version number
plist['CFBundleShortVersionString'] = version

# Add copyright string
plist['NSHumanReadableCopyright'] = u"Copyright © 2021  Jonathan Gagne"

# Enable retina display resolution
plist['NSHighResolutionCapable'] = True

# Write the modified plist back to the Info.plist file
if hasattr(plistlib, 'dump'):
    # Python 3
    plist['NSRequiresAquaSystemAppearance'] = True  # DISABLE dark mode
    with open(args.info_plist[0], 'wb') as fp:
        plistlib.dump(plist, fp)
else:
    # Python 2
    plistlib.writePlist(plist, args.info_plist[0])
