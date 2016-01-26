""" This module contains auxiliary functions for the talk workflow.
"""
import subprocess
import fnmatch
import shutil
import os


def remove(path):
    """ Remove path, where path can be either a directory or a file. The
        appropriate function is selected. Note, however, that if an
        OSError occurs, the function will just path.
    """
    if os.path.isdir(path):

        shutil.rmtree(path)

    if os.path.isfile(path):

        os.remove(path)


def cleanup():
    """ Remove nuisance files from the directory tree.
    """

    matches = []
    for root, _, filenames in os.walk('.'):
        for filetypes in ['*.aux', '*.log', '*.pyc', '*.so', '*~', '*tar',
                          '*.bbl', '*.blg', '*.out', '*.zip', '.waf*',
                          '*lock*', '*.mod', '*.a', '*.snm', '*.toc',
                          '*.nav', '*.slides.html']:
                for filename in fnmatch.filter(filenames, filetypes):
                    matches.append(os.path.join(root, filename))

    for files in matches:
        remove(files)

    remove('.ipynb_checkpoints')


def run(type_):
    """ Run Latex in directory dir_.
    """
    p = subprocess.Popen((type_, 'notes'))
    p.wait()