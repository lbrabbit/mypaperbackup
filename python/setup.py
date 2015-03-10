from distutils.core import setup
import py2exe

setup(name="main",
      version="0.1",
      windows=["main.py"],
      options = {'py2exe': {'includes': ['encodings.utf_8']}})

