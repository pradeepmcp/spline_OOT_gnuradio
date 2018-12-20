#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/Users/pradmc/gnuradio/OOT/gr-custom_resampler/python
export PATH=/Users/pradmc/gnuradio/OOT/gr-custom_resampler/python/python:$PATH
export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH
export PYTHONPATH=/Users/pradmc/gnuradio/OOT/gr-custom_resampler/python/swig:$PYTHONPATH
/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/python2 /Users/pradmc/gnuradio/OOT/gr-custom_resampler/python/qa_spline_resampler_fff.py 
