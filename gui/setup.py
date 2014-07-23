from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')
data_file = [('', ['ui.ui','trans.py'])]

setup(
    
   
   data_files = data_file ,
   windows=[{"script":"gui.py"}], options={"py2exe":{"includes":["sip"]}}
    
)