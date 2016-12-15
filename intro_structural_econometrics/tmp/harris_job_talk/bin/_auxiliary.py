''' Auxiliary functions for the refereeing process.
'''

# standard library
import subprocess
import fnmatch
import shutil
import glob
import os

def remove(path):
    ''' Remove path, where path can be either a directory or a file. The
        appropriate function is selected. Note, however, that if an 
        OSError occurs, the function will just path.
    '''

    if os.path.isdir(path):

        shutil.rmtree(path)
    
    if os.path.isfile(path):

        os.remove(path)

def run(type_, document):
    ''' Run Latex in directory dir_.
    '''
    current = os.getcwd()
    
    os.chdir(document)

    p = subprocess.Popen((type_, 'main'))
    
    p.wait()    

    os.chdir(current)
    
def copy(document):
    ''' Copy document to main directory.
    '''
    current = os.getcwd()
    
    os.chdir(document)
    
    src = 'main.pdf'
    dst = '../eisenhauer-' + document + '.pdf'
    
    shutil.copy(src, dst)
    
    os.chdir(current)

def cleanup(all_ = True):
    ''' Remove nuisance files from the directory tree.

    '''

    matches = []

    for root, _, filenames in os.walk('.'):

        for filetypes in ['*.aux','*.log','*.pyc', '*.so', '*~', '*tar', \
                          '*.bbl', '*.blg', '*.out', \
                          '*.zip', '.waf*', '*lock*', '*.mod', '*.a', '*.snm', \
                          '*.toc', '*.nav', '*.fdb_latexmk', '*.fls', 'main.pdf']:

                for filename in fnmatch.filter(filenames, filetypes):
                    
                    matches.append(os.path.join(root, filename))

    matches += ['presentation/main.pdf', 'script/main.pdf', 'bin/__pycache__']

    if(all_): matches += glob.glob('eisenhauer-*')

    for files in matches:

        remove(files)