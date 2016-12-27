#!/usr/bin/env python
""" This module builds all material and updates the GitHub repository.
"""

# standard library
import os

# Publish most recent material of current directory online.
os.system("git commit -m'committing' -- .")
os.system("git push")

