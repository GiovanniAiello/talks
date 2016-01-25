#!/usr/bin/env python
""" This script creates all desired versions of the material for each talk.
"""

# project library
from auxiliary import cleanup
from auxiliary import run

# Create a pdf version of the accompanying notes.
for type_ in ['pdflatex', 'bibtex', 'pdflatex', 'pdflatex']:
    run(type_)
cleanup()
