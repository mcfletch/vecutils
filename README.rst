Python VecUtils
================

Numpy vector manipulation code suitable for developing scenegraph
engines for use with OpenGL (or OpenGL-like) libraries.

Purpose
-------

VecUtils are the various utility bits from PyVRML97 and OpenGLContext
which provide the vector (and triangle) manipulation code. This is 
not an attempt to provide a universal library, but rather is the 
set of code developed to produce a working scenegraph engine.

The hope is that in breaking out these bits they can be cleaned up 
and become useful for others who want to do something similar to 
OpenGLContext without requiring huge dependencies.

Installation
-------------

VecUtils is a python library, use:

..code:: bash

    pip install git+http://github.com/mcfletch/vecutils#egg=vecutils 
    
to get the current HEAD. Which is the only current version. You will 
have to have git installed for that to work, obviously.
