#!/usr/bin/env python
""" Create presentation and manuscript.
"""
# project library
from _auxiliary import *

# global variables
DOCUMENTS = ['slides', 'script']

''' Execution of module as script.
'''
if __name__ == '__main__':
        
    # Compile documents.
    for type_ in ['pdflatex', 'bibtex', 'pdflatex', 'pdflatex']:

        for document in DOCUMENTS:
            
            run(type_, document)
            
    # Copying of files.
    for document in DOCUMENTS:
        
        copy(document)   

    # Finishing.
    cleanup(all_=False) 