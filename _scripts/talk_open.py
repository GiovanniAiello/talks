#!/usr/bin/env python
""" This script creates and serves a local slide show.
"""

# standard library
import os

# Create and serve the slides.
os.system('ipython nbconvert --to slides talk.slides.ipynb --post serve')