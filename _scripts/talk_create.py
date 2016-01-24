#!/usr/bin/env python
""" This script creates all desired versions of the material for each talk.
"""

# standard library
import os

# Creates the pdf version from the notes.
os.system('libreoffice --headless --convert-to pdf talk.notes.odt')